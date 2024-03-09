from tkinter import *


window=Tk()
window.title("CENTER THE WINDOW")
width=500
height=500

sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()

x=(sw/2)-(width/2)
y=(sh/2)-(height/2)

window.geometry("%dx%d+%d+%d" %(width,height,x,y))
window.mainloop()