from tkinter import *
import signe

root = Tk()
root.resizable(False, False)
height = 350
width = 500
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
root.configure(bg='white')
root.configure(cursor="pirate")
# image = PhotoImage(file='VISION.png')
# bg_Label = Label(root, image=image, bg='white')
# bg_Label.pack(fill='both', expand='yes')

progress_label = Label(root, text="Please Wait....", font=("yu gothic ui", 13, 'bold'), bg="white", fg='grey')
progress_label.place(x=180, y=300)
i = 0


def top():
    win = Toplevel()
    signe.loginpage(win)
    root.withdraw()
    # win.deiconify()


def load():
    global i
    if i <= 5:
        txt = 'Please Wait....' + (str(20 * i) + '%')
        progress_label.configure(text=txt)
        progress_label.after(800, load)
        i += 1
    else:
        top()


load()
root.mainloop()


