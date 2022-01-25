from typing import List
import cv2
from cvutils.images import Image

class TunerParameter:
    def __init__(self, name:str, default:int, max:int) -> None:
        self.name = name
        self.default = default
        self.max = max


class Tuner:

    def __init__(self, params: List[TunerParameter], callback=None) -> None:
        self.params = params
        self.callback = callback if callback is not None else self.default_callback
        self._is_dirty = False


    def default_callback(self, x):
        """Default callback, trigger image transform computation only when called"""
        self._is_dirty = True
        pass


    def tune(self, image, method, window_name='tuner'):
        """Create a cv2 window containing sliderbars that will call the 'method' to generate a new image to display"""
        cv2.namedWindow(window_name)

        
        for param in self.params:
            cv2.createTrackbar(param.name, window_name, param.default, param.max, self.callback)

        while 1:

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

            slider_params = {param.name : cv2.getTrackbarPos(param.name, window_name) for param in self.params}

            if self._is_dirty:
                resulting_image = method(image, **slider_params)
                cv2.imshow(window_name, resulting_image)
                self._is_dirty = False

        cv2.destroyAllWindows()