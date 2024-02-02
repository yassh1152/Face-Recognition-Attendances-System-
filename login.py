from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win = Tk()
    app = Login(win)
    win.mainloop()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.sae = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.sae.place(x=50, y=210, width=250)
        self.newwin=None

        self.bg = ImageTk.PhotoImage(file=r"D:\Python\Project\image\login.jpg")
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=180, width=340, height=450)

        i1 = Image.open("D:\\Python\\Project\\image\\profile.png")
        i1 = i1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(i1)

        # Label
        l1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        l1.place(x=730, y=175, width=100, height=100)

        # Get Started
        gs = Label(frame, text="Get Started", font=("Times new roman", 20, "bold"), bg="black", fg="white")
        gs.place(x=95, y=100)

        # Labels username, password
        user = Label(frame, text="UserName", font=("Times new roman", 15, "bold"), bg="black", fg="white")
        user.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=185, width=270)

        pw = Label(frame, text="Password", font=("Times new roman", 15, "bold"), bg="black", fg="white")
        pw.place(x=70, y=225)

        self.pwe = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')  # Use show='*' to hide password
        self.pwe.place(x=40, y=250, width=270)

        # Icon Images
        i2 = Image.open("D:\Python\Project\image\profile.png")
        i2 = i2.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(i2)
        l2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        l2.place(x=650, y=340, width=25, height=25)

        i3 = Image.open("D:\Python\Project\image\pass.png")
        i3 = i3.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(i3)
        l3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        l3.place(x=650, y=405, width=25, height=25)

        # Login Button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE,
                          fg="white", bg="red", activeforeground="white", activebackground="red", )
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        rbtn = Button(frame, text="New User Register", command=self.rwun, font=("times new roman", 10, "bold"),
                      borderwidth=0, bd=3,
                      relief=RIDGE, fg="white", bg="black", activeforeground="black", activebackground="black")
        rbtn.place(x=20, y=350, width=160)

        # Forget Password
        fbtn = Button(frame, text="Forget Password", command=self.forgetpass, font=("times new roman", 10, "bold"),
                      borderwidth=0, bd=3,
                      relief=RIDGE, fg="white", bg="black", activeforeground="black", activebackground="black")
        fbtn.place(x=20, y=380, width=160)

    def rwun(self):
        self.newwin = Toplevel(self.root)
        self.app = Register(self.newwin)

    def login(self):
        if self.txtuser.get() == "" or self.pwe.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        elif self.txtuser.get() == "123" and self.pwe.get() == "123":
            messagebox.showinfo("Success", "Login Successful")
        else:

            conn = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="yash",
                                           database="studentm")
            mycur = conn.cursor()
            mycur.execute("Select * from register2 where email=%s and pass=%s", (
            self.txtuser.get(), self.pwe.get()))
            row = mycur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open = messagebox.askyesno("YN", "Access Only Admin")
                if open > 0:
                    self.newwin = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.newwin)
                else:
                    if not open:
                        return
            conn.commit()
            conn.close()

    # Forget Password
    def forgetpass(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="yash", database="studentm")
            mycur = conn.cursor()
            query = "select * from register2 where email=%s"
            value = (self.txtuser.get(),)
            mycur.execute(query, value)
            row = mycur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter the Valid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                sn = Label(self.root2, text="Select Security Question", font=("tiimes new roman", 15, "bold"))
                sn.place(x=40, y=90)
                self.secombo = ttk.Combobox(self.root2, font=("times new roman", 12, "bold"), state="readonly")
                self.secombo["values"] = ("Select", "Your GirlFriend Name", "Your BoyFriend Name", "Your BirthPlace")
                self.secombo.place(x=40, y=130, width=250, height=30)
                self.secombo.current(0)

                san = Label(self.root2, text="Security Question Answer", font=("times new roman", 15, "bold"))
                san.place(x=40, y=170)
                self.sae = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.sae.place(x=50, y=210, width=250)

                newpass = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"))
                newpass.place(x=50, y=250)
                self.newpasse = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.newpasse.place(x=50, y=280, width=250)

                btn = Button(self.root2, text="Reset", command=self.resetpass, font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=145, y=330)

    # Reset Password
    def resetpass(self):
        if self.secombo.get() == "Select":
            messagebox.showerror("error", "Select Security Question",parent=self.root2)
        elif self.sae.get() == "":
            messagebox.showerror("error", "Please Enter Answer",parent=self.root2)
        elif self.newpasse.get() == "":
            messagebox.showerror("error", "Please Enter The New Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="yash", database="studentm")
            mycur = conn.cursor()
            query = "Select * from register2 where email=%s and secq=%s and seca=%s"
            value = (self.txtuser.get(), self.secombo.get(), self.sae.get())
            mycur.execute(query, value)
            row = mycur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please Enter the Correct Answer",parent=self.root2)
            else:
                query1 = "Update register2 set pass = %s where email=%s"
                value = (self.newpasse.get(), self.txtuser.get())
                mycur.execute(query1, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Password Reset Successfully. Now You Can Login",parent=self.root2)
                # Close the current window
                self.root2.destroy()
                # Open a new instance of the Login class
                self.root.deiconify()

                

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        # Variable
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = IntVar()
        self.var_email = StringVar()
        self.var_secq = StringVar()
        self.var_seca = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()

        # Background Image
        # self.bg = ImageTk.PhotoImage(file=r"D:\\Python\\Project\\image\\re.jpg")
        # bg = Label(self.root, image=self.bg)
        # bg.place(x=0, y=0, relwidth=1, relheight=1)

        # leftside image
        # self.bg1 = ImageTk.PhotoImage(file=r"D:\\Python\\Project\\image\\b.jpg")
        # left = Label(self.root, image=self.bg1)
        # left.place(x=50, y=100, width=470, height=550)

        # Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=1550, height=700)

        # Label
        rl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen")
        rl.place(x=700, y=0)
        # Entry
        fn = Label(frame, text="First Name", font=("tiimes new roman", 15, "bold"))
        fn.place(x=40, y=50)
        fne = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fne.place(x=40, y=90, width=250)

        ln = Label(frame, text="Last  Name", font=("tiimes new roman", 15, "bold"))
        ln.place(x=500, y=50)
        lne = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        lne.place(x=500, y=90, width=250)

        cn = Label(frame, text="Contact No", font=("tiimes new roman", 15, "bold"))
        cn.place(x=40, y=150)
        cne = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        cne.place(x=40, y=190, width=250)

        en = Label(frame, text="Email", font=("tiimes new roman", 15, "bold"))
        en.place(x=500, y=150)
        ene = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        ene.place(x=500, y=190, width=250)

        sn = Label(frame, text="Select Security Question", font=("tiimes new roman", 15, "bold"))
        sn.place(x=40, y=250)

        self.secombo = ttk.Combobox(frame, textvariable=self.var_secq, font=("times new roman", 12, "bold"),
                                     state="readonly")
        self.secombo["values"] = ("Select", "Your GirlFriend Name", "Your BoyFriend Name", "Your BirthPlace")
        self.secombo.place(x=40, y=290, width=250, height=30)
        self.secombo.current(0)

        san = Label(frame, text="Security Question Answer", font=("times new roman", 15, "bold"))
        san.place(x=500, y=250)
        sae = ttk.Entry(frame, textvariable=self.var_seca, font=("times new roman", 15, "bold"))
        sae.place(x=500, y=290, width=250)

        pn = Label(frame, text="New Password", font=("tiimes new roman", 15, "bold"))
        pn.place(x=40, y=350)
        pne = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        pne.place(x=40, y=390, width=230)

        cpn = Label(frame, text="Confirm New Password", font=("tiimes new roman", 15, "bold"))
        cpn.place(x=500, y=350)
        cpne = ttk.Entry(frame, textvariable=self.var_cpass, font=("times new roman", 15, "bold"))
        cpne.place(x=500, y=390, width=250)

        # Checkbutton
        self.var_check = IntVar()
        cbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                           font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        cbtn.place(x=40, y=430)

        # Button
        i11 = Image.open("D:\\Python\\Project\\image\\now.png")
        i11 = i11.resize((200, 50))
        self.photoimm = ImageTk.PhotoImage(i11)
        b1 = Button(frame, image=self.photoimm, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=480, width=300)

        # i12 = Image.open("D:\\Python\\Project\\image\\log.png")
        # i12 = i12.resize((200, 100))
        # self.photoimm2 = ImageTk.PhotoImage(i12)
        # b2 = Button(frame, image=self.photoimm2, borderwidth=0, cursor="hand2")
        # b2.place(x=460, y=460, width=300, height=100)

    # Function Declaration
    def register_data(self):
        if len(str(self.var_contact.get())) != 10:
            messagebox.showerror("Error", "Contact number must have exactly 10 digits")
            return
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact == "" or self.var_email == "" or \
                self.var_seca == "" or self.var_secq == "" or self.var_pass == "" or self.var_cpass == "" or \
                self.var_check.get() == "Select":
            messagebox.showerror("Error", "All Fields Required")
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Password And Confirm Password Must be Same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree Terms & Condition")
        else:
            conn = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="yash",
                                           database="studentm")
            mycur = conn.cursor()
            query = ("Select * from register2 where contact=%s")
            value = (self.var_contact.get(),)
            mycur.execute(query, value)
            row = mycur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User Already Exist")
            else:
                conn = mysql.connector.connect(host="localhost", user="root", password="yash", database="studentm")
                mycur = conn.cursor()
                mycur.execute("Insert into register2 values (%s,%s,%s,%s,%s,%s,%s)", (
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
                messagebox.showinfo("Success", "Registered Successfully")
    
    

if __name__ == "__main__":
    main()
