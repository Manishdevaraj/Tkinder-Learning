from tkinter import *
from tkinter import ttk


window = Tk()

window.geometry("500x500")
window.title("COMBOBOX")

combo=ttk.Combobox(window,width='20',state="readonly")
combo['values']=('c','c++','java')
combo.current(0)
combo.pack()

window.mainloop()