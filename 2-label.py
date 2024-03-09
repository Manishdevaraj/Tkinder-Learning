from tkinter import *
from tkinter.font import Font
window=Tk()
window.geometry('500x500')
myfont=Font(family='times',size=20,weight='bold',slant='italic')
lab=Label(window,text="welcome to my gui",font=myfont,bg="black",fg='aqua',padx=20,pady=20)
lab.pack()
window.mainloop()


