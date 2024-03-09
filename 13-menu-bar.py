from tkinter import *

def new():
    file=Toplevel(window)
    file.title("new")
    lb=Label(file,text="hello")
    lb.pack()




window=Tk()

menubar=Menu(window)

filemenu=Menu(menubar,tearoff=0) 

filemenu.add_command(label="NEW",command=new)
filemenu.add_command(label="SAVE")
filemenu.add_command(label="SAVE AS")
filemenu.add_command(label="EXIT")

menubar.add_cascade(label="FILE",menu=filemenu)
window.config(menu=menubar)


editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="NEW",command=new)
editmenu.add_command(label="SAVE")
editmenu.add_command(label="SAVE AS")
editmenu.add_command(label="EXIT",command=window.destroy)
menubar.add_cascade(label="EDIT",menu=editmenu)









window.mainloop()


