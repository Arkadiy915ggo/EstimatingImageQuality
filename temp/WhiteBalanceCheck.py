from skimage import io, color
import numpy as np

def analyze_white_balance(image_path):
    img = io.imread("F:/photo/Exorts/forStock/Stock-97.JPG")

    if img.ndim == 2 or img.shape[2] == 1:
        return "Gray image"

    lab = color.rgb2lab(img / 255.0)
    a_mean = lab[:, :, 1].mean()
    b_mean = lab[:, :, 2].mean()


    deviation = np.sqrt(a_mean**2 + b_mean**2)

    return {
        "a*": round(a_mean, 2),
        "b*": round(b_mean, 2),
        "deviation": round(deviation, 2),
        "status": status
    }


result = analyze_white_balance("your_image.jpg")
print("White balance deviation (a*, b*):", result["a*"], result["b*"])
print("General:", result["deviation"])
print("Review:", result["status"])