import cv2
import numpy as np


def estimate(img):

    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    cr = ycrcb[:, :, 1].astype(np.float32)
    cb = ycrcb[:, :, 2].astype(np.float32)

    cr_blur = cv2.GaussianBlur(cr, (9, 9), 0)
    cb_blur = cv2.GaussianBlur(cb, (9, 9), 0)
    cr_noise_map = np.abs(cr - cr_blur)
    cb_noise_map = np.abs(cb - cb_blur)
    cr_noise = np.mean(cr_noise_map)
    cb_noise = np.mean(cb_noise_map)

    data = f"Red:{cr_noise:.4f}, Blue:{cb_noise:.4f}"

    # print(data)

    return data


# raw_image = cv2.imread(str(""))
# estimate(raw_image)