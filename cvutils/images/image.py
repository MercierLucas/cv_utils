import cv2
import numpy as np

class Image:
    """Hold basic image transformation"""
    def __init__(self, path:str, name=''):
        self.image = cv2.imread(path)
        if self.image is None:
            print(f'Warning: can\'t load: {path}')
        self.format = 'BGR'
        if name == '':
            name = path.split('.')[-2].split('/')[-1]
        self.name = name

    @property
    def grayscale(self) -> np.ndarray:
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


    @property
    def rgb(self) -> np.ndarray:
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

