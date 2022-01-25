from typing import List
import cv2
import numpy as np

from cvutils.shapes import Shape

COLORS = {
    'random': lambda : list(np.random.random(size=3) * 256),
    'red' : lambda : (255, 0, 0),
    'green' : lambda : (0, 255, 0),
    'blue' : lambda : (0, 0, 255)
}

def add_shapes(img:np.ndarray, shapes:List[Shape], colors='random') -> np.ndarray:
    """Add cv2 shapes to an image"""
    assert colors in COLORS, 'This color is not available'
    img_copy = img.copy()
    if len(img.shape) == 2:
        img_copy = cv2.cvtColor(img_copy, cv2.COLOR_GRAY2RGB)
    for shape in shapes:
        color = COLORS[colors]()
        shape.add_cv2_shape(img_copy, color)
    return img_copy
