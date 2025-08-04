import cv2
import numpy as np

from Modules_EstimateImgQuality.normalize_data import normalize_data_linear


def estimate(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contrast = np.std(gray_image)
    raw_data = contrast
    min_value = 0
    max_value = 127.5
    # print(raw_data)
    data = normalize_data_linear(raw_data, min_value, max_value)
    # print(data)
    formatting_coefficient = int
    if data < 12:
        formatting_coefficient = 2
    elif 12 <= data < 24:
        formatting_coefficient = 3
    elif 24 <= data < 40:
        formatting_coefficient = 4
    elif 40 <= data <= 63:
        formatting_coefficient = 4
    elif data > 63:
        formatting_coefficient = 5

    result = [f"{data:.2f}", formatting_coefficient]
    # print(result)

    return result



# raw_image = cv2.imread(str(""))
# estimate(raw_image)

