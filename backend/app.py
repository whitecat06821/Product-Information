from flask import Flask, jsonify, request
from flask_cors import CORS
from withLC import get_product_info, RateLimitError, ModelError, APIError
import asyncio
import nest_asyncio

# Enable nested event loops
nest_asyncio.apply()

app = Flask(__name__)
CORS(app)

@app.route("/api/generate", methods=['POST'])
def generate():
    try:
        data = request.form
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file provided'}), 400

        prompt = data.get('prompt', '')
        tone = data.get('tone', 'professional')
        language = data.get('language', 'English')

        async def process_request():
            return await get_product_info(file.stream.read(), prompt, tone, language)

        # Run the async function
        result = asyncio.run(process_request())
        return jsonify({'result': result})

    except RateLimitError as e:
        return jsonify({
            'error': 'Rate limit exceeded',
            'message': str(e),
            'retry_after': 'Please try again in a few minutes'
        }), 429
    except ModelError as e:
        return jsonify({
            'error': 'Model error',
            'message': str(e)
        }), 500
    except APIError as e:
        return jsonify({
            'error': 'API error',
            'message': str(e)
        }), 500
    except Exception as e:
        print(f"Error in generate endpoint: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': 'An unexpected error occurred'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')