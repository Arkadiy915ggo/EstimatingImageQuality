import cv2
import numpy as np
from Modules_EstimateImgQuality.normalize_data import normalize_data


def estimate(img):
    """
    :img is any raw image
        - take an image
        - convert an image to gray color
        - apply Gaussian Blur
        - subtract from gray image
        - normalize result (100 is coefficient of normalizing)
        - check for add formatting number
        - create date
        - min_value and max_value are normal range for noise
    :return - % of noise and formatting number for sheets
    """
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    normalized_gray_image = gray_image.astype(np.float32) / 255.0
    blur = cv2.GaussianBlur(normalized_gray_image, (3, 3), 0)
    noise = normalized_gray_image - blur
    min_value = 0.005
    max_value = 0.03
    raw_data = np.std(noise)
    # print(raw_data)

    data = normalize_data(raw_data,(min_value+max_value)/2, 100)
    # print(data)
    formatting_coefficient = int
    if data < 22:
        formatting_coefficient = 4
    elif  22 <= data < 45:
        formatting_coefficient = 4
    elif 45 <= data <= 78:
        formatting_coefficient = 3
    elif data > 78:
        formatting_coefficient = 2

    result = [f"{data:.2f}", formatting_coefficient]
    # print(result)

    return result

# raw_image = cv2.imread(str(""))
# estimate(raw_image)





