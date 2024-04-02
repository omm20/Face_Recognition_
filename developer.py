from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl = Label(self.root,text="Devoloper",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"photos/logo-m2.png")
        img_top = img_top.resize((1530, 725), Image.LANCZOS)

        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 1530, height=725)
#Frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=500,height=600)
#devoler img
        img_top1 = Image.open(r"photos/logo-m2.png")
        img_top1 = img_top1.resize((1530, 725), Image.LANCZOS)

        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame,image = self.photoimg_top1)
        f_lbl.place(x=300,y=0,width = 200, height=200)
#developer info
        dev_lable = Label(main_frame,text="Omm",font=("times new roman",20,"bold"),bg="white")
        dev_lable.place(x=0,y=5)
        dev_lable = Label(main_frame,text="I am software engineer",font=("times new roman",20,"bold"),bg="white")
        dev_lable.place(x=0,y=40)

        img2 = Image.open(r"photos/logo-m2.png")
        img2 = img2.resize((500,300), Image.LANCZOS)

        self.photoimg_top2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame,image = self.photoimg_top2)
        f_lbl.place(x=0,y=210,width = 500, height=300)






if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()