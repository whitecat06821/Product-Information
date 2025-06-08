import requests
import time
import json
from pathlib import Path
import base64

def test_api():
    url = "http://localhost:5000/api/generate"

    # Test image path - replace with your test image
    test_image_path = Path("test_image.jpg")
    if not test_image_path.exists():
        print("Please place a test image named 'test_image.jpg' in the backend directory")
        return

    # Test data
    files = {
        'file': ('test_image.jpg', open(test_image_path, 'rb'), 'image/jpeg')
    }
    data = {
        'prompt': 'Describe this product in detail',
        'tone': 'professional',
        'language': 'English'
    }

    print("Testing API with single request...")
    try:
        response = requests.post(url, files=files, data=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {str(e)}")

    print("\nTesting rate limiting with multiple requests...")
    # Close and reopen the file for each request to avoid file handle issues
    for i in range(3):
        print(f"\nRequest {i+1}:")
        try:
            # Reopen the file for each request
            with open(test_image_path, 'rb') as img_file:
                files = {
                    'file': ('test_image.jpg', img_file, 'image/jpeg')
                }
                response = requests.post(url, files=files, data=data)
                print(f"Status Code: {response.status_code}")
                print(f"Response: {json.dumps(response.json(), indent=2)}")

                # If we hit rate limit, wait longer
                if response.status_code == 429:
                    retry_after = response.json().get('retry_after', 'Please try again in a few minutes')
                    print(f"\nRate limit hit. {retry_after}")
                    time.sleep(30)  # Wait 30 seconds before next request
                else:
                    time.sleep(5)  # Normal delay between requests

        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(5)  # Wait before next request even if there's an error

def analyze_response(response_data):
    """Analyze the response data and print key information"""
    if 'result' in response_data:
        result = response_data['result']
        print("\nAnalysis of successful response:")
        print(f"Title: {result.get('title', 'N/A')}")
        print(f"Colors: {', '.join(result.get('colors', []))}")
        print(f"Number of tags: {len(result.get('tags', []))}")
        print(f"Description length: {len(result.get('description', ''))} characters")
    elif 'error' in response_data:
        print("\nAnalysis of error response:")
        print(f"Error type: {response_data.get('error', 'Unknown error')}")
        print(f"Message: {response_data.get('message', 'No message provided')}")
        if 'retry_after' in response_data:
            print(f"Retry suggestion: {response_data['retry_after']}")

if __name__ == "__main__":
    test_api()