# import cv2
# from tkinter import *

# def capture():

#     cap=cv2.VideoCapture(0)
#     cap.set(3,640)
#     cap.set(4,480)

#     while True:
#         success, img=cap.read()
#         cv2.imshow("webcam",img)
#         cv2.waitKey(1)



# window=Tk()
# width=500
# height=500

# sw=window.winfo_screenwidth()
# sh=window.winfo_screenheight()

# x=(sw/2)-(width/2)
# y=(sh/2)-(height/2)

# window.geometry("%dx%d+%d+%d" %(width,height,x,y))

# btncam=Button(window,text="capture",fg="aqua",bg="green",padx=10,pady=10,command=capture)
# btncam.pack(pady=30)


# window.title("ADENTENCE SYSTEM")




# window.mainloop()





import cv2
import tkinter as tk
from PIL import Image, ImageTk

def capture():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    def update_frame():
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        window.after(10, update_frame)

    update_frame()

window = tk.Tk()
# width = 640
# height = 480

# sw = window.winfo_screenwidth()
# sh = window.winfo_screenheight()

# x = (sw/2) - (width/2)
# y = (sh/2) - (height/2)

window.geometry("500x500")

label = tk.Label(window)
label.pack()

btncam = tk.Button(window, text="Capture", fg="aqua", bg="green", padx=10, pady=10, command=capture)
btncam.pack(pady=30)

window.title("ADENTENCE SYSTEM")
window.mainloop()




