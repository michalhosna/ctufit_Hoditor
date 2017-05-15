
from tkinter import Frame, BOTH, Menu, filedialog

from Image import Image

class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
        self.ImageProcessor = Image()

    def initUI(self):

        self.parent.title("Hoditor")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Save", command=self.onSave)  #TODO
        fileMenu.add_command(label="Save As", command=self.onSaveAs)  #TODO

        menubar.add_cascade(label="File", menu=fileMenu)

        effectsMenu = Menu(self.parent)
        effectsMenu.add_command(label="Rotate CW") #TODO
        effectsMenu.add_command(label="Rotate CCW") #TODO
        effectsMenu.add_command(label="Vertical Flip")  #TODO
        effectsMenu.add_command(label="Horizontal Flip") #TODO
        effectsMenu.add_separator()
        effectsMenu.add_command(label="Invert") #TODO
        effectsMenu.add_command(label="Greyscale") #TODO
        effectsMenu.add_command(label="Lighten") #TODO
        effectsMenu.add_command(label="Darken") #TODO
        effectsMenu.add_command(label="Find edges") #TODO
        effectsMenu.add_command(label="Sharpen") #TODO

        menubar.add_cascade(label="Effects", menu=effectsMenu)

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
            self.ImageProcessor.open(fl)
