#!/usr/bin/env python3

from tkinter import Tk
from MainWindows import MainWindow

def main():
    root = Tk()
    MainWindow(root)
    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()