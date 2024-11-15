from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector as conn
from homepage import second

db = conn.connect(host="localhost", user="root", password="", database="python_file")
mycursor = db.cursor()


class loginpage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1365x800')
        self.window.resizable(False, False)
        self.window.title('FEROUS')
        self.window.configure(cursor="pirate")
        bg_frame = Image.open('intelli.png')
        new_image = bg_frame.resize((1365, 800))
        new_image.save('image_623.png')
        photo = ImageTk.PhotoImage(new_image)
        bg_Label = Label(self.window, image=photo)
        bg_Label.image = photo
        bg_Label.pack(fill='both', expand='yes')
        image1 = PhotoImage(file='FEROUS.png')
        self.window.iconphoto(False, image1)

        frame = Frame(window, width=800, height=360, bg='black')
        frame.place(x=260, y=180)
        frame_label = Label(frame, text="Have an account?", font=('calisto mt', 20), fg='white', bg='black')
        frame_label.place(x=420, y=50)
        frame_label2 = Label(frame, text="Personalize your A.I mouse to", font=('calisto mt', 15), fg='white',
                             bg='black')
        frame_label2.place(x=420, y=100)
        frame_label2 = Label(frame, text="get the best experience", font=('calisto mt', 15), fg='white',
                             bg='black')
        frame_label2.place(x=420, y=130)
        signin_btn = Button(frame, width=15, font=('calisto mt', 13), text='LOG IN', bg='black', fg='white',
                            command=lambda: log())
        signin_btn.place(x=420, y=190)
        frame2 = Frame(window, width=360, height=400, bg='white')
        frame2.place(x=280, y=160)
        signup = Label(frame2, text="SIGN UP", font=('calisto mt', 17), fg='#1D2F43', bg='white')
        signup.place(x=40, y=20)

        first_name = Label(frame2, text="First_name", font=('calisto mt', 13), fg='#32393E', bg='white')
        first_name.place(x=40, y=60)
        first_name.entry = Entry(frame2, width=20, font=('calisto mt', 13))
        first_name.entry.place(x=40, y=90)
        last_name = Label(frame2, text="Last_name", font=('calisto mt', 13), fg='#32393E', bg='white')
        last_name.place(x=40, y=130)
        last_name.entry = Entry(frame2, width=20, font=('calisto mt', 13))
        last_name.entry.place(x=40, y=160)
        email = Label(frame2, text="Email", font=('calisto mt', 13), fg='#32393E', bg='white')
        email.place(x=40, y=200)
        email.entry = Entry(frame2, width=20, font=('calisto mt', 13))
        email.entry.place(x=40, y=230)
        password = Label(frame2, text="Password", font=('calisto mt', 13), fg='#32393E', bg='white')
        password.place(x=40, y=270)
        password.entry = Entry(frame2, width=20, font=('calisto mt', 13))
        password.entry.place(x=40, y=300)
        password.entry.configure(show="....")

        signup_btn = Button(frame2, width=10, font=('calisto mt', 13), text='SIGN UP', bg='black', fg='white',
                            command=lambda: signup())
        signup_btn.place(x=230, y=350)

        def signup():
            if email.entry.get() == "" and password.entry.get() == "" and first_name.entry.get() == "" and last_name.entry.get() == "":
                messagebox.showerror("Error", "All Fields are Required")
            elif first_name.entry.get() == "":
                messagebox.showerror("Error", "First_name is required")
            elif last_name.entry.get() == "":
                messagebox.showerror("Error", "last_name is required")
            elif email.entry.get() == "":
                messagebox.showerror("Error", "Email field is required")
            elif password.entry.get() == "":
                messagebox.showerror("Error", "Password field is required")
            else:
                query = f"INSERT INTO `ai mouse`(`first_name`, `last_name`, `Email`, `password`) VALUES ('{first_name.entry.get()}'," \
                        f"'{last_name.entry.get()}','{email.entry.get()}','{password.entry.get()}')"
                mycursor.execute(query)
                db.commit()
                messagebox.showinfo("DONE", "Sign-Up Completed")

        var1 = BooleanVar(value=False)
        check = Checkbutton(frame2, text="Show password", onvalue=1, offvalue=0, variable=var1,
                            command=lambda: Show_password(),
                            bg="white")
        check.place(x=40, y=350)

        def Show_password():
            if var1.get() == 1:
                password.entry.config(show="")
            else:
                password.entry.config(show="..")

        def log():
            frame.place_forget()
            frame2.place_forget()
            frame1 = Frame(window, width=800, height=360, bg='black')
            frame1.place(x=270, y=180)
            frame3 = Frame(window, width=360, height=400, bg='white')
            frame3.place(x=685, y=160)
            email = Label(frame3, text="Email", font=('calisto mt', 13), fg='#32393E', bg='white')
            email.place(x=40, y=100)
            email.entry = Entry(frame3, width=20, font=('calisto mt', 13))
            email.entry.place(x=40, y=130)
            password1 = Label(frame3, text="Password", font=('calisto mt', 13), fg='#32393E', bg='white')
            password1.place(x=40, y=170)
            password1.entry = Entry(frame3, width=20, font=('calisto mt', 13))
            password1.entry.place(x=40, y=200)
            password1.entry.configure(show="...")
            LOGIN_btn = Button(frame3, width=10, font=('calisto mt', 13), text='LOG IN', bg='black', fg='white',
                               command=lambda: loggin())
            LOGIN_btn.place(x=230, y=300)

            def home():
                bg_Label.pack_forget()
                frame.place_forget()
                frame2.place_forget()
                frame1.place_forget()
                frame3.place_forget()
                second(window)

            def loggin():
                if email.entry.get() == "" and password1.entry.get() == "":
                    messagebox.showerror("Error", "All Fields are Required")
                elif email.entry.get() == "":
                    messagebox.showerror("Error", "Email is required")
                elif password1.entry.get() == "":
                    messagebox.showerror("Error", "Password is required")
                else:
                    query = f"SELECT * FROM `ai mouse` WHERE `Email` = '{email.entry.get()}' and `password` ='{password1.entry.get()}' "
                    mycursor.execute(query)
                    data = mycursor.fetchall()
                    if len(data) > 0:
                        home()
                    else:
                        messagebox.showerror("Error", "Invalid login details")

            var1 = BooleanVar(value=False)
            check = Checkbutton(frame3, text="Show password", onvalue=1, offvalue=0, variable=var1,
                                command=lambda: Show_password(),
                                bg="white")
            check.place(x=230, y=250)

            def Show_password():
                if var1.get() == 1:
                    password1.entry.config(show="")
                else:
                    password1.entry.config(show="..")

            login = Label(frame3, text="LOG IN", font=('calisto mt', 17), fg='#1D2F43', bg='white')
            login.place(x=40, y=30)
            frame1_label = Label(frame1, text="Don't Have an account?", font=('calisto mt', 20), fg='white', bg='black')
            frame1_label.place(x=70, y=50)
            frame6_label2 = Label(frame1, text="Personalize your A.I mouse to", font=('calisto mt', 15), fg='white',
                                  bg='black')
            frame6_label2.place(x=70, y=100)
            frame7_label2 = Label(frame1, text="get the best experience to", font=('calisto mt', 15), fg='white',
                                  bg='black')
            frame7_label2.place(x=70, y=130)
            frame8_label2 = Label(frame1, text="learn more ......", font=('calisto mt', 15), fg='white',
                                  bg='black')
            frame8_label2.place(x=70, y=160)
            signup_btn = Button(frame1, width=15, font=('calisto mt', 13), text='SIGN UP', bg='black', fg='white',
                                command=lambda: sign())
            signup_btn.place(x=70, y=210)

            def sign():
                frame1.place_forget()
                frame3.place_forget()
                loginpage(window)
