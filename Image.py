from PIL import ImageOps, Image as PImage, ImageFilter
import Effects


class Image:
    def __init__(self, path):
        self.image = PImage.open(path)
        self.originalPath = path

    def save(self):
        if self.originalPath != 'init.png':
            self.image.save(self.originalPath)

    def saveAs(self, path):
        self.image.save(path)

    def rotateCW(self):
        self.image = Effects.rotateRight(self.image)
    def rotateCCW(self):
        self.image = Effects.rotateLeft(self.image)
    def verticalFlip(self):
        self.image = self.image.transpose(PImage.FLIP_TOP_BOTTOM)
    def horizontalFlip(self):
        self.image = self.image.transpose(PImage.FLIP_LEFT_RIGHT)
    def invert(self):
        self.image = Effects.invert(self.image)
    def grayscale(self):
        self.image = ImageOps.grayscale(self.image)
    def lighten(self):
        self.image = Effects.lighten(self.image)
    def darken(self):
        self.image = Effects.darken(self.image)
    def findEdges(self):
        self.image = self.image.filter(ImageFilter.FIND_EDGES)
    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
