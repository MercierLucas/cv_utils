import cv2
from .shape import Shape

class Point(Shape):
    def __init__(self, pos, label=None) -> None:
        """Args:
            Pos: [x, y]
        """
        super().__init__(label=label)
        self.x = int(pos[0])
        self.y = int(pos[1])


    @property
    def center(self):
        return self.x, self.y


    @property
    def label_pos(self):
        return self.x - 10, self.y - 10


    def add_cv2_shape(self, img, color=(255, 0, 0)):
        cv2.circle(img, self.center, 0, color, thickness=-1)
        if self.label:
            cv2.putText(img, self.label, self.label_pos, cv2.FONT_HERSHEY_SIMPLEX,.5, color, 1, 2)


    