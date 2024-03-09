from tkinter import *


window=Tk()
window.geometry("500x500")
window.title("GRID")

labre=Label(window,text="Registeration",font=("times",30,"bold"))
labre.grid(row=1,column=2)

window.mainloop()