import cv2
from .point import Point

class Circle(Point):
    def __init__(self, pos, radius, label=None) -> None:
        super().__init__(pos, label=label)
        self.radius = int(radius)


    def add_cv2_shape(self, img, color):
        cv2.circle(img, self.center, self.radius, color, 2)
        if self.label:
            cv2.putText(img, self.label, self.label_pos, cv2.FONT_HERSHEY_SIMPLEX,.5, color, 1, 2)
