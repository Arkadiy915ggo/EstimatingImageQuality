import cv2
import numpy as np

def check_clipping(image_path):
    img = cv2.imread("F:/photo/Exorts/forStock/Stock-30.JPG", cv2.IMREAD_GRAYSCALE)
    total = img.size
    black = np.sum(img <= 5)
    white = np.sum(img >= 250)
    return black / total * 100, white / total * 100

black_ratio, white_ratio = check_clipping("your_image.jpg")
print(f"Clipped shadows: {black_ratio:.4f}, highlights: {white_ratio:.4f}")