import cv2
import numpy as np

class Transform:
    """Work in progress"""
    def grayscale(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    def canny(img):
        return cv2.Canny(img, 0, 100)


    def opening(img):
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))


    def otsu(img):
        return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


    def apply(img, transforms):
        for transform in transforms:
            img = transform(img)
        return img