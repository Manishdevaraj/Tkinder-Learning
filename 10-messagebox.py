# SHOW INFO
# SHOW ERROR 
# SHOW Warning
# ASK QUESTION
# ASK OK CANCEL
# ASK RETY CANCEL
# ASK YES NO
# ASK YES NO CANCEL

from tkinter import *
from tkinter import messagebox

def showinfo():
    messagebox.showinfo("message","show info")

def showerror():
    messagebox.showerror("message","show error")   


def showwarning():
    messagebox.showwarning("message","show warning") 


window=Tk()
window.geometry("500x600")
window.title("MASSAGEBOXES")

showinfo=Button(window,text="show info",font=("times",20,'bold'),padx=8,pady=8,command=showinfo)
showinfo.pack()

showerror=Button(window,text="show error",font=("times",20,'bold'),padx=8,pady=8,command=showerror)
showerror.pack()

showwarning=Button(window,text="show error",font=("times",20,'bold'),padx=8,pady=8,command=showwarning)
showwarning.pack()





window.mainloop()
