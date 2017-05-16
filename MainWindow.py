import os.path
from tkinter import Frame, BOTH, Menu, filedialog, Label as tkLabel
from PIL import ImageTk
from Image import Image
from math import floor


def actionCall(function):
    def _actionCall(self, *args, **kwargs):
        try:
            self.parent.config(cursor="wait")
        except:
            ...
        result = function(self, *args, **kwargs)
        self.reloadImage()
        self.parent.config(cursor="")

        return result

    return _actionCall


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self, *args):

        self.parent.title("Hoditor")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen, accelerator="Ctrl + O")
        fileMenu.add_command(label="Save", command=self.onSave, accelerator="Ctrl + S")
        fileMenu.add_command(label="Save As", command=self.onSaveAs)

        menubar.add_cascade(label="File", menu=fileMenu)

        effectsMenu = Menu(self.parent)
        effectsMenu.add_command(label="Rotate CW", command=self.onRotateCW, accelerator="Ctrl + R")
        effectsMenu.add_command(label="Rotate CCW", command=self.onRotateCCW, accelerator="Ctrl + L")
        effectsMenu.add_command(label="Vertical Flip", command=self.onVerticalFlip, accelerator="Ctrl + V")
        effectsMenu.add_command(label="Horizontal Flip", command=self.onHorizontalFlip, accelerator="Ctrl + H")
        effectsMenu.add_separator()
        effectsMenu.add_command(label="Invert", command=self.onInvert, accelerator="Ctrl + I")
        effectsMenu.add_command(label="Grayscale", command=self.onGrayscale, accelerator="Ctrl + G")
        effectsMenu.add_command(label="Lighten", command=self.onLighten, accelerator="Ctrl + A")
        effectsMenu.add_command(label="Darken", command=self.onDarken, accelerator="Ctrl + B")
        effectsMenu.add_command(label="Find edges", command=self.onFindEdges, accelerator="Ctrl + E")
        effectsMenu.add_command(label="Sharpen", command=self.onSharpen, accelerator="Ctrl + C")
        effectsMenu.add_command(label="Blur", command=self.onBlur, accelerator="Ctrl + D")

        self.bind_all("<Control-o>", self.onOpen)
        self.bind_all("<Control-s>", self.onSave)

        self.bind_all("<Control-r>", self.onRotateCW)
        self.bind_all("<Control-l>", self.onRotateCCW)
        self.bind_all("<Control-v>", self.onVerticalFlip)
        self.bind_all("<Control-h>", self.onHorizontalFlip)
        self.bind_all("<Control-i>", self.onInvert)
        self.bind_all("<Control-g>", self.onGrayscale)
        self.bind_all("<Control-a>", self.onLighten)
        self.bind_all("<Control-b>", self.onDarken)
        self.bind_all("<Control-e>", self.onFindEdges)
        self.bind_all("<Control-c>", self.onSharpen)
        self.bind_all("<Control-d>", self.onBlur)

        menubar.add_cascade(label="Effects", menu=effectsMenu)

        self.parent.resizable(0, 0)

        self.ImageProcessor = Image(os.path.dirname(os.path.abspath(__file__)) + "/init.png")

        self.keepPhoto = ImageTk.PhotoImage(self.ImageProcessor.image)
        self.imageLabel = tkLabel(self, image=self.keepPhoto)
        self.imageLabel.pack()

        self.reloadImage()

    def onSave(self, *args):
        self.ImageProcessor.save()

    def onSaveAs(self, *args):
        ftypes = [('All files', '*')]
        title = 'Choose the output directory'
        dlg = filedialog.asksaveasfilename(filetypes=ftypes, title=title,
                                           initialfile='--this directory--')
        if dlg is None:
            return
        self.ImageProcessor.saveAs(dlg)

    def onOpen(self, *args):

        dlg = filedialog.Open(self)
        fl = dlg.show()

        if fl != '':
            self.ImageProcessor = Image(fl)
            self.reloadImage()

    @actionCall
    def onRotateCW(self, *args):
        self.ImageProcessor.rotateCW()

    @actionCall
    def onRotateCCW(self, *args):
        self.ImageProcessor.rotateCCW()

    @actionCall
    def onVerticalFlip(self, *args):
        self.ImageProcessor.verticalFlip()

    @actionCall
    def onHorizontalFlip(self, *args):
        self.ImageProcessor.horizontalFlip()

    @actionCall
    def onInvert(self, *args):
        self.ImageProcessor.invert()

    @actionCall
    def onGrayscale(self, *args):
        self.ImageProcessor.grayscale()

    @actionCall
    def onLighten(self, *args):
        self.ImageProcessor.lighten()

    @actionCall
    def onDarken(self, *args):
        self.ImageProcessor.darken()

    @actionCall
    def onFindEdges(self, *args):
        self.ImageProcessor.findEdges()

    @actionCall
    def onSharpen(self, *args):
        self.ImageProcessor.sharpen()

    @actionCall
    def onBlur(self, *args):
        self.ImageProcessor.blur()

    def reloadImage(self, *args):
        self.imageLabel.configure(image=None)
        image = self.ImageProcessor.image
        if image.size[0] > 800 or image.size[1] > 800:
            if image.size[0] > image.size[1]:
                image = image.resize((800, floor((800 / image.size[0]) * image.size[1])), True)
            else:
                image = image.resize((floor((800 / image.size[1]) * image.size[0]), 800), True)

        if self.ImageProcessor.originalPath.rsplit('/', 1)[1] != 'init.png':
            self.parent.title('Hoditor (' + self.ImageProcessor.originalPath.rsplit('/', 1)[1] + ': ' + str(
                self.ImageProcessor.image.size[0]) + 'x' + str(self.ImageProcessor.image.size[1]) + ')')
        self.keepPhoto = ImageTk.PhotoImage(image)
        self.parent.geometry('{}x{}'.format(self.keepPhoto.width(), self.keepPhoto.height()))
        self.imageLabel.configure(image=self.keepPhoto)
