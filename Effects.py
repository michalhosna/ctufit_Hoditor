from PIL import Image
import numpy as np

def rotateRight(image):
    return rotate(image, 3)

def rotateLeft(image):
    return rotate(image, 1)

def rotate(image, times):
    pixData = np.array(image)
    pixData = np.rot90(pixData, times)
    return Image.fromarray(pixData)

def lighten(image):
    return image.point(lambda p: p * 1.1)

def darken(image):
    return image.point(lambda p: p * 1.1)

def invert(image):
    pixData = np.array(image)
    r, g, b = pixData[:, :, 0], pixData[:, :, 1], pixData[:, :, 2]
    pixData[:, :, 0] = 255 - r
    pixData[:, :, 1] = 255 - g
    pixData[:, :, 2] = 255 - b
    return Image.fromarray(pixData)
