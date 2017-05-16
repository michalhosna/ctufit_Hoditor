
from tkinter import Frame, BOTH, Menu, filedialog, Canvas
from PIL import ImageTk

from Image import Image

class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

        self.ImageProcessor = None

    def initUI(self):

        self.parent.title("Hoditor")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_command(label="Save As", command=self.onSaveAs)

        menubar.add_cascade(label="File", menu=fileMenu)

        effectsMenu = Menu(self.parent)
        effectsMenu.add_command(label="Rotate CW", command=self.onRotateCW)
        effectsMenu.add_command(label="Rotate CCW", command=self.onRotateCCW)
        effectsMenu.add_command(label="Vertical Flip", command=self.onVerticalFlip)
        effectsMenu.add_command(label="Horizontal Flip", command=self.onHorizontalFlip)
        effectsMenu.add_separator()
        effectsMenu.add_command(label="Invert", command=self.onInvert)
        effectsMenu.add_command(label="Greyscale", command=self.onGreyscale)
        effectsMenu.add_command(label="Lighten", command=self.onLighten)
        effectsMenu.add_command(label="Darken", command=self.onDarken)
        effectsMenu.add_command(label="Find edges", command=self.onFindEdges)
        effectsMenu.add_command(label="Sharpen", command=self.onSharpen)
        effectsMenu.add_command(label="Blur", command=self.onBlur)

        menubar.add_cascade(label="Effects", menu=effectsMenu)

        self.canvas = Canvas(self.parent, width=500, height=500)
        self.canvas.pack()

    def onSave(self):
        self.ImageProcessor.save()

    def onSaveAs(self):
        ftypes = [('All files', '*')]
        title = 'Choose the output directory'
        dlg = filedialog.asksaveasfilename(filetypes=ftypes, title=title,
                                         initialfile='--this directory--')
        if dlg is None:
            return
        self.ImageProcessor.saveAs(dlg)

    def onOpen(self):

        ftypes = [('All files', '*'), ('Supported images', '*.png')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            self.ImageProcessor = Image(fl)
            tk_img = ImageTk.PhotoImage(self.ImageProcessor.image)
            self.canvas.create_image(250, 250, image=tk_img)

    def onRotateCW(self):
        self.ImageProcessor.rotateCW()
    def onRotateCCW(self):
        self.ImageProcessor.rotateCCW()
    def onVerticalFlip(self):
        self.ImageProcessor.verticalFlip()
    def onHorizontalFlip(self):
        self.ImageProcessor.horizontalFlip()
    def onInvert(self):
        self.ImageProcessor.invert()
    def onGreyscale(self):
        self.ImageProcessor.greyscale()
    def onLighten(self):
        self.ImageProcessor.lighten()
    def onDarken(self):
        self.ImageProcessor.darken()
    def onFindEdges(self):
        self.ImageProcessor.findEdges()
    def onSharpen(self):
        self.ImageProcessor.sharpen()
    def onBlur(self):
        self.ImageProcessor.blur()
