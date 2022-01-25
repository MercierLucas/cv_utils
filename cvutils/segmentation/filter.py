from typing import List
import numpy as np

from cvutils.shapes import Box
from cvutils.shapes import Circle


def filter_by_neighbours_in_radius(circles:List[Circle], n:int, radius:float, exact_amount=False) -> List[Circle]:
    """Filter points to keep only those who have exactly or at least a certain number of neighbours based on specific radius"""
    filtered = []
    current_neighbours = 0
    radius = radius**2
    for circle_a in circles:
        for circle_b in circles:
            if circle_a == circle_b:
                continue
            r = (circle_b.x - circle_a.x)**2 + (circle_b.y - circle_a.y)**2
            if r <= radius:
                current_neighbours += 1
        if (current_neighbours >= n and exact_amount == False) or (current_neighbours == n and exact_amount):
            filtered.append(circle_a)
        current_neighbours = 0
    return filtered


def filter_by_mean_color(img:np.ndarray, circles:List[Circle], threshold=170) -> List[Circle]:
    """Filter circles to keep only those who covers an area which high pixel mean than threshold"""
    filtered = []
    for circle in circles:
        box = Box(circle=circle)
        area = box.get_region(img)
        if np.mean(area) > threshold:
            filtered.append(circle)
    return filtered