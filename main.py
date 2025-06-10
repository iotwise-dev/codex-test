import base64
import sys


def ImageToBase64(image_path):
    """Print the base64 representation of the image at the given path."""
    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
    encoded_str = encoded_bytes.decode("utf-8")
    print(encoded_str)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
    else:
        ImageToBase64(sys.argv[1])

