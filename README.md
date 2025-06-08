# AI Image Tagging Service

An AI-powered service that generates detailed product information from images. This tool uses advanced language models to analyze product images and generate comprehensive descriptions, tags, and metadata.

## Features

- Image to product information conversion
- Customizable output format (JSON)
- Support for multiple languages
- Adjustable tone settings
- Rate limiting and error handling
- Robust API with proper error responses

## Technologies Used

### Backend
- Python 3.11+
- Flask
- Langchain
- OpenAI API
- Rate limiting implementation
- Error handling and retry mechanisms

### Frontend
- Vue.js
- Tailwind CSS
- Modern UI/UX design

## Getting Started

1. Clone the repository
2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Add your OpenAI API key to .env
   ```
4. Run the backend server:
   ```bash
   python app.py
   ```
5. Install frontend dependencies and run:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## API Endpoints

### POST /api/generate
Generates product information from an image.

**Parameters:**
- `file`: Image file (required)
- `prompt`: Custom prompt (optional)
- `tone`: Output tone (optional, default: 'professional')
- `language`: Output language (optional, default: 'English')

**Response:**
```json
{
  "result": {
    "title": "Product Title",
    "description": "Detailed product description",
    "tags": ["tag1", "tag2", ...],
    "colors": ["color1", "color2", ...]
  }
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by Ren

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
