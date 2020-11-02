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

root = Tk()
root.title("Test1")


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



root = Tk()
root.title("Test1")

root = Tk()
root.title("Test")
menubar = Menu(root)

zaehler = 0

def zaehler_erhoehen():
    global zaehler
    zaehler = zaehler + 1


def button2():
    ("test")
def ButtonPress():
    ("button")
def button1Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button1['text'] = "X"
    else: 
         print('gerade')
         button1['text'] = "O"
         print('gerade')
def button2Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button2['text'] = "X"
    else: 
         print('gerade')
         button2['text'] = "O"
         print('gerade')
def button3Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button3['text'] = "X"
    else: 
         print('gerade')
         button3['text'] = "O"
         print('gerade')
def button4Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button4['text'] = "X"
    else: 
         print('gerade')
         button4['text'] = "O"
         print('gerade')
def button5Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button5['text'] = "X"
    else: 
         print('gerade')
         button5['text'] = "O"
         print('gerade')
        
def button6Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button6['text'] = "X"
    else: 
         print('gerade')
         button6['text'] = "O"
         print('gerade')
def button7Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button7['text'] = "X"
    else: 
         print('gerade')
         button7['text'] = "O"
         print('gerade')
def button8Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')  
         button8['text'] = "X"
    else:
         print('gerade')
         button8['text'] = "O"

def button9Press():
    zaehler_erhoehen()
    if zaehler % 2:
         print ('ungerade')
         button9['text'] = "X"
    else: 
         print('gerade')
         button9['text'] = "O"

button1 = Button(root, bg="gray", fg="black", command=button1Press)
button1.place(x=5, y=5, width=290, height=45)

button2 = Button(root, bg="gray", fg="black", command=button2Press)
button2.place(x=305, y=5, width=290, height=45)

button3 = Button(root,bg="gray", fg="black", command=button3Press)
button3.place(x=605, y=5, width=290, height=45)

button4 = Button(root, bg="gray", fg="black", command=button4Press)
button4.place(x=5, y=60, width=290, height=45)

button5 = Button(root, bg="gray", fg="black", command=button5Press)
button5.place(x=305, y=60, width=290, height=45)

button6 = Button(root,bg="gray", fg="black", command=button6Press)
button6.place(x=605, y=60, width=290, height=45)

button7 = Button(root, bg="gray", fg="black", command=button7Press)
button7.place(x=5, y=115, width=290, height=45)

button8 = Button(root, bg="gray", fg="black", command=button8Press)
button8.place(x=305, y=115, width=290, height=45)

button9 = Button(root, bg="gray", fg="black", command=button9Press)
button9.place(x=605, y=115, width=290, height=45)


root.mainloop()


