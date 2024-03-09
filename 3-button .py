from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

def sub():
    # myfont=Font(family='times',size=20,weight='bold')
    # lab=Label(text="sumitted",fg='green',font=myfont)
    # lab.pack()
    messagebox.showinfo(title='meswsage',message='submitted')

def clr():
    # myfont=Font(family='times',size=20,weight='bold')
    # lab=Label(text="cleared",fg='red',font=myfont)
    # lab.pack()
      messagebox.showinfo(title='meswsage',message='cleared')


window=Tk()


window.geometry('500x500')
window.title("GUI")
myfont=Font(family='times',size=20,weight='bold')
sub=Button(text="submit",bg='green',fg='aqua',font=myfont,activebackground="green",activeforeground='white',command=sub)
sub.pack()
clr=Button(text="clear",bg='red',fg='aqua',font=myfont,activebackground="red",activeforeground='white',command=clr)
clr.pack()


window.mainloop()