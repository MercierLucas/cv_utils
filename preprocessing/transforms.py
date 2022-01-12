from typing import List
import cv2
import numpy as np

""" Inspired by torch transforms stack """

class Transform:
    """Abstract class """
    def __init__(self) -> None:
        pass

    def apply(self, img):
        raise  NotImplementedError


class GaussianBlur(Transform):
    def __init__(self, kernel_size=15) -> None:
        assert kernel_size % 2 == 1, 'Kernel size for Gaussian must be odd'

        self.kernel_size = kernel_size

    def apply(self, img):
        return cv2.GaussianBlur(img, (self.kernel_size, self.kernel_size), 1)


class Canny(Transform):
    def __init__(self, t1=100, t2=200) -> None:
        """Threshold for hystheresis. Canny usually use Sobel filter output as input"""
        self.t1 = t1
        self.t2 = t2

    def apply(self, img):
        return cv2.Canny(img, self.t1, self.t2)


class Sobel(Transform):
    def __init__(self, kernel_size=3) -> None:
        self.kernel_size = kernel_size

    def apply(self, img):
        """From opencv doc"""
        grad_x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=self.kernel_size, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=self.kernel_size, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        return grad


class Otsu(Transform):
    """Need a bit of tweaking"""
    def __init__(self) -> None:
        pass

    def apply(self, img):
        return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


class Opening(Transform):
    def __init__(self, kernel_size=5) -> None:
        self.kernel_size = kernel_size

    def apply(self, img):
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((self.kernel_size, self.kernel_size), np.uint8))



class Compose:
    """
    Chain multiple transforms.

    Example:
        >>> transforms.Compose([
        >>>     transforms.GaussianBlur(10),
        >>>     transforms.Canny(),
        >>> ])
    
    
    (todo) Also contain pre defined common cv preprocessing like:
        >>> Canny: Gaussian blur > Sobel > Canny (Canny contains gaussian blur but you might want to increase the size)
    
    """

    def __init__(self, transforms:List[Transform]) -> None:
        for t in transforms:
            assert isinstance(t, Transform), 'If you use custom transform you still must inherit from Transform class'

        self.transforms = transforms

    def __call__(self, img) -> np.ndarray:
        for t in self.transforms:
            img = t.apply(img)
        return img