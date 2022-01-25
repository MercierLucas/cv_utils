class Shape:
    def __init__(self, label=None) -> None:
        self._label = label


    def add_cv2_shape(self, img, color=(255, 0, 0)):
        raise NotImplemented


    @property
    def center(self):
        raise NotImplemented
        
    @property
    def label_pos(self):
        raise NotImplemented


    @property
    def label(self):
        if isinstance(self._label, float):
            return f'{self._label:.1f}'
        if self._label is None:
            return ''
        return str(self._label)