from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class student:
 def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1080+0+0")
        self.root.title("Face Recognition System")

        # ================variable============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_dob=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_mail=StringVar()
        self.var_phoneNo=StringVar()
        self.var_add=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        


        # first image
        img = Image.open("D:\\Python\\Project\\image\\s2.jpeg")
        img = img.resize((500, 130))
        self.photoimage = ImageTk.PhotoImage(img)

        l1 = Label(self.root, image=self.photoimage)
        l1.place(x=0, y=0, width=500, height=130)
 
          # second image
        img2 = Image.open("D:\\Python\\Project\\image\\s1.jpg")
        img2 = img2.resize((500, 130))
        self.photoimage2 = ImageTk.PhotoImage(img2)

        l2 = Label(self.root, image=self.photoimage2)
        l2.place(x=500, y=0, width=500, height=130)

        # third image
        img3 = Image.open("D:\\Python\\Project\\image\\s3.jpg")
        img3 = img3.resize((500, 130))
        self.photoimage3 = ImageTk.PhotoImage(img3)

        l3 = Label(self.root, image=self.photoimage3)
        l3.place(x=1000, y=0, width=550, height=130)

# bg image
        img4 = Image.open("D:\Python\Project\image\Attendance.jpg")
        img4 = img4.resize((1550, 710))
        self.photoimage4 = ImageTk.PhotoImage(img4)

        bg = Label(self.root, image=self.photoimage4)
        bg.place(x=0, y=130, width=1530, height=710)

        t1 = Label(bg, text="Student Manegment System", font=("times new roman", 35, "bold"),
                   bg="white", fg="darkblue")
        t1.place(x=0, y=0, width=1530, height=55)



        f1=Frame(bg,bd=2)
        f1.place(x=0,y=60,width=1550,height=600)

        #left side label frame
        lf=LabelFrame(f1,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        lf.place(x=10,y=10,width=730,height=580)

        imglf = Image.open("D:\\Python\\Project\\image\\Attendance.jpg")
        imglf = imglf.resize((720,130))
        self.photoimageleft = ImageTk.PhotoImage(imglf)

        l2 = Label(lf, image=self.photoimageleft)
        l2.place(x=5, y=0, width=720, height=150)

          #current Course
        currentf=LabelFrame(lf,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        currentf.place(x=5,y=135,width=720,height=115)

             #department
        deptl=Label(currentf,text='Department',font=("times new roman",12,"bold"),bg="white")
        deptl.grid(row=0,column=0,padx=10)

        deptcombo=ttk.Combobox(currentf,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="read only")
        deptcombo["values"]=("Select Department","IT","Computer Application","Computer Science","Mathematics")        
        deptcombo.current(0)
        deptcombo.grid(row=0,column=1,padx=2,pady=10)

           #course
        coursel=Label(currentf,text='Courses',font=("times new roman",12,"bold"),bg="white")
        coursel.grid(row=0,column=2,padx=10)

        coursecombo=ttk.Combobox(currentf,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="read only")
        coursecombo["values"]=("Select Course","BCA","BCS","BSC(cs)","BBA(ca)")        
        coursecombo.current(0)
        coursecombo.grid(row=0,column=3,padx=2,pady=10,stick=W)
            #year
        yearl=Label(currentf,text='Year',font=("times new roman",12,"bold"),bg="white")
        yearl.grid(row=1,column=0,padx=10)

        yearcombo=ttk.Combobox(currentf,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        yearcombo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")        
        yearcombo.current(0)
        yearcombo.grid(row=1,column=1,padx=2,pady=10)

       #Semester
        seml=Label(currentf,text='Semester',font=("times new roman",12,"bold"),bg="white")
        seml.grid(row=1,column=2,padx=10,sticky=W)

        semcombo=ttk.Combobox(currentf,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        semcombo["values"]=("Select Semester","Sem-1","Sem-2")        
        semcombo.current(0)
        semcombo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

       #Student Informartion 
        studf=LabelFrame(lf,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        studf.place(x=5,y=250,width=720,height=300)
             #student id
        studid=Label(studf,text='Student ID',font=("times new roman",12,"bold"),bg="white")
        studid.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studidentry = ttk.Entry(studf,textvariable=self.var_id, width=20, font=("times new roman", 12, "bold"))
        studidentry.grid(row=0, column=1, padx=10, sticky=W)
               #student name
        studname=Label(studf,text='Student Name',font=("times new roman",12,"bold"),bg="white")
        studname.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        studnameentry = ttk.Entry(studf,textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        studnameentry.grid(row=0, column=3, padx=10,pady=5, sticky=W)

        #Class Division
        classdiv=Label(studf,text='Class Division',font=("times new roman",12,"bold"),bg="white")
        classdiv.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        divcombo=ttk.Combobox(studf,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="read only")
        divcombo["values"]=("A","B","C","D","E")        
        divcombo.current(0)
        divcombo.grid(row=1,column=1,padx=2,pady=5)

        #DOB
        dob=Label(studf,text='DOB',font=("times new roman",12,"bold"),bg="white")
        dob.grid(row=1,column=2,padx=10,pady=5,sticky=W)


        dobentry = ttk.Entry(studf,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dobentry.grid(row=1, column=3, padx=10,pady=5, sticky=W)

        

        #Roll No

        rollno=Label(studf,text='Roll No',font=("times new roman",12,"bold"),bg="white")
        rollno.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        rollnoentry = ttk.Entry(studf,textvariable=self.var_rollno, width=20, font=("times new roman", 12, "bold"))
        rollnoentry.grid(row=2, column=1, padx=10,pady=5, sticky=W)


        #Gender
        gender=Label(studf,text='Gender',font=("times new roman",12,"bold"),bg="white")
        gender.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        gendercombo=ttk.Combobox(studf,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="read only")
        gendercombo["values"]=("Male","Female","Other")        
        gendercombo.current(0)
        gendercombo.grid(row=2,column=3,padx=2,pady=5)


        
       
       #Email
        email=Label(studf,text='E-Mail',font=("times new roman",12,"bold"),bg="white")
        email.grid(row=3,column=0,padx=10,pady=5,sticky=W)


        mailentry = ttk.Entry(studf,textvariable=self.var_mail, width=20, font=("times new roman", 12, "bold"))
        mailentry.grid(row=3, column=1, padx=10,pady=5, sticky=W)
       
       #Phone no
        phoneno=Label(studf,text='Phone No',font=("times new roman",12,"bold"),bg="white")
        phoneno.grid(row=3,column=2,padx=10,pady=5,sticky=W)


        phonenoentry = ttk.Entry(studf,textvariable=self.var_phoneNo, width=20, font=("times new roman", 12, "bold"))
        phonenoentry.grid(row=3, column=3, padx=10,pady=5, sticky=W)

        #Address 
        add=Label(studf,text='Address',font=("times new roman",12,"bold"),bg="white")
        add.grid(row=4,column=0,padx=10,pady=5,sticky=W)


        addentry = ttk.Entry(studf,textvariable=self.var_add, width=20, font=("times new roman", 12, "bold"))
        addentry.grid(row=4, column=1, padx=10,pady=5, sticky=W)
       
       #Teacher Name
        teacher=Label(studf,text='Teacher Name',font=("times new roman",12,"bold"),bg="white")
        teacher.grid(row=4,column=2,padx=10,pady=5,sticky=W)


        teacherentry = ttk.Entry(studf,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacherentry.grid(row=4, column=3, padx=10,pady=5, sticky=W)

        #Radio Buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(studf, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio1.grid(row=6, column=0)

        self.var_radio2 = StringVar()
        radio2 = ttk.Radiobutton(studf, variable=self.var_radio2, text="No  Photo Sample", value="No")
        radio2.grid(row=6, column=1)


        #Button Frame
        buttonframe=Frame(studf,bd=2,relief=RIDGE,bg="white")
        buttonframe.place(x=0,y=200,width=715,height=70)
        #save button
        savebtn=Button(buttonframe,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        savebtn.grid(row=0,column=0)
           #update button
        upbtn=Button(buttonframe,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        upbtn.grid(row=0,column=1)
        #delete
        delbtn=Button(buttonframe,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delbtn.grid(row=0,column=2)
        #reset
        rebtn=Button(buttonframe,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        rebtn.grid(row=0,column=3)

        #take button
        takebtn=Button(buttonframe,command=self.generate_dataset,text="Take Photo Sample",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takebtn.grid(row=1,column=0)

        upsamplebtn=Button(buttonframe,text="Update Photo Sample",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        upsamplebtn.grid(row=1,column=1)





        
        #right side label frame
        rf=LabelFrame(f1,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        rf.place(x=780,y=10,width=660,height=580)

        imgr = Image.open("D:\\Python\\Project\\image\\attendance-management.jpg")
        imgr = imgr.resize((720, 130))
        self.photoimgr = ImageTk.PhotoImage(imgr)

        rl1 = Label(rf, image=self.photoimgr)
        rl1.place(x=5, y=0, width=720, height=130)

        # =============search system=============
        screachf=LabelFrame(rf,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        screachf.place(x=5,y=135,width=710,height=70)

        screach=Label(screachf,text='Search By',font=("times new roman",12,"bold"),bg="red",fg="white")
        screach.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        screachcombo=ttk.Combobox(screachf,font=("times new roman",12,"bold"),width=15,state="read only")
        screachcombo["values"]=("Select ","Roll No","Name","Phone No","Email id")        
        screachcombo.current(0)
        screachcombo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        screachentry = ttk.Entry(screachf, width=15, font=("times new roman", 12, "bold"))
        screachentry.grid(row=0, column=2, padx=10,pady=5, sticky=W)



        #screach
        screachsbtn=Button(screachf,text="Screach",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        screachsbtn.grid(row=0,column=3,padx=4)
        #show all
        showbtn=Button(screachf,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showbtn.grid(row=0,column=4)
   
         #    =================table frame==============
        tablef=Frame(rf,bd=2,bg="white",relief=RIDGE)
        tablef.place(x=5,y=210,width=645,height=350)
 
        scroll_x=ttk.Scrollbar(tablef,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tablef,orient=VERTICAL)

        self.studtable=ttk.Treeview(tablef,column=("Dep","Cou","year","Sem","id","name","Div","DOb","Rollno","gender","mail","phoneNo","Add","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studtable.xview)
        scroll_y.config(command=self.studtable.yview)

        self.studtable.heading("Dep",text="Department")
        self.studtable.heading("Cou",text="Course")
        self.studtable.heading("year",text="Year")
        self.studtable.heading("Sem",text="Semester")
        self.studtable.heading("id",text="Student ID")
        self.studtable.heading("name",text="Name")
        self.studtable.heading("Div",text="Division")
        self.studtable.heading("DOb",text="DOB") 
        self.studtable.heading("Rollno",text="RollNo")
        self.studtable.heading("gender",text="Gender")
        self.studtable.heading("mail",text="EMail")
        self.studtable.heading("phoneNo",text="Phone No")
        self.studtable.heading("Add",text="Address")
        self.studtable.heading("teacher",text="Teacher")
        self.studtable.heading("photo",text="Photo")
        self.studtable["show"]="headings"

        self.studtable.pack(fill=BOTH,expand=1)
        self.studtable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ==================================Function Decleration========================
 def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:

            try:
                if len(self.var_phoneNo.get()) != 10 or not self.var_phoneNo.get().isdigit():
                    messagebox.showerror("Error", "Invalid Phone Number", parent=self.root)
                    return
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="yash", database="python_project")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_dob.get(),
                        self.var_rollno.get(),
                        self.var_gender.get(),
                        self.var_mail.get(),
                        self.var_phoneNo.get(),
                        self.var_add.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student Details Inserted Successfully", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        #     ==============Fecthing Data======================
 def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="yash", database="python_project")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.studtable.delete(*self.studtable.get_children())
            for i in data:
                self.studtable.insert("", END, values=i)
            conn.commit()
        conn.close()


        # ============Get Cursor============
 def get_cursor(self, event):
    cursor_focus = self.studtable.focus()
    content = self.studtable.item(cursor_focus)
    data = content["values"]

    if data:
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_dob.set(data[7])
        self.var_rollno.set(data[8])
        self.var_gender.set(data[9])
        self.var_mail.set(data[10])
        self.var_phoneNo.set(data[11])
        self.var_add.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])



    #   ============Update button======
 def update_data(self):
    if (
        self.var_dep.get() == "Select Department"
        or self.var_course.get() == "Select Course"
        or self.var_id.get() == ""
    ):
        messagebox.showerror("Error", "All Fields are Required", parent=self.root)
    else:
        try:
            Update = messagebox.askyesno(
                "Update", "Do You Want TO Update Student Details", parent=self.root
            )
            if Update > 0:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="yash",
                        database="python_project",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        """Update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,
                        dob=%s,rollno=%s,gender=%s,mail=%s,phoneNo=%s,address=%s,teacher=%s,photo=%s 
                        where id=%s""",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_div.get(),
                            self.var_dob.get(),
                            self.var_rollno.get(),
                            self.var_gender.get(),
                            self.var_mail.get(),
                            self.var_phoneNo.get(),
                            self.var_add.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_id.get(),
                        ),
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo(
                        "Success", "Student Details Updated Successfully", parent=self.root
                    )
                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Error in update: {str(es)}", parent=self.root
                    )
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


       
#   ============Delete ===========
 def delete_data(self):
    if self.var_id.get() == "":
        messagebox.showerror("Error", "Student Id Must be Required", parent=self.root)
    else:
        try:
            delete = messagebox.askyesno(
                "Delete", "Do You Want TO Delete Student Details", parent=self.root
            )
            if delete > 0:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="yash",
                        database="python_project",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "DELETE FROM student WHERE id=%s", (self.var_id.get(),)
                    )
                except Exception as es:
                    print(es)
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_data()  # Corrected this line
            conn.close()
            messagebox.showinfo("Delete", "Successfully Deleted", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)



        
 


            # ============reset==============
 def reset_data(self):
     self.var_dep.set("Select Department")
     self.var_course.set("Select Course")
     self.var_year.set("Select Year")
     self.var_semester.set("Select Semester")
     self.var_id.set("")
     self.var_name.set("")
     self.var_div.set("Division")
     self.var_rollno.set("")
     self.var_gender.set("Male")
     self.var_dob.set("")
     self.var_mail.set("")
     self.var_phoneNo.set("")
     self.var_add.set("")
     self.var_teacher.set("")
     self.var_radio1.set("")


   

     # ============Generate data set or take photo sample==============
 # ============Generate data set or take photo sample==============
 def generate_dataset(self):
    if (
        self.var_dep.get() == "Select Department"
        or self.var_course.get() == "Select Course"
        or self.var_id.get() == ""
    ):
        messagebox.showerror("Error", "All Fields are Required", parent=self.root)
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="yash",
                database="python_project",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from student")
            myresult = my_cursor.fetchall()
            id = 0
            for x in myresult:
                id += 1
                my_cursor.execute(
                    """Update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,
                    dob=%s,rollno=%s,gender=%s,mail=%s,phoneNo=%s,address=%s,teacher=%s,photo=%s 
                    where id=%s""",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_dob.get(),
                        self.var_rollno.get(),
                        self.var_gender.get(),
                        self.var_mail.get(),
                        self.var_phoneNo.get(),
                        self.var_add.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()

            # Load Predefined data on haarcascade_frontalface_default
            face_classifier = cv2.CascadeClassifier("D:\Python\Project\Face Recognition System\haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped

            # Opening camera
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (500, 500))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "D:\Python\Project\data/user." + str(self.var_id.get()) + "." + str(
                        img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                                cv2.LINE_AA)
                    cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 1:
                        break

            cap.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Result", "Generating DataSet Successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()  


    
