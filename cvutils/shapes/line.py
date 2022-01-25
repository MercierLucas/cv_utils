import cv2
import numpy as np
from .point import Point
from .shape import Shape


class Line(Shape):
    def __init__(self, point_a:Point, point_b:Point, label=None) -> None:
        super().__init__(label=label)
        self.start = point_a
        self.end = point_b
        self.length = np.sqrt(
            (self.start.x - self.end.x) ** 2 +
            (self.start.y - self.end.y) ** 2
        )

        if label is None:
            self._label = self.length

    @property
    def label_pos(self):
        return (self.start.x + self.end.x) // 2, (self.start.y + self.end.y) // 2 


    def add_cv2_shape(self, img, color):
        cv2.line(img, self.start.center, self.end.center, color, 2)
        if self.label:
            cv2.putText(img, self.label, self.label_pos, cv2.FONT_HERSHEY_SIMPLEX,.5, color, 1, 2)
