import cv2
import numpy as np


def detect_dominant_colors(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Cannot load image: {image_path}")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    color_ranges = {
        "Red": [
            ((0, 100, 100), (10, 255, 255)),
            ((160, 100, 100), (180, 255, 255))
        ],
        "Green": [
            ((40, 40, 40), (80, 255, 255))
        ],
        "Blue": [
            ((90, 50, 50), (130, 255, 255))
        ],
        "Yellow": [
            ((20, 100, 100), (35, 255, 255))
        ],
        "White": [
            ((0, 0, 180), (180, 40, 255))
        ],
        "Black": [
            ((0, 0, 0), (180, 255, 40))
        ]
    }

    detected = []

    total_pixels = image.shape[0] * image.shape[1]

    for color, ranges in color_ranges.items():

        pixels = 0

        for lower, upper in ranges:

            mask = cv2.inRange(
                hsv,
                np.array(lower),
                np.array(upper)
            )

            pixels += cv2.countNonZero(mask)

        percentage = (pixels / total_pixels) * 100

        if percentage > 1:
            detected.append((color, round(percentage, 2)))

    return detected
