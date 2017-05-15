from PIL import Image as PImage

class Image:
    def open(self, path):
        self.image = PImage.open(path)
        self.originalPath = path

    def save(self):
        self.image.save(self.originalPath)

    def saveAs(self, path):
        self.image.save(path)
