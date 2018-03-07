from Tkinter import *

master = Tk()

def callback():
    print "click!"

b = Button(master, text="OK", command=callback)
b.config(relief=SUNKEN)
b.pack()

mainloop()
