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

load_image_chain = TransformChain(
    input_variables=['image_path'],
    output_variables=["image"],
    transform=load_image
)

# Set verbose
globals.set_debug(True)

@chain
async def image_model(inputs: dict):
    """Invoke model with image and prompt."""
    # Using httpx.AsyncClient within the chain to manage its lifecycle per invocation
    # We'll remove the explicit http_client argument to see if Langchain handles it.
    # async with httpx.AsyncClient(timeout=30.0, verify=False) as client:
    try:
        # Create model with minimal required parameters
        model = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.5,
            max_tokens=1024,
            api_key=os.getenv("OPENAI_API_KEY"),
            # Removed http_client=client
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
    except Exception as e:
        print(f"Error in image_model: {str(e)}")
        # print("Full error details:")
        # print(traceback.format_exc())
        raise

async def get_product_info(image_bytes: bytes, prompt: str, tone: str, language: str) -> dict:
    print("Calling OpenAI API...")
    try:
        # Re-integrating the actual chain invocation
        generate_product_chain = load_image_chain | image_model | parser
        return await generate_product_chain.ainvoke({'image_path': image_bytes,
                                    'prompt': f"""
                                    Given the image of a product, provide the following information in {language}:
                                    - Product Title
                                    - Product Description
                                    - At least 13 Product Tags for SEO purposes
                                    - At most 3 primary Colors of the Product, excluding the background colors.
                                    {prompt}
                                    The tone of the description should be {tone.lower()}.
                                    """
                                    })
    except Exception as e:
        print(f"Error during API call: {str(e)}")
        # print("Full error details:")
        # print(traceback.format_exc())
        raise # Re-raise the exception after printing

# The test_proxy function is no longer needed if we are removing proxy functionality
# async def test_proxy():
#     print("Testing proxy connection...")
#     ...

# The main execution block for test_proxy is also removed
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(test_proxy())
