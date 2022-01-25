from cvutils.images import Image
from cvutils.visualization import show_image
from cvutils.preprocessing import transforms



if __name__ == '__main__':
    image = Image('demos/peppers.jpg')
    image = transforms.Compose([
        transforms.GaussianBlur(9),
        transforms.Sobel(),
        transforms.Canny()
    ])(image.grayscale)

    show_image(image, title='Simple transforms')
