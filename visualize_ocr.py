import cv2
import numpy as np

from text_detector import extract_text

IMAGE_PATH = "sample_images/test.jpeg"

image = cv2.imread(IMAGE_PATH)

results = extract_text(IMAGE_PATH)

for item in results:

    text = item["text"]
    bbox = item["bbox"]

    # Convert bbox to integer numpy array
    pts = np.array(bbox, dtype=np.int32)

    # Draw bounding box
    cv2.polylines(image, [pts], True, (0, 255, 0), 2)

    # Draw text above box
    x = int(pts[0][0])
    y = int(pts[0][1]) - 10

    cv2.putText(
        image,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

cv2.imwrite("outputs/ocr_result.jpg", image)

print("Image saved as outputs/ocr_result.jpg")
