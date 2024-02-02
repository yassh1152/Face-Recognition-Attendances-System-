from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class devloper:
 def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1080+0+0")
        self.root.title("Face Recognition System")


        t1 = Label(self.root, text="Devloper", font=("times new roman", 35, "bold"),
                   bg="white", fg="darkblue")
        t1.place(x=0, y=0, width=1530, height=55)

        imgtop = Image.open("D:\\Python\\Project\\image\\bggg.jpg")
        imgtop = imgtop.resize((1530, 720))
        self.photoimage_top = ImageTk.PhotoImage(imgtop)

        l2 = Label(self.root, image=self.photoimage_top)
        l2.place(x=0, y=55, width=1530, height=720)
  
                #    ======Frame=======
        # f1=Frame(l2,bd=2,bg="white")
        # f1.place(x=1000,y=0,width=500,height=600)

        imgttop = Image.open("C:\\Users\\Guide\\OneDrive\\Pictures\\yash91.jpg")
        imgttop = imgttop.resize((500, 500))
        self.photoimage_ttop = ImageTk.PhotoImage(imgttop)

        l2 = Label( image=self.photoimage_ttop)
        l2.place(x=1029, y=55, width=500, height=500)
            #  Devloper Information
        dev=Label(text='Hey, My Name Is Yash',font=("times new roman",20,"bold"),bg="white")
        dev.place(x=0,y=60)

        dev=Label(text='I am Backend Devloper',font=("times new roman",20,"bold"),bg="white")
        dev.place(x=0,y=110)


        # img3 = Image.open("D:\\Python\\Project\\image\\s3.jpg")
        # img3 = img3.resize((500,400))
        # self.photoimage3 = ImageTk.PhotoImage(img3)

        # l3 = Label(f1, image=self.photoimage3)
        # l3.place(x=0, y=205, width=500, height=400)








if __name__ == "__main__":
    root = Tk()
    obj = devloper(root)
    root.mainloop() 