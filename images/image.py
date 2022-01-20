import cv2
import numpy as np

class Image:
    """Hold basic image transformation"""
    def __init__(self, path:str, name=''):
        self.image = cv2.imread(path)
        if self.image is None:
            print(f'Warning: can\'t load: {path}')
        self.format = 'BGR'
        self.attributes = {}
        if name == '':
            name = path.split('.')[-2].split('/')[-1]
        self.name = name
        
        
    def _cached_attribute(self, attr_name:str, value:object) -> object:
        if attr_name in self.attributes:
            return self.attributes[attr_name]
        self.attributes[attr_name] = value
        return value
    
    
    @property
    def contours(self) -> np.ndarray:
        return self._cached_attribute('contours', cv2.Canny(self.grayscale, 0, 100))

    
    @property
    def rgb(self) -> np.ndarray:
        return self._cached_attribute('rgb', cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))

