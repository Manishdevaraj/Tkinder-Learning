from tkinter import *
from tkinter import ttk



def start():
    progerasbar['value']+=20
    # progerasbar.start(20)
    

def stop():
    progerasbar.stop()





window=Tk()

window.title("PROGRESS_BAR")
window.geometry("500x500")

progerasbar=ttk.Progressbar(window,orient=HORIZONTAL,length=900)
progerasbar.pack(pady=50)

btnstart=Button(window,text="start",padx=10,pady=10,fg="red",bg="green",font=("times",30,"bold"),command=start)
btnstart.pack(pady=10)

btnstop=Button(window,text="stop",padx=10,pady=10,fg="aqua",bg="green",font=("times",30,"bold"),command=stop)
btnstop.pack(pady=10)

window.mainloop()