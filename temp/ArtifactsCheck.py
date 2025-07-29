import cv2
import numpy as np

def jpeg_artifacts_score(image_path):
    img = cv2.imread("F:/photo/Exorts/forStock/Stock-31.JPG", cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    blocks = []
    for y in range(0, h - 8, 8):
        for x in range(0, w - 8, 8):
            block = img[y:y+8, x:x+8]
            blocks.append(np.var(block))
    return np.mean(blocks)

print("JPEG artifact level:", jpeg_artifacts_score("your_image.jpg"))

