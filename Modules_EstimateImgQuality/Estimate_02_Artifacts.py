import cv2
import numpy as np

def estimate(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray_image.shape
    blocks = []
    for y in range(0, h - 8, 8):
        for x in range(0, w - 8, 8):
            block = gray_image[y:y+8, x:x+8]
            blocks.append(np.var(block))
    data = f"{np.mean(blocks):.4f}"

    # print(data)

    return data


# raw_image = cv2.imread(str(""))
# estimate(raw_image)
