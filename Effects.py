from collections import namedtuple
from math import floor

import numpy as np
from PIL import Image, ImageDraw

filterTuple = namedtuple('filterName', ['name', 'factor', 'bias', 'filter'])


def rotateRight(image):
    return rotate(image, 3)


def rotateLeft(image):
    return rotate(image, 1)


def rotate(image, times):
    pixData = np.array(image)
    pixData = np.rot90(pixData, times)
    return Image.fromarray(pixData)


def lighten(image):
    return image.point(lambda p: p * 1.2)


def darken(image):
    return image.point(lambda p: p * 0.8)


def invert(image):
    pixData = np.array(image)
    r, g, b = pixData[:, :, 0], pixData[:, :, 1], pixData[:, :, 2]
    pixData[:, :, 0] = 255 - r
    pixData[:, :, 1] = 255 - g
    pixData[:, :, 2] = 255 - b
    return Image.fromarray(pixData)


def grayScale(image):
    pixData = np.array(image)
    r, g, b = pixData[:, :, 0], pixData[:, :, 1], pixData[:, :, 2]
    m = 0.21 * r + 0.72 * g + 0.07 * b
    pixData[:, :, 0], pixData[:, :, 1], pixData[:, :, 2] = m, m, m
    pixData = np.clip(pixData[:, :, :], 0, 255)
    return Image.fromarray(pixData.astype('uint8'))


def flipHorizontal(image):
    pixData = np.array(image)
    pixData = np.fliplr(pixData)
    return Image.fromarray(pixData)


def flipVertical(image):
    pixData = np.array(image)
    pixData = np.flipud(pixData)
    return Image.fromarray(pixData)


def blur(image):
    return applyMatrixFilter(image, filterTuple('blur', 1.0 / 13.0, 0.0, [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ]))


def sharpen(image):
    return applyMatrixFilter(image, filterTuple('sharpen', 1.0, 0.0, [
        [1, 1, 1],
        [1, -7, 1],
        [1, 1, 1]
    ]))


def edgeDetection(image):
    return applyMatrixFilter(image, filterTuple("Find Edges", 1.0, 0.0, [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ]))


def applyMatrixFilter(image, filter_matrix):
    w, h, pData = image.size[0], image.size[1], image.load()
    resultImage = Image.new('RGB', [w, h], (255, 255, 255))
    drawField = ImageDraw.Draw(resultImage)
    for x in range(w):
        for y in range(h):
            r, g, b = 0.0, 0.0, 0.0

            for fy in range(len(filter_matrix.filter)):
                for fx in range(len(filter_matrix.filter[0])):
                    im_x = (x - len(filter_matrix.filter[0]) / 2 + fx + w) % w
                    im_y = (y - len(filter_matrix.filter) / 2 + fy + h) % h

                    r += pData[im_x, im_y][0] * filter_matrix.filter[fy][fx]
                    g += pData[im_x, im_y][1] * filter_matrix.filter[fy][fx]
                    b += pData[im_x, im_y][2] * filter_matrix.filter[fy][fx]

            r = min(max(int(filter_matrix.factor * r + filter_matrix.bias), 0), 255)
            g = min(max(int(filter_matrix.factor * g + filter_matrix.bias), 0), 255)
            b = min(max(int(filter_matrix.factor * b + filter_matrix.bias), 0), 255)
            drawField.point((x, y), (r, g, b))
            print('Hardly working ..'
                  + str(floor((x * h + y) / (w * h) * 100)) + '%  ', end='\r')
    print('Done, suckers!       ')

    return resultImage
