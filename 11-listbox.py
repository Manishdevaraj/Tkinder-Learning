from tkinter import *
from tkinter import messagebox



def lstdata(event):
    data_id=listdata.curselection()
    data=listdata.get(data_id)
    mv.set(data)

def submit():
    data=adddata.get()
    listdata.insert(END,data)

def select():
    data=adddata.get()
    messagebox.showinfo("message","you selected "+data)

def update():
    if(adddata.get()!=""):
      data_id=listdata.curselection()
      data=adddata.get()
      listdata.delete(data_id)
      listdata.insert(data_id,data)
      adddata.delete(0,END)

    else:
        messagebox.showwarning("Warning","enter the data")  








window=Tk()
window.geometry("500x500")
window.title("LISTBOX")
mv=StringVar()

adddata=Entry(window,font=("times",20,"bold"),fg="aquamarine",textvariable=mv)
adddata.pack(padx=10,pady=10)

myframe=Frame(window)
myframe.pack()

Yscrollbar=Scrollbar(myframe,orient=VERTICAL)
Xscrollbar=Scrollbar(myframe,orient=HORIZONTAL)


listdata=Listbox(myframe,width=30,height=20,yscrollcommand=Yscrollbar.set,xscrollcommand=Xscrollbar.set)

Yscrollbar.config(command=listdata.yview)

Xscrollbar.config(command=listdata.xview)
Xscrollbar.pack(side=BOTTOM,fill=X)
Yscrollbar.pack(side=RIGHT,fill=Y)

listdata.pack()



listdata.bind("<<ListboxSelect>>",lstdata)


sub=Button(window,text="submit",bg="black",fg="red",command=submit)
sub.pack()

select=Button(window,text="select",bg="black",fg="red",command=select)
select.pack()

update=Button(window,text="update",bg="black",fg="red",command=update)
update.pack()















listdata.insert(END,"c")
listdata.insert(END,"java")
listdata.insert(END,"python")

for data in range(20):
    data="programming language is the best language in the world"
    listdata.insert(END,data)

window.mainloop()
