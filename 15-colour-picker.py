from tkinter import *
from tkinter import colorchooser

def color():
    mycol=colorchooser.askcolor()[1]
    window.configure(bg=mycol)

window=Tk()
window.title("COLOR_PICKER")

w=500
h=500

sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()

x=(sw/2)-(w/2)
y=(sh/2)-(h/2)

window.geometry("%dx%d+%d+%d" %(w,h,x,y))



btncolor=Button(window,text="color picker",fg="red",bg="green",padx=10,pady=20,font=("times",30,"bold"),command=color)
btncolor.pack(pady=50)


window.mainloop()
