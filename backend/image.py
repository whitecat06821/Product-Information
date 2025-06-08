import base64

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def load_image(inputs: dict) -> dict:
    """Load image from bytes and convert to base64."""
    image_bytes = inputs["image_path"]
    base64_image = base64.b64encode(image_bytes).decode('utf-8')
    return {"image": base64_image}