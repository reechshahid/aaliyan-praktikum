from tkinter import *
from tkinter import ttk

def save(): 
    print("saving")
def save2():
    print("speichern unter")
def shutdown():
    print("shutingdown")
def undo():
    print("undoing")
def redo():
    print("redoing")

root = Tk()
root.title("Test")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Speichern", command=save)
filemenu.add_command(label="Speichern unter", command=save2)
filemenu.add_separator()
filemenu.add_command(label="programm beenden", command=shutdown)
menubar.add_cascade(label="Datei", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Rückgängig", command=undo)
editmenu.add_separator()
editmenu.add_command(label="Wiederholen", command=redo)
menubar.add_cascade(label="Bearbeiten", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
