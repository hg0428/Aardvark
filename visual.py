#Aardvark.library
from tkinter import *
from Aardvark import *


@Aardvark.function("visual")
def visual(name, title, geometry):
    global window
    window = Tk()
    window.title(title)
    window.geometry(geometry)


@Aardvark.function("label")
def label(name, text, color, back, xplace, yplace):
    global window
    lb = Label(window, text=text, fg=color, bg=back)
    lb.place(x=int(xplace), y=int(yplace))


@Aardvark.function("entry")
def entry(name, prompt, color, back, xplace, yplace):
    e = Entry(window, text=prompt, bg=back, fg=color)
    e.place(x=xplace, y=yplace)


@Aardvark.function("show")
def show(name):
    window.mainloop()


#visual("hello world", "700x700+10+20")
#label('hello', 'black', 'white', 80, 150)
