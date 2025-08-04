import cv2
import numpy as np

from Modules_EstimateImgQuality.normalize_data import normalize_data


def estimate(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray_image.shape
    blocks = []
    for y in range(0, h - 8, 8):
        for x in range(0, w - 8, 8):
            block = gray_image[y:y+8, x:x+8]
            blocks.append(np.var(block))
    raw_data = np.mean(blocks)
    min_value = 50
    max_value = 500
    # print(raw_data)
    data = normalize_data(raw_data, (min_value + max_value) / 2, 0.01)

    sharp_blocks = [v for v in blocks if v > 200]
    sharp_ratio = len(sharp_blocks) / len(blocks)

    formatting_coefficient = int
    if data > 90:
        formatting_coefficient = 4
    elif 50 < data <= 90:
        formatting_coefficient = 4
    elif 10 <= data <= 50:
        formatting_coefficient = 3
    elif data < 10 and sharp_ratio > 0.15:
        formatting_coefficient = 2
    elif data < 10 and sharp_ratio <= 0.15:
        formatting_coefficient = 5

    result = [f"{data:.2f}", formatting_coefficient]
    # print(result)

    return result

# raw_image = cv2.imread(str(""))
# estimate(raw_image)
