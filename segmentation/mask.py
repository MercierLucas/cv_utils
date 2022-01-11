import cv2
from typing import List

from cv_utils.entities.box import Box


def add_mask_to_image(img, mask, x, y):
    """Paste a mask at specific position on image"""
    if y + mask.shape[0] > img.shape[0]:
        max_height = img.shape[0] - y
        mask = mask[: max_height, :]

    if x + mask.shape[1] > img.shape[1]:
        max_width = img.shape[1] - x
        mask = mask[: , :max_width]
    alpha_mask = mask / 255.0
    alpha_img = 1.0 - alpha_mask
    img[y: y + mask.shape[0], x: x + mask.shape[1]] = (alpha_mask * mask + alpha_img * img[y: y + mask.shape[0], x: x + mask.shape[1]])
    return img


def find_mask(img, mask) -> Box:
    result = cv2.matchTemplate(img, mask, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    x1, y1 = maxLoc
    x2 = x1 + mask.shape[1]
    y2 = y1 + mask.shape[0]
    return Box([x1, y1, x2, y2])


def find_masks(img, masks) -> List[Box]:
    return [find_mask(img, mask) for mask in masks]