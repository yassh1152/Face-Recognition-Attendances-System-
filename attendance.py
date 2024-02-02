from tkinter import *
from PIL import Image, ImageTk
import cv2
import mysql.connector
from datetime import datetime
from tkinter import ttk
import os
import csv
from tkinter import dialog
from tkinter import filedialog
from tkinter import ttk, messagebox

mydata=[]
class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1080+0+0")
        self.root.title("Face Recognition System")


            # ============Variable===========
        self.var_attendance=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_a_attendance=StringVar()

        # First image
        imgtop = Image.open("D:\\Python\\Project\\image\\a1.webp")
        imgtop = imgtop.resize((800, 200))
        self.photoimage_top = ImageTk.PhotoImage(imgtop)

        self.l2 = Label(self.root, image=self.photoimage_top)
        self.l2.place(x=0, y=0, width=800, height=200)

        # Second image
        imgbot = Image.open("D:\\Python\\Project\\image\\a2.jpg")
        imgbot = imgbot.resize((800, 200))
        self.photoimage_bot = ImageTk.PhotoImage(imgbot)

        self.l2_bot = Label(self.root, image=self.photoimage_bot)
        self.l2_bot.place(x=800, y=0, width=800, height=200)

        # t1 = Label( text="Attendances Manegment System", font=("times new roman", 35, "bold"),
        #            bg="white", fg="darkblue")
        # t1.place(x=0, y=0, width=1530, height=45)
        # bg Image

        img4 = Image.open("D:\Python\\Project\\image\\bg.jpeg")
        img4 = img4.resize((1550, 710))
        self.photoimage4 = ImageTk.PhotoImage(img4)

        bg = Label(self.root, image=self.photoimage4)
        bg.place(x=0, y=200, width=1530, height=710)

        t1 = Label(bg, text="Attendances Manegment System", font=("times new roman", 35, "bold"),
                   bg="white", fg="darkblue")
        t1.place(x=0, y=0, width=1530, height=55)

        # Frame
        f1 = Frame(bg, bd=2)
        f1.place(x=0, y=60, width=1550, height=600)

        # left side label frame
        lf = LabelFrame(f1, bd=2, bg="white", relief=RIDGE, text="Student Attendances Details",
                        font=("times new roman", 12, "bold"))
        lf.place(x=10, y=10, width=730, height=580)

        imglf = Image.open("D:\\Python\\Project\\image\\attendance-management.jpg")
        imglf = imglf.resize((720, 130))
        self.photoimageleft = ImageTk.PhotoImage(imglf)

        l2 = Label(lf, image=self.photoimageleft)
        l2.place(x=5, y=0, width=720, height=150)

        leftinsideframe=Frame(lf,bd=2,relief=RIDGE,bg="white")
        leftinsideframe.place(x=0,y=135,width=720,height=370)


        # attendances id
        attid = Label(leftinsideframe, text='Attendances ID', font=("times new roman", 12, "bold"), bg="white")
        attid.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attentry = ttk.Entry(leftinsideframe, width=20,textvariable=self.var_attendance, font=("times new roman", 12, "bold"))
        attentry.grid(row=0, column=1, padx=10, sticky=W)

        # Roll No
        nameid = Label(leftinsideframe, text='Roll No', font=("comicsansns 11 bold", 12, "bold"), bg="white")
        nameid.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        nameentry = ttk.Entry(leftinsideframe, width=20,textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        nameentry.grid(row=0, column=3, padx=8, sticky=W)

        # Name
        dateid = Label(leftinsideframe, text='Name', font=("comicsansns 11 bold", 12, "bold"), bg="white")
        dateid.grid(row=1, column=0)

        dateentry = ttk.Entry(leftinsideframe, width=20,textvariable=self.var_name, font=("comicsansns 11 bold", 12, "bold"))
        dateentry.grid(row=1, column=1, padx=8)

        # Department
        deptid = Label(leftinsideframe, text='Department', font=("comicsansns 11 bold", 12, "bold"), bg="white")
        deptid.grid(row=1, column=2)

        deptentry = ttk.Entry(leftinsideframe, width=20,textvariable=self.var_dep, font=("comicsansns 11 bold", 12, "bold"))
        deptentry.grid(row=1, column=3, padx=8)
        
        # time
        timeid = Label(leftinsideframe, text='Time', font=("comicsansns 11 bold", 12, "bold"), bg="white")
        timeid.grid(row=2, column=0)

        timeentry = ttk.Entry(leftinsideframe, width=20,textvariable=self.var_time,font=("comicsansns 11 bold", 12, "bold"))
        timeentry.grid(row=2, column=1, padx=8)

         # date
        dateeid = Label(leftinsideframe, text='Date', font=("comicsansns 11 bold", 12, "bold"), bg="white")
        dateeid.grid(row=2, column=2)

        dateentry = ttk.Entry(leftinsideframe, width=20,textvariable=self.var_date,font=("comicsansns 11 bold", 12, "bold"))
        dateentry.grid(row=2, column=3, padx=8)

         # attendances
        aid = Label(leftinsideframe, text='attendances', font=("comicsansns 11 bold", 12, "bold"), bg="white")
        aid.grid(row=2, column=2)

        aentry = ttk.Entry(leftinsideframe, width=20,textvariable=self.var_a_attendance,font=("comicsansns 11 bold", 12, "bold"))
        aentry.grid(row=2, column=3, padx=8)

            #    attendance
        attlabel=Label(leftinsideframe,text="Attendances Status",bg="white",font="comicsansans 11 bold")
        attlabel.grid(row=3,column=0)

        self.attstatus=ttk.Combobox(leftinsideframe,width=20,font="comicsansans 11 bold",state="readonly")
        self.attstatus["values"]=("Status","Present","Absent")
        self.attstatus.grid(row=3,column=1,pady=8)
        self.attstatus.current(0)

        #Button Frame
        buttonframe=Frame(leftinsideframe,bd=2,relief=RIDGE,bg="white")
        buttonframe.place(x=0,y=300,width=715,height=70)
              #importcsv button
        savebtn=Button(buttonframe,text="Import CSV",command=self.importcsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        savebtn.grid(row=0,column=0)
           #exportcsv  button
        upbtn=Button(buttonframe,text="Export CSV",command=self.exportcsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        upbtn.grid(row=0,column=1)
             #update
        delbtn=Button(buttonframe,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delbtn.grid(row=0,column=2)
            #reset
        rebtn=Button(buttonframe,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        rebtn.grid(row=0,column=3)





                #right frame
        rf = LabelFrame(f1, bd=2, bg="white", relief=RIDGE, text="Attendances Details",
                        font=("times new roman", 12, "bold"))
        rf.place(x=750, y=10, width=720, height=580)

        # imgrf = Image.open("D:\\Python\\Project\\image\\attendance-management.jpg")
        # imglf = imglf.resize((720, 130))
        # self.photoimageleft = ImageTk.PhotoImage(imglf)

        # l2 = Label(lf, image=self.photoimageleft)
        # l2.place(x=5, y=0, width=720, height=150)

        tableframe=Frame(rf,bd=2,relief=RIDGE,bg="white")
        tableframe.place(x=5,y=5,width=707,height=455)

                #  ==============Scroll Bar Table ================
        scrollx=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.Attendancesreporttable=ttk.Treeview(tableframe,column=("id","roll","name","department","time","date","attendances"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        self.Attendancesreporttable.heading("id",text="Attendances ID")
        self.Attendancesreporttable.heading("roll",text="Roll No")
        self.Attendancesreporttable.heading("name",text="Name")
        self.Attendancesreporttable.heading("department",text="Department")
        self.Attendancesreporttable.heading("time",text="Time")
        self.Attendancesreporttable.heading("date",text="Date")
        self.Attendancesreporttable.heading("attendances",text="Attendances")
        
        self.Attendancesreporttable["show"]="headings"
        self.Attendancesreporttable.column("id",width=100)
        self.Attendancesreporttable.column("roll",width=100)
        self.Attendancesreporttable.column("name",width=100)
        self.Attendancesreporttable.column("department",width=100)
        self.Attendancesreporttable.column("time",width=100)
        self.Attendancesreporttable.column("date",width=100)
        self.Attendancesreporttable.column("attendances",width=100)
       
        self.Attendancesreporttable.pack(fill=BOTH,expand=1)
        self.Attendancesreporttable.bind("<ButtonRelease>",self.get_cursor)



        #    ==============Fetchg Data=============
    def fetchdata(self,rows):
        self.Attendancesreporttable.delete(*self.Attendancesreporttable.get_children())
        for i in rows:
            self.Attendancesreporttable.insert("",END,values=i)
        
       
    
    def importcsv(self):
        global mydata
        mydata.clear()
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(filename,encoding="utf-8") as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
    
         #================Export CSV============
    def exportcsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data Found to Export",parent=self.root)
                return False
            filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            with open(filename,mode="w",newline="") as myfile:
                exportwrite = csv.writer(myfile, delimiter=",") 
                for i in mydata:
                    exportwrite.writerow(i)
                messagebox.showinfo("dataexport","Your Data Exported Successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    def get_cursor(self,event=""):
        cursorrow=self.Attendancesreporttable.focus()
        content=self.Attendancesreporttable.item(cursorrow)
        rows=content["values"]
        self.var_attendance.set(rows[0]) 
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_a_attendance.set(rows[6])
    
    def reset_data(self):
        self.var_attendance.set("") 
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_a_attendance.set("")
    
   

    





if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()
