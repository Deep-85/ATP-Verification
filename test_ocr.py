from text_detector import extract_text

results = extract_text("sample_images/test.jpeg")

print("\nDetected OCR Results")
print("=" * 60)

for i, item in enumerate(results, start=1):

    print(f"\nDetection {i}")
    print(f"Text       : {item['text']}")
    print(f"Confidence : {item['confidence']:.3f}")
    print(f"BoundingBox: {item['bbox']}")
