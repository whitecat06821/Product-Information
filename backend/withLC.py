from langchain.chains import TransformChain
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from image import load_image
import os
from langchain_core.runnables import chain
from langchain import globals
from Product import Product
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
import openai
import httpx
import traceback
import time
from datetime import datetime, timedelta
import asyncio
from typing import Optional, Dict, Any

load_dotenv()

# Get proxy settings from environment variables
# proxy_host = os.getenv('PROXY_HOST')
# proxy_port = os.getenv('PROXY_PORT')
# proxy_username = os.getenv('PROXY_USERNAME')
# proxy_password = os.getenv('PROXY_PASSWORD')

# Configure proxy settings
# Construct the proxy URL explicitly from individual components
# proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}" if all([proxy_username, proxy_password, proxy_host, proxy_port]) else None

# If proxy_url is None, check if PROXY_URL environment variable is set as a fallback
# if not proxy_url:
#     proxy_url = os.getenv('PROXY_URL')
#     if proxy_url:
#       print("Using PROXY_URL environment variable as fallback.")
# else:
#     print("Constructed proxy URL from components.")

# Initialize parser first
parser = JsonOutputParser(pydantic_object=Product)

# Rate limiting configuration
RATE_LIMIT_TOKENS = 100000  # Tokens per minute
RATE_LIMIT_WINDOW = 60  # 1 minute window
TOKEN_BUFFER = 0.8  # Use 80% of the rate limit to be safe

class RateLimiter:
    def __init__(self, tokens_per_minute: int, window_seconds: int = 60):
        self.tokens_per_minute = tokens_per_minute
        self.window_seconds = window_seconds
        self.tokens_used = 0
        self.window_start = datetime.now()
        self.lock = asyncio.Lock()

    async def acquire(self, tokens: int) -> None:
        async with self.lock:
            now = datetime.now()
            # Reset window if needed
            if (now - self.window_start).total_seconds() >= self.window_seconds:
                self.tokens_used = 0
                self.window_start = now

            # Calculate available tokens
            available_tokens = self.tokens_per_minute - self.tokens_used

            if tokens > available_tokens:
                # Calculate wait time
                wait_time = self.window_seconds - (now - self.window_start).total_seconds()
                if wait_time > 0:
                    await asyncio.sleep(wait_time)
                    self.tokens_used = 0
                    self.window_start = datetime.now()
                else:
                    self.tokens_used = 0
                    self.window_start = now

            self.tokens_used += tokens

# Initialize rate limiter
rate_limiter = RateLimiter(
    tokens_per_minute=int(RATE_LIMIT_TOKENS * TOKEN_BUFFER),
    window_seconds=RATE_LIMIT_WINDOW
)

load_image_chain = TransformChain(
    input_variables=['image_path'],
    output_variables=["image"],
    transform=load_image
)

# Set verbose
globals.set_debug(True)

class APIError(Exception):
    """Base class for API errors"""
    pass

class RateLimitError(APIError):
    """Raised when rate limit is exceeded"""
    pass

class ModelError(APIError):
    """Raised when there's an error with the model"""
    pass

async def retry_with_backoff(func, *args, max_retries=3, initial_delay=1):
    """Retry a function with exponential backoff"""
    delay = initial_delay
    last_error = None

    for attempt in range(max_retries):
        try:
            return await func(*args)
        except RateLimitError as e:
            last_error = e
            if attempt < max_retries - 1:
                await asyncio.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise
        except Exception as e:
            last_error = e
            if attempt < max_retries - 1:
                await asyncio.sleep(delay)
                delay *= 2
            else:
                raise

    raise last_error

@chain
async def image_model(inputs: dict):
    """Invoke model with image and prompt."""
    try:
        # Estimate tokens (rough estimation)
        estimated_tokens = len(inputs["prompt"].split()) * 1.3 + 1000  # Base tokens for image processing
        await rate_limiter.acquire(int(estimated_tokens))

        model = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.5,
            max_tokens=1024,
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        msg = await model.ainvoke(
            [
                HumanMessage(
                    content=[
                        {"type": "text", "text": inputs["prompt"]},
                        {"type": "text", "text": parser.get_format_instructions()},
                        {"type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{inputs['image']}"}},
                    ]
                )
            ]
        )
        return msg.content
    except openai.RateLimitError as e:
        print(f"Rate limit exceeded: {str(e)}")
        raise RateLimitError(f"Rate limit exceeded. Please try again later. Details: {str(e)}")
    except openai.APIError as e:
        print(f"OpenAI API error: {str(e)}")
        raise ModelError(f"Error communicating with OpenAI API: {str(e)}")
    except Exception as e:
        print(f"Unexpected error in image_model: {str(e)}")
        print("Full error details:")
        print(traceback.format_exc())
        raise APIError(f"An unexpected error occurred: {str(e)}")

async def get_product_info(image_bytes: bytes, prompt: str, tone: str, language: str) -> dict:
    print("Calling OpenAI API...")
    try:
        generate_product_chain = load_image_chain | image_model | parser

        # Wrap the chain invocation with retry logic
        result = await retry_with_backoff(
            generate_product_chain.ainvoke,
            {
                'image_path': image_bytes,
                'prompt': f"""
                Given the image of a product, provide the following information in {language}:
                - Product Title
                - Product Description
                - At least 13 Product Tags for SEO purposes
                - At most 3 primary Colors of the Product, excluding the background colors.
                {prompt}
                The tone of the description should be {tone.lower()}.
                """
            }
        )
        return result
    except RateLimitError as e:
        print(f"Rate limit error: {str(e)}")
        raise
    except ModelError as e:
        print(f"Model error: {str(e)}")
        raise
    except APIError as e:
        print(f"API error: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error during API call: {str(e)}")
        print("Full error details:")
        print(traceback.format_exc())
        raise APIError(f"An unexpected error occurred: {str(e)}")

# The test_proxy function is no longer needed if we are removing proxy functionality
# async def test_proxy():
#     print("Testing proxy connection...")
#     ...

# The main execution block for test_proxy is also removed
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(test_proxy())
