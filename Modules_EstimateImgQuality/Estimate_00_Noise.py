import cv2
import numpy as np


def estimate(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    normalized_gray_image = gray_image.astype(np.float32) / 255.0
    blur = cv2.GaussianBlur(normalized_gray_image, (3, 3), 0)
    noise = normalized_gray_image - blur
    data = f"{np.std(noise):.4f}"

    return data


