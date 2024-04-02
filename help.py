from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl = Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"photos/logo-m2.png")
        img_top = img_top.resize((1530, 725), Image.LANCZOS)

        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 1530, height=725)

        dev_lable = Label(f_lbl,text="Email:kumarom202002@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_lable.place(x=600,y=200)





if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()