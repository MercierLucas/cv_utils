import cv2
from math import ceil
import matplotlib.pyplot as plt


def show_image(img, title='', to_rgb=False, size=None):
    """Show a single image"""
    if size:
        plt.figure(figsize=(size,size))
    if to_rgb:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    if title != '':
        plt.title(title)
    plt.show()
    
    
def show_images(images, labels, rows='auto', cols='auto', max_cols=4, size=None, axis=False):
    """Show images side-by-side"""

    assert len(images) == len(labels), 'Must have same number of labels and images'
    
    if size:
        plt.figure(figsize=(size,size))
    
    if rows == 'auto' and cols == 'auto':
        cols = max_cols if len(images) > max_cols else len(images)
        rows = ceil(len(labels) / cols)
        
    for i, (image, label) in enumerate(zip(images, labels)):
        plt.subplot(rows, cols, (i+1))
        if not axis:
            plt.axis('off')
        if len(image.shape) == 2:
            plt.imshow(image, cmap='gray')
        else:
            plt.imshow(image)
        plt.title(label)
    plt.show()


def show_gray_hist(gray):
    """Show grayscale histgram for an image"""
    plt.hist(gray.ravel(), 255, (0,255))
    plt.xlabel('Echelle de gris')
    plt.ylabel('Occurences')
    plt.title('Grayscale histgram')
    plt.show()