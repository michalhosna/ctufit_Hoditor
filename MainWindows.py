
from tkinter import Frame, BOTH, Menu

class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Hoditor")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Save")  #TODO
        fileMenu.add_command(label="Save As")  #TODO

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


    def onOpen(self):

        ftypes = [('Supported images', '*.png'), ('All files', '*')]
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            self.readFile(fl)

    def readFile(self, filename):
        # TODO
        ...

