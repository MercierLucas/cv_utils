

class SquareSlider2D:
    def __init__(self, field, stride, image) -> None:
        self.field = field
        self.stride = stride
        self.image = image
        self.height = image.shape[0]
        self.width = image.shape[1]

    def __iter__(self):
        for y in range(0, self.height - self.field + 1, self.stride):
            for x in range(0, self.width - self.field + 1, self.stride):
                yield y//self.stride, x//self.stride, self.image[y : y + self.field, x : x + self.field]


class Slider:
    def __init__(self, field, stride, image) -> None:
        self.field_y = field[0]
        self.field_x = field[1]
        self.stride = stride
        self.image = image
        self.height = image.shape[0]
        self.width = image.shape[1]
        
    def __iter__(self):
        for y in range(0, self.height - self.field_y + 1, self.stride):
            for x in range(0, self.width - self.field_x + 1, self.stride):
                yield y//self.stride, x//self.stride, self.image[y : y + self.field_y, x : x + self.field_x]