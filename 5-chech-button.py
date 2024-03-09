from tkinter import *
from tkinter import messagebox

def clr():
    ch1.deselect()
    ch2.deselect()
    ch3.deselect()


def sub():
    if(c1.get()==1):
     val=ch1.cget("text")
     messagebox.showinfo("message",val)

    if(c2.get()==1):
     val=ch2.cget("text")
     messagebox.showinfo("message",val) 
    
    if(c3.get()==1):
     val=ch3.cget("text")
     messagebox.showinfo("message",val)
    

window=Tk()
window.geometry("500x500")
window.title("Checkbox")

c1=IntVar()
c2=IntVar()
c3=IntVar()

ch1=Checkbutton(window,text="c++",fg="red",font=('times',"30","bold"),variable=c1,onvalue=1,offvalue=0)
ch2=Checkbutton(window,text="java",fg="red",font=('times',"30","bold"),variable=c2,onvalue=1,offvalue=0)
ch3=Checkbutton(window,text="python",fg="red",font=('times',"30","bold"),variable=c3,onvalue=1,offvalue=0)

ch1.pack()
ch2.pack()
ch3.pack()

subt=Button(window,text="Submit",fg="green",bg="aqua",padx="10",pady="10",command=sub)
clear=Button(window,text="clear",fg="green",bg="aqua",padx="10",pady="10",command=clr)
subt.pack()
clear.pack()




window.mainloop()
