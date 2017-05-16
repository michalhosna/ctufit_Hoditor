from PIL import ImageOps, Image as PImage, ImageFilter

class Image:
    def __init__(self, path):
        self.image = PImage.open(path)
        self.originalPath = path

    def save(self):
        self.image.save(self.originalPath)

    def saveAs(self, path):
        self.image.save(path)

    def rotateCW(self):
        self.image = self.image.rotate(-90)
    def rotateCCW(self):
        self.image = self.image.rotate(90)
    def verticalFlip(self):
        self.image = self.image.transpose(PImage.FLIP_TOP_BOTTOM)
    def horizontalFlip(self):
        self.image = self.image.transpose(PImage.FLIP_LEFT_RIGHT)
    def invert(self):
        self.image = ImageOps.invert(self.image)
    def greyscale(self):
        self.image = ImageOps.grayscale(self.image)
    def lighten(self):
        self.image = self.image.point(lambda p: p * 1.1)
    def darken(self):
        self.image = self.image.point(lambda p: p * 0.9)
    def findEdges(self):
        self.image = self.image.filter(ImageFilter.FIND_EDGES)
    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
