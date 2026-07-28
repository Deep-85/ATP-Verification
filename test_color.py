from color_detector import detect_dominant_colors

colors = detect_dominant_colors("sample_images/test.jpeg")

print("\nDetected Colors")
print("================")

for color, percent in colors:
    print(f"{color:<10} {percent}%")
