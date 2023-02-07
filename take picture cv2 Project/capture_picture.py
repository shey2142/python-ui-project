import cv2
from tkinter import *
from PIL import Image, ImageTk


win = Tk()

win.geometry("700x350")

label = Label(win)
label.grid(row=0,column=0)

cap = cv2.VideoCapture(0)

def show_frames():
    cv2image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(20, show_frames)

show_frames()
win.mainloop()
                       


cap = cv2.VideoCapture(0)
cap.set(3,640) #width=640
cap.set(4,480) #height=480

if cap.isOpened():
    _,frame = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    if _ and frame is not None:
        cv2.imwrite('img.jpg', frame)
        cv2.imwrite(name, frame)
