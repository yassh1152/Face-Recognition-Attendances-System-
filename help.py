from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
 def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1080+0+0")
        self.root.title("Face Recognition System")


        t1 = Label(self.root, text="SUPPORT", font=("times new roman", 35, "bold"),
                   bg="white", fg="darkblue")
        t1.place(x=0, y=0, width=1530, height=55)

        imgtop = Image.open("D:\\Python\\Project\\image\\support.jpg")
        imgtop = imgtop.resize((1530, 720))
        self.photoimage_top = ImageTk.PhotoImage(imgtop)

        l2 = Label(self.root, image=self.photoimage_top)
        l2.place(x=0, y=55, width=1530, height=720)

        dev=Label(l2,text='Email:Khairnaryashk3@gmail.com',font=("times new roman",20,"bold"),bg="white")
        dev.place(x=0,y=5)





if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop() 