from image_enhancer import enhance_image
from text_detector import extract_text
from blur_detector import detect_blur
from color_detector import detect_dominant_colors
from object_detector import detect_objects

# Image to analyze
image_path = "sample_images/tower08.jpeg"

print("=" * 60)
print("IMAGE ANALYSIS REPORT")
print("=" * 60)

print(f"\nImage : {image_path}")

# --------------------------------------------------
# 1. Image Enhancement
# --------------------------------------------------
print("\n[1] Image Enhancement")

enhance_image(image_path)

print("Done")

# --------------------------------------------------
# 2. OCR
# --------------------------------------------------
print("\n[2] OCR")

texts = extract_text(image_path)

if len(texts) == 0:
    print("No text detected")
else:
    for text in texts:
        print(text)

# --------------------------------------------------
# 3. Blur Detection
# --------------------------------------------------
print("\n[3] Blur Detection")

blur = detect_blur(image_path)

print("Score :", blur["blur_score"])

if blur["is_blurry"]:
    print("Status : BLURRY")
else:
    print("Status : CLEAR")

# --------------------------------------------------
# 4. Dominant Colors
# --------------------------------------------------
print("\n[4] Dominant Colors")

colors = detect_dominant_colors(image_path)

if len(colors) == 0:
    print("No dominant colors found")
else:
    for color, percent in colors:
        print(f"{color} : {percent}%")

# --------------------------------------------------
# 5. Object Detection
# --------------------------------------------------
print("\n[5] Object Detection")

objects = detect_objects(image_path)

if len(objects) == 0:
    print("No objects detected")
else:
    for obj in objects:
        print(f"{obj['object']} ({obj['confidence']})")

print("\n" + "=" * 60)
print("Analysis Complete")
print("=" * 60)
