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
root.title("Test1")
root.geometry("950x250")
root.title ("demo1")
root.configure(background="black")


menubar = Menu(root)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Speichern", command=save)
filemenu.add_command(label="Speichern unter", command=save2)
filemenu.add_separator()
filemenu.add_command(label="programm beenden", command=shutdown)
menubar.add_cascade(label="Datei", menu=filemenu)

zaehler = 0


def zaehler_erhoehen():
    global zaehler
    zaehler = zaehler + 1 


def button2():
    ("test")
def ButtonPress():
    ("button")
def button1Press():
    global button1
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button1['text'] = "X"
    else: 
        print('gerade')
        button1['text'] = "O"
        print('gerade')
    button1["state"] == "normal"
    button1["state"] = "disabled"
def button2Press(): 
    global button2
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button2['text'] = "X"
    else: 
        print('gerade')
        button2['text'] = "O"
        print('gerade')
    button2["state"] == "normal"
    button2["state"] = "disabled"  
def button3Press():
    global button3
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button3['text'] = "X"
    else: 
        print('gerade')
        button3['text'] = "O"
        print('gerade')
    button3["state"] == "normal"
    button3["state"] = "disabled"
def button4Press():
    global button4
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button4['text'] = "X"
    else: 
        print('gerade')
        button4['text'] = "O"
        print('gerade')
    button4["state"] == "normal"
    button4["state"] = "disabled"
def button5Press():
    global button5
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button5['text'] = "X"
    else: 
        print('gerade')
        button5['text'] = "O"
        print('gerade')
    button5["state"] == "normal"
    button5["state"] = "disabled"
def button6Press():
    global button6
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button6['text'] = "X"
    else: 
        print('gerade')
        button6['text'] = "O"
        print('gerade')
    button6["state"] == "normal"
    button6["state"] = "disabled"
def button7Press():
    global button7
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button7['text'] = "X"
    else: 
        print('gerade')
        button7['text'] = "O"
        print('gerade')
    button7["state"] == "normal"
    button7["state"] = "disabled"
def button8Press():
    global button8
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button8['text'] = "X"
    else: 
        print('gerade')
        button8['text'] = "O"
        print('gerade')
    button8["state"] == "normal"
    button8["state"] = "disabled"
def button9Press():
    global button9
    zaehler_erhoehen()
    if zaehler % 2:
        print ('ungerade')
        button9['text'] = "X"
      
    else: 
        print('gerade')
        button9['text'] = "O"
        print('gerade')
    button9["state"] == "normal"
    button9["state"] = "disabled"

def leave_buttonpress():
    global leave_button
    Text = ("leave")
    print("leave")
    root.destroy()


    

button1 = Button(root, command=button1Press)
button1.place(x=5, y=5, width=290, height=45)

button2 = Button(root, command=button2Press)
button2.place(x=305, y=5, width=290, height=45)

button3 = Button(root, command=button3Press)
button3.place(x=605, y=5, width=290, height=45)

button4 = Button(root, command=button4Press)
button4.place(x=5, y=60, width=290, height=45)

button5 = Button(root, command=button5Press)
button5.place(x=305, y=60, width=290, height=45)

button6 = Button(root, command=button6Press)
button6.place(x=605, y=60, width=290, height=45)

button7 = Button(root, command=button7Press)
button7.place(x=5, y=115, width=290, height=45)

button8 = Button(root, command=button8Press)
button8.place(x=305, y=115, width=290, height=45)

button9 = Button(root, command=button9Press)
button9.place(x=605, y=115, width=290, height=45)

leave_button= Button(root, command=leave_buttonpress)
leave_button.place(x=805, y=200, width=90, height=30)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=undo)
filemenu.add_separator()
filemenu.add_separator()
editmenu.add_command(label="Spiel Neustarten")
menubar.add_cascade(label="Bearbeiten", menu=editmenu)

root.config(menu=menubar)


root.mainloop()