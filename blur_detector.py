import cv2


def detect_blur(image_path, threshold=100):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Cannot load image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    score = cv2.Laplacian(gray, cv2.CV_64F).var()

    return {
        "blur_score": round(score, 2),
        "is_blurry": score < threshold
    }
