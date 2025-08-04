import cv2

from Modules_EstimateImgQuality.normalize_data import normalize_data


def estimate(img):
    """
    :img is any raw image
        - take an image
        - check laplacian
        - normalize result (0.009 is coefficient of normalizing)
        - check for add formatting number
        - create date
        - min_value and max_value are normal range for noise
    :return - % of Sharpness and formatting number for sheets
    """
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    raw_data = laplacian.var()
    min_value = 100
    max_value = 1000
    # print(raw_data)

    data = normalize_data(raw_data, (min_value + max_value) / 2, 0.009)
    # print(data)
    formatting_coefficient = int
    if data > 95:
        formatting_coefficient = 4
    elif 40 < data <= 95:
        formatting_coefficient = 4
    elif 5 <= data <= 40:
        formatting_coefficient = 3
    elif data < 5:
        formatting_coefficient = 2

    result = [f"{data:.2f}", formatting_coefficient]
    # print(result)

    return result


# raw_image = cv2.imread(str(""))
# estimate(raw_image)

