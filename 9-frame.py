from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("FRAME")

frame1=Frame(window,highlightbackground="black",highlightthickness="2",padx=10,pady=10,bg="aqua")
frame1.grid(row=1,column=2,padx=50,pady=50)

labreg=Label(frame1,text="REGISTERATION",font=('times',20,"bold"),fg="green",bg="aqua")
labreg.grid(columnspan=2)

labname=Label(frame1,text="NAME",font=('times',20,"bold"),bg="aqua")
labname.grid(row=1,column=0)

enname=Entry(frame1,font=('times',20,'bold'),bg="aqua")
enname.grid(row=1,column=1,padx=2,pady=20)


window.mainloop()