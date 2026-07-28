import cv2
from image_enhancer import enhance_image

# Input image
image = enhance_image("sample_images/test.jpeg")

# Save the processed image
cv2.imwrite("outputs/enhanced_test.jpeg", image)

print("✅ Image enhancement successful!")
