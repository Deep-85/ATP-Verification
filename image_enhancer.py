import cv2

def enhance_image(image_path):
    """
    Reads an image and performs basic preprocessing for OCR.
    """

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray
