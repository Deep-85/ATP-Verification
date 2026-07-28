import os
import cv2
from text_detector import extract_text

INPUT_FOLDER = "sample_images"
OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):

    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(INPUT_FOLDER, filename)

    print("=" * 60)
    print("Processing:", filename)

    image = cv2.imread(image_path)

    detections = extract_text(image_path)

    for detection in detections:

        bbox = detection["bbox"]
        text = detection["text"]
        confidence = detection["confidence"]

        pts = []

        for point in bbox:
            pts.append((int(point[0]), int(point[1])))

        for i in range(4):
            cv2.line(image,
                     pts[i],
                     pts[(i + 1) % 4],
                     (0,255,0),
                     2)

        cv2.putText(
            image,
            text,
            (pts[0][0], pts[0][1]-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )

        print(f"{text:30} {confidence}")

    output_name = os.path.splitext(filename)[0] + "_ocr.jpg"

    cv2.imwrite(
        os.path.join(OUTPUT_FOLDER, output_name),
        image
    )

print("\nDone!")
