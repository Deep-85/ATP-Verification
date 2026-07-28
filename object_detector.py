from ultralytics import YOLO

# Load pretrained YOLOv8 model
model = YOLO("yolov8n.pt")


def detect_objects(image_path):

    results = model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            detections.append({
                "object": model.names[cls],
                "confidence": round(conf, 3)
            })

    return detections
