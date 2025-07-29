import cv2
import numpy as np

def detect_moire(image_path):
    img = cv2.imread("F:/photo/Exorts/forStock/Stock-97.JPG", cv2.IMREAD_GRAYSCALE)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude = 20 * np.log(np.abs(fshift) + 1)

    strong_freqs = np.sum(magnitude > np.percentile(magnitude, 99.5))

    print(f": {strong_freqs}")

    if strong_freqs > 50:
        print("moire")


detect_moire("sample.jpg")