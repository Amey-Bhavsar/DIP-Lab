import numpy as np

def global_thresholding(img, threshold):
    output = np.where(img >= threshold, 255, 0)
    return output.astype(np.uint8)