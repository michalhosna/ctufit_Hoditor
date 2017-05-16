from PIL import Image as PImage, ImageFilter

import Effects


class Image:
    def __init__(self, path):
        self.image = PImage.open(path)
        self.originalPath = path

    def save(self):
        if self.originalPath.rsplit('/', 1)[1] != 'init.png':
            self.image.save(self.originalPath)

    def saveAs(self, path):
        self.image.save(path)

    def rotateCW(self):
        self.image = Effects.rotateRight(self.image)
    def rotateCCW(self):
        self.image = Effects.rotateLeft(self.image)
    def verticalFlip(self):
        self.image = Effects.flipVertical(self.image)
    def horizontalFlip(self):
        self.image = Effects.flipHorizontal(self.image)
    def invert(self):
        self.image = Effects.invert(self.image)
    def grayscale(self):
        self.image = Effects.grayScale(self.image)
    def lighten(self):
        self.image = Effects.lighten(self.image)
    def darken(self):
        self.image = Effects.darken(self.image)
    def findEdges(self):
        self.image = Effects.edgeDetection(self.image)
    def sharpen(self):
        self.image = Effects.sharpen(self.image)
    def blur(self):
        self.image = Effects.blur(self.image)
