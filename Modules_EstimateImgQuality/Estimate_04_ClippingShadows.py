import cv2
import numpy as np

def estimate(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    total = gray_image.size
    black = np.sum(gray_image <= 5)
    data = f"{black / total:.4f}"

    # print(data)

    return  data

# raw_image = cv2.imread(str(""))
# estimate(raw_image)