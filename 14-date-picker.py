from tkcalendar import *
from tkinter import *
from tkinter import messagebox

def datepicker():
    def datemessage():
        mycal=cal.get_date()
        messagebox.showinfo("CALANDER",mycal)
        
    top=Toplevel(window)
    top.title("CALENDAR")
    top.geometry("500x500")
    cal=Calendar(top,Selectmode="day",year=2023,day=11,month=7,cursor="hand1",
                 date_pattern="dd/mm/yyyy")
    cal.pack(fill=BOTH,expand=True)
    btnsubmit=Button(top,text="SUBMIT",command=datemessage,fg="red",bg="aqua")
    btnsubmit.pack(pady=19)






 


window=Tk()

w=500
h=500

sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()

x=(sw/2)-(w/2)
y=(sh/2)-(h/2)

window.geometry("%dx%d+%d+%d" %(w,h,x,y))


btncal=Button(window,text="calender",fg="grey",bg="green",activebackground="red",activeforeground="aqua",padx=20,pady=20,font=("times",30,"bold"),command=datepicker)
btncal.pack(pady=30)



window.mainloop()