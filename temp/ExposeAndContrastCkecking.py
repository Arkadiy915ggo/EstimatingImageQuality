import cv2
import numpy as np

def check_exposure_and_contrast(image_path):
    img = cv2.imread("F:/photo/Exorts/forStock/Stock-26.JPG", cv2.IMREAD_GRAYSCALE)
    brightness = np.mean(img)
    contrast = np.std(img)

    print(f"Bright: {brightness:.2f} (okay: 80–200)")
    print(f"contrast: {contrast:.2f} (okay: >30)")

    if brightness < 60 or brightness > 220:
        print("Problem exposure")
    if contrast < 30:
        print("contrast problem")


check_exposure_and_contrast("sample.jpg")