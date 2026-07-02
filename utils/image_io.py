import cv2
import numpy as np

def load_image(path, grayscale=True):
    if grayscale:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if img is None:
        raise FileNotFoundError(f"Could not load image at path: {path}")
    return img

def save_image(path, img):
    if img.ndim == 3 :
        img_to_save = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    else : 
        img_to_save = img

    success = cv2.imwrite(path, img_to_save)

    if not success:
        raise IOError(f"Failed to save image at path : {path}")

