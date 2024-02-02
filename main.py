from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student
import os
from train import Train
from face_recognition import FaceRecognition
from attendance import attendance
from Devloper import devloper
from help import Help
import tkinter

from time import strftime



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1080+0+0")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open("D:\Python\Project\image\m1.webp")
        img = img.resize((500, 130))
        self.photoimage = ImageTk.PhotoImage(img)

        l1 = Label(self.root, image=self.photoimage)
        l1.place(x=0, y=0, width=500, height=130)

        # second image
        img2 = Image.open("D:\\Python\\Project\\image\\f2.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimage2 = ImageTk.PhotoImage(img2)

        l2 = Label(self.root, image=self.photoimage2)
        l2.place(x=500, y=0, width=500, height=130)

        # third image
        img3 = Image.open("D:\\Python\\Project\\image\\college3.jpg")
        img3 = img3.resize((500, 130))
        self.photoimage3 = ImageTk.PhotoImage(img3)

        l3 = Label(self.root, image=self.photoimage3)
        l3.place(x=1000, y=0, width=550, height=130)

        # background image
        img4 = Image.open("D:\\Python\\Project\\image\\bggg.jpg")
        img4 = img4.resize((1550, 710))
        self.photoimage4 = ImageTk.PhotoImage(img4)

        bg = Label(self.root, image=self.photoimage4)
        bg.place(x=0, y=130, width=1530, height=710)

        t1 = Label(bg, text="Face Recognition System(Attendance Software)", font=("times new roman", 35, "bold"),
                   bg="white", fg="red")
        t1.place(x=0, y=0, width=1530, height=55)


            # Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(t1,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        

        # Student Button
        img5 = Image.open("D:\Python\Project\image\student.jpg")
        img5 = img5.resize((220, 220))
        self.photoimage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg, image=self.photoimage5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg, text="Student Details", command=self.student_details, cursor="hand2", font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b1_1.place(x=200, y=300, width=220, height=40)

        # face detectore Button
        img6 = Image.open("D:\Python\Project\image\detection.jpg")
        img6 = img6.resize((220, 220))
        self.photoimage6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg, image=self.photoimage6, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)

        b2_2 = Button(bg, text="Face Detection", cursor="hand2",command=self.face_data, font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b2_2.place(x=500, y=300, width=220, height=40)

         #Attendances Button
        img7 = Image.open("D:\\Python\\Project\\image\\atte.jpg")
        img7 = img7.resize((220, 220))
        self.photoimage7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg, image=self.photoimage7, cursor="hand2",command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)

        b3_3 = Button(bg, text="Attendances",command=self.attendance_data, cursor="hand2", font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b3_3.place(x=800, y=300, width=220, height=40)


        #Help Desk Button
        img8 = Image.open("D:\\Python\\Project\\image\\help.jpg")
        img8 = img8.resize((220, 220))
        self.photoimage8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg, image=self.photoimage8, cursor="hand2",command=self.help_data)
        b4.place(x=1100, y=100, width=220, height=220)

        b4_4 = Button(bg, text="Help Desk",command=self.help_data, cursor="hand2", font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b4_4.place(x=1100, y=300, width=220, height=40)

        # train image
        img9 = Image.open("D:\\Python\\Project\\image\\trainn.jpg")
        img9 = img9.resize((220, 220))
        self.photoimage9 = ImageTk.PhotoImage(img9)

        b5= Button(bg, image=self.photoimage9, cursor="hand2",command=self.train_details)
        b5.place(x=200, y=400, width=220, height=220)

        b5_5 = Button(bg, text="Train", cursor="hand2",command=self.train_details, font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b5_5.place(x=200, y=600, width=220, height=40)


        #photos Button
        img10 = Image.open("D:\Python\Project\image\photos.jpeg")
        img10 = img10.resize((220, 220))
        self.photoimage10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg, image=self.photoimage10, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=400, width=220, height=220)

        b6_6 = Button(bg, text="Photo", cursor="hand2",command=self.open_img, font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b6_6.place(x=500, y=600, width=220, height=40)


         #Devloper logo
        img11 = Image.open("D:\Python\Project\image\devlo.png")
        img11 = img11.resize((220, 220))
        self.photoimage11 = ImageTk.PhotoImage(img11)

        b7 = Button(bg, image=self.photoimage11, cursor="hand2",command=self.Devloper_data)
        b7.place(x=800, y=400, width=220, height=220)

        b7_7 = Button(bg, text="Devloper", cursor="hand2", command=self.Devloper_data,font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b7_7.place(x=800, y=600, width=220, height=40)


         #Exit Button
        img12 = Image.open("D:\\Python\\Project\\image\\exit.jpg")
        img12 = img12.resize((220, 220))
        self.photoimage12 = ImageTk.PhotoImage(img12)

        b8 = Button(bg, image=self.photoimage12, cursor="hand2",command=self.iexit)
        b8.place(x=1100, y=400, width=220, height=220)

        b8_8 = Button(bg, text="Exit", command=self.iexit,cursor="hand2", font=("Raleway", 15, "bold"), bg="white",
                      fg="dark blue")
        b8_8.place(x=1100, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("data")
    
    def iexit(self):
        self.iexit = tkinter.messagebox.askyesno("face", "Are You Sure Exit From Project", parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return




        # ========Function Button=========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)
    

    def train_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = attendance(self.new_window)

    def Devloper_data(self):
        self.new_window = Toplevel(self.root)
        self.app = devloper(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
        
        



        

        

        


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
