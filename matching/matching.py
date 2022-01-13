import cv2
import math
import numpy as np
from typing import List
from cv_utils.entities import Box
from cv_utils.entities import Line
from cv_utils.misc import Slider


def _couple_exists(dict_, a, b):
    if a in dict_:
        if dict_[a] == b:
            return True
    if b in dict_:
        if dict_[b] == a:
            return True
    return False

def join_points(points, k=2):
    lines = []
    couples = {}
    for a in points:
        lines_from_a = []
        for b in points:
            if a == b or _couple_exists(couples, a, b):
                continue
            lines_from_a.append(Line(a, b))
            couples[a] = b
        lines_from_a = sorted(lines_from_a, key=lambda x: float(x.length), reverse=False)
        lines.extend(lines_from_a[:k])
    return lines
        

def get_humoments(img):
    """Compute 7 Hu moments"""
    moments = cv2.moments(img)
    huMoments = cv2.HuMoments(moments)
    for i in range(0,7):
        if huMoments[i] == 0:
            continue
        huMoments[i] = -1* math.copysign(1.0, huMoments[i]) * math.log10(abs(huMoments[i]))
    return huMoments


def compute_moments_distance(m1, m2):
    return np.linalg.norm(m1-m2)


def match_mask(img, mask, top_k=1, only_min=True, return_regions=False) -> List[Box]:
    """Sliding window to find mask in the image based on huMoments"""
    if only_min:
        top_k = 1
    mask_size_y = mask.shape[0]
    mask_size_x = mask.shape[1]
    stride = mask_size_y
    boxes = []
    min_ = 1000
    regions = []
    mask_moments = get_humoments(mask)
    for y, x, region in Slider(mask.shape, stride, img):
        #dist = cv2.matchShapes(mask, region, cv2.CONTOURS_MATCH_I2, 0)
        region_moments = get_humoments(region)
        dist = compute_moments_distance(mask_moments, region_moments)

        if dist > 9000:
            dist = 9000

        x *= stride
        y *= stride

        pos = [x, y, x  + mask_size_x, y + mask_size_y]

        if (only_min and dist < min_):
            min_ = dist
            boxes = [Box(pos, label=dist)]
            regions = [region]
        elif not(only_min):
            boxes.append(Box(pos, label=dist))

    boxes = sorted(boxes, key=lambda x: float(x.label), reverse=False)
            
    return boxes[:top_k], regions