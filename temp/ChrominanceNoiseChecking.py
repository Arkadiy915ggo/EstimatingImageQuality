import cv2
import numpy as np

def check_chrominance_noise(image_path):
    img = cv2.imread("F:/photo/Exorts/forStock/Stock-97.JPG")
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    cr = ycrcb[:, :, 1]
    cb = ycrcb[:, :, 2]

    cr_noise = np.std(cr)
    cb_noise = np.std(cb)

    print(f"chrominance Cr: {cr_noise:.2f}, Cb: {cb_noise:.2f} (best: <10)")

    if cr_noise > 10 or cb_noise > 10:
        print("Noisy")


check_chrominance_noise("sample.jpg")