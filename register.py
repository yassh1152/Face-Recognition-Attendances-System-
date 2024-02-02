from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
            # Variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=IntVar()
        self.var_email=StringVar()
        self.var_secq=StringVar()
        self.var_seca=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()



        #         #  Background Image
        # self.bg = ImageTk.PhotoImage(file=r"D:\\Python\\Project\\image\\re.jpg")
        # bg = Label(self.root, image=self.bg)
        # bg.place(x=0, y=0, relwidth=1, relheight=1)

        #         #    leftside image
        # self.bg1 = ImageTk.PhotoImage(file=r"D:\\Python\\Project\\image\\b.jpg")
        # left = Label(self.root, image=self.bg1)
        # left.place(x=50, y=100, width=470, height=550)

                #    Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=0,y=0,width=1550,height=700)

            #   Label
        rl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen")
        rl.place(x=700,y=0)
            #  Entry
        fn=Label(frame,text="First Name",font=("tiimes new roman",15,"bold"))
        fn.place(x=40,y=50)    
        fne=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fne.place(x=40,y=90,width=250)

        ln=Label(frame,text="Last  Name",font=("tiimes new roman",15,"bold"))
        ln.place(x=500,y=50)    
        lne=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lne.place(x=500,y=90,width=250)

        cn=Label(frame,text="Contact No",font=("tiimes new roman",15,"bold"))
        cn.place(x=40,y=150)    
        cne=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        cne.place(x=40,y=190,width=250)

        en=Label(frame,text="Email",font=("tiimes new roman",15,"bold"))
        en.place(x=500,y=150)    
        ene=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        ene.place(x=500,y=190,width=250)

        sn=Label(frame,text="Select Security Question",font=("tiimes new roman",15,"bold"))
        sn.place(x=40,y=250)    

        self.secombo=ttk.Combobox(frame,textvariable=self.var_secq,font=("times new roman",12,"bold"),state="readonly")
        self.secombo["values"]=("Select","Your GirlFriend Name","Your BoyFriend Name","Your BirthPlace")
        self.secombo.place(x=40,y=290,width=250,height=30)
        self.secombo.current(0)
        

        san=Label(frame,text="Security Question Answer",font=("times new roman",15,"bold"))
        san.place(x=500,y=250)    
        sae=ttk.Entry(frame,textvariable=self.var_seca,font=("times new roman",15,"bold"))
        sae.place(x=500,y=290,width=250)

        pn=Label(frame,text="New Password",font=("tiimes new roman",15,"bold"))
        pn.place(x=40,y=350)    
        pne=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        pne.place(x=40,y=390,width=230)

        cpn=Label(frame,text="Confirm New Password",font=("tiimes new roman",15,"bold"))
        cpn.place(x=500,y=350)    
        cpne=ttk.Entry(frame,textvariable=self.var_cpass,font=("times new roman",15,"bold"))
        cpne.place(x=500,y=390,width=250)


            # Checkbutton
        self.var_check=IntVar()
        cbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        cbtn.place(x=40,y=430)

            #  Button 
        i11 = Image.open("D:\\Python\\Project\\image\\now.png")
        i11 = i11.resize((200, 50))
        self.photoimm = ImageTk.PhotoImage(i11)
        b1 = Button(frame, image=self.photoimm,command=self.register_data,borderwidth=0, cursor="hand2")
        b1.place(x=10, y=480, width=300)


        i12= Image.open("D:\Python\Project\image\log.png")
        i12 = i12.resize((200, 100))
        self.photoimm2 = ImageTk.PhotoImage(i12)
        b2 = Button(frame, image=self.photoimm2, borderwidth=0, cursor="hand2")
        b2.place(x=460, y=460, width=300,height=100)

        #    Function Decleration
    def register_data(self):
        if self.var_fname.get=="" or self.var_lname.get=="" or self.var_contact==0 or self.var_email=="" or self.var_seca=="" or self.var_secq=="" or self.var_pass=="" or self.var_cpass=="" or self.var_check.get()=="Select":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_pass.get()!=self.var_cpass.get():
            messagebox.showerror("Error","Password And Confirm Password Must be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Terms & Condition")
        else:
            conn=mysql.connector.connect(host="localhost",
                                   username="root",
                                   password="yash",
                                   database="studentm")
            mycur=conn.cursor()
            query=("Select * from register where contact=%s")
            value=(self.var_contact.get(),)
            mycur.execute(query,value)
            row=mycur.fetchone()
            if row != None:
                messagebox.showerror("Error","User Already Exist")
            else:
                mycur.execute("Insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_secq.get(),
                                                                                     self.var_seca.get(),
                                                                                     self.var_pass.get()
                                                                                
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered Successfully")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
