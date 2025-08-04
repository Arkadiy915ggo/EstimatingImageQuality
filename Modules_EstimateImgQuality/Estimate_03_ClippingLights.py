import cv2
import numpy as np
from Modules_EstimateImgQuality.normalize_data import normalize_data


def estimate(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    total = gray_image.size
    white = np.sum(gray_image >= 250)
    raw_data = white / total
    min_value = 0.005
    max_value = 0.05
    # print(raw_data)
    data = normalize_data(raw_data, (min_value + max_value) / 2, 100)
    # print(data)
    formatting_coefficient = int
    if data < 10:
        formatting_coefficient = 4
    elif 10 <= data < 35:
        formatting_coefficient = 3
    elif 35 <= data <= 90:
        formatting_coefficient = 2
    elif data > 90:
        formatting_coefficient = 1

    result = [f"{data:.2f}", formatting_coefficient]
    # print(result)

    return result

# raw_image = cv2.imread(str(""))
# estimate(raw_image)

