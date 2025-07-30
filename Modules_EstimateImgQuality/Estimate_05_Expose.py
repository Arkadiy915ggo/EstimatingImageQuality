import cv2
import numpy as np

def estimate(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray_image)
    data = f"{brightness:.4f}"

    # print(data)

    return data

# raw_image = cv2.imread(str(""))
# estimate(raw_image)