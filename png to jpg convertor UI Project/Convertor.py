from tkinter import *
from tkinter import filedialog as fd
from PIL import Image

root = Tk()  # create parent window
root.title("Convertor")
root.geometry('200x150')
root.configure(bg='#2c3e50')
root.resizable(False,False)



def buttonFunc():
    global filename
    filename = fd.askopenfilename(title= "Select a File")
    im1 = Image.open(filename)
    im1.save('new_pic.jpg')
    return im1


l = Label(root, text = "PNG2JPG")
l.config(bg= '#e74c3c',font=("Courier", 35))

l.pack()

# use Button and Label widgets to create a simple TV remote
try:
    turn_on = Button(root, text="Upload", command = buttonFunc,bg='#e74c3c',font=("Courier", 25))
    turn_on.place(x=26, y=70).pack()
    turn_on.pack()
except:
    x = 0


root.mainloop()
