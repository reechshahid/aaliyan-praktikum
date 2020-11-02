from tkinter import *
from tkinter import ttk


root1 = Tk()
root1.title("Test1")
root1.background("black")
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

button1 = Button(root1, bg="gray", fg="black", command=button1Press)
button1.place(x=5, y=5, width=290, height=45)

button2 = Button(root1, bg="gray", fg="black", command=button2Press)
button2.place(x=305, y=5, width=290, height=45)

button3 = Button(root1,bg="gray", fg="black", command=button3Press)
button3.place(x=605, y=5, width=290, height=45)

button4 = Button(root1, bg="gray", fg="black", command=button4Press)
button4.place(x=5, y=60, width=290, height=45)

button5 = Button(root1, bg="gray", fg="black", command=button5Press)
button5.place(x=305, y=60, width=290, height=45)

button6 = Button(root1,bg="gray", fg="black", command=button6Press)
button6.place(x=605, y=60, width=290, height=45)

button7 = Button(root1, bg="gray", fg="black", command=button7Press)
button7.place(x=5, y=115, width=290, height=45)

button8 = Button(root1, bg="gray", fg="black", command=button8Press)
button8.place(x=305, y=115, width=290, height=45)

button9 = Button(root1, bg="gray", fg="black", command=button9Press)
button9.place(x=605, y=115, width=290, height=45)


root1.mainloop()


