import easyocr
import cv2
from preprocessing import preprocess_image

# Initialize EasyOCR only once
reader = easyocr.Reader(['en'])

def extract_text(image_path):

    image = preprocess_image(image_path)

    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    results = reader.readtext(image)

    detections = []

    for (bbox, text, confidence) in results:

        text = text.strip()

        if confidence < 0.60:
            continue

        if len(text) == 0:
            continue

        detections.append({
            "text": text,
            "confidence": round(float(confidence), 3),
            "bbox": bbox
        })

    return detections
