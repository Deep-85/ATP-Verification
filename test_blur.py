from blur_detector import detect_blur

result = detect_blur("sample_images/test.jpeg")

print("\nBlur Detection")
print("================")
print("Blur Score :", result["blur_score"])

if result["is_blurry"]:
    print("Status     : BLURRY")
else:
    print("Status     : CLEAR")
