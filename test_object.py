from object_detector import detect_objects

objects = detect_objects("sample_images/test.jpeg")

print("\nDetected Objects")
print("====================")

for obj in objects:
    print(obj["object"], obj["confidence"])
