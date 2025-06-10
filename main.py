import base64

def ImageToBase64(image_path):
    """Print the base64 representation of the image at the given path."""
    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
    encoded_str = encoded_bytes.decode("utf-8")
    print(encoded_str)

ImageToBase64('./image.jpg')

