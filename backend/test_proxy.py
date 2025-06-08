import httpx
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

# Get proxy settings from environment variables
proxy_host = os.getenv('PROXY_HOST')
proxy_port = os.getenv('PROXY_PORT')
proxy_username = os.getenv('PROXY_USERNAME')
proxy_password = os.getenv('PROXY_PASSWORD')

# Configure proxy settings
# Construct the proxy URL explicitly from individual components
proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}" if all([proxy_username, proxy_password, proxy_host, proxy_port]) else None

# If proxy_url is None, check if PROXY_URL environment variable is set as a fallback
if not proxy_url:
    proxy_url = os.getenv('PROXY_URL')
    if proxy_url:
      print("Using PROXY_URL environment variable as fallback.")
else:
    print("Constructed proxy URL from components.")

async def test_proxy():
    print("Testing proxy connection...")

    if not proxy_url:
        print("Proxy settings not found in environment variables (PROXY_HOST, PROXY_PORT, PROXY_USERNAME, PROXY_PASSWORD, or PROXY_URL).")
        return False

    print(f"Proxy URL being used: {proxy_url}")

    try:
        async with httpx.AsyncClient(
            proxies={
                "http://": proxy_url,
                "https://": proxy_url
            },
            timeout=30.0,
            verify=False
        ) as client:
            print("Attempting to connect to test API...")
            # Test connection to a simple API
            response = await client.get("https://api.ipify.org?format=json")
            print(f"Response status: {response.status_code}")
            print(f"Your IP through proxy: {response.json()['ip']}")
            return True
    except httpx.ProxyError as e:
        print(f"Proxy Error: {str(e)}")
        print("This usually means the proxy server is not responding or the credentials are incorrect.")
        print("Full error details:")
        print(traceback.format_exc())
        return False
    except httpx.ConnectTimeout as e:
        print(f"Connection Timeout: {str(e)}")
        print("The proxy server took too long to respond.")
        print("Full error details:")
        print(traceback.format_exc())
        return False
    except httpx.RequestError as e:
        print(f"Request Error: {str(e)}")
        print("There was an error making the request through the proxy.")
        print("It's possible the issue is with the proxy, the target server, or the request itself.")
        print("Full error details:")
        print(traceback.format_exc())
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print("Full error details:")
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_proxy())