from tkinter import *


def clr():
    name.delete(0,END)

window=Tk()
window.geometry("500x500")
window.title("hell")
name=Entry(window,fg="aquamarine")
name.pack()

rt=Button(window,text="clear",command=clr,bg="red",fg='green')
rt.pack()



window.mainloop()