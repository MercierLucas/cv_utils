import cv2
import numpy as np
from cv_utils.entities.circle import Circle
from cv_utils.entities.shape import Shape


class Box(Shape):

    def __init__(self, pos=None, label=None, format='xyxy', circle:Circle=None) -> None:
        """
        Args:
            pos: [x_left, y_top, x_right, y_bottom]
            label (optional): label of the box
            format (optional): not implemented yet
            circle (optional): create box from circle, override pos if not null
        """
        super().__init__(label=label)

        if pos is None:
            pos = [0]*4

        if circle:
            pos[0] = circle.x - circle.radius
            pos[1] = circle.y - circle.radius
            pos[2] = circle.x + circle.radius
            pos[3] = circle.y + circle.radius

        self.pos = pos
        self.start_x = pos[0]
        self.start_y = pos[1]
        self.end_x = pos[2]
        self.end_y = pos[3]
        self.width = abs(self.start_x - self.end_x)
        self.height = abs(self.start_y - self.end_y)


    def add_cv2_shape(self, img, color):
        cv2.rectangle(img, self.top_left, self.bottom_right, color, 1)
        if self.label:
            cv2.putText(img, self.label, self.label_pos, cv2.FONT_HERSHEY_SIMPLEX,.5, color, 1, 2)


    @property
    def top_left(self):
        return self.pos[0], self.pos[1]


    @property
    def bottom_right(self):
        return self.pos[2], self.pos[3]


    @property
    def center(self):
        return (self.pos[0] + self.pos[2]) // 2, (self.pos[1] + self.pos[3]) // 2


    @property
    def label_pos(self):
        return self.pos[0], (self.pos[1] + self.pos[3]) // 2


    def get_region(self, img):
        return img[self.start_y: self.end_y, self.start_x: self.end_x]


    def get_area(self, img):
        region = self.get_region(img)
        if region.size == 0:
            return 0
        return int(np.mean(region))