from typing import List
import cv2
import numpy as np
from cv_utils.entities.box import Box
from cv_utils.entities.circle import Circle

def detect_circles(img, min_radius=3, max_radius=10) -> List[Circle]:
    contours = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    centers = []
    for contour in contours:
        ((x, y), radius) = cv2.minEnclosingCircle(contour)
        if min_radius < radius < max_radius:
           centers.append(Circle((x, y), radius))
    return centers


def detect_hough_circles(img, min_dist=20, param1=300, param2=9, min_radius=1, max_radius=10) -> List[Circle]:
    """ 
    Circle detection using Hough transformation.
    Args:
        min_dist = 20       # minimum distance between points
        param1 = 300        # threshold for the canny filter
        param2 = 9          # The lower the more false positive?
        min_radius = 1      # Minimum radius for circles
        max_radius = 10     # Maximum radius for circles
    """

    hough_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, minDist=min_dist, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    circles = []
    if hough_circles is not None:
        hough_circles = np.uint16(np.around(hough_circles))
        for x, y, radius in hough_circles[0,:]:
            circle = Circle((x,y), radius)
            area = Box(circle=circle).get_area(img)
            circle._label = int(area)
            circles.append(circle)

    return circles


