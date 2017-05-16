#!/usr/bin/env python3

from tkinter import Tk

from MainWindow import MainWindow


def main():
    root = Tk()
    MainWindow(root)
    root.mainloop()
    try:
        root.destroy()
    except:
        pass


if __name__ == '__main__':
    main()
