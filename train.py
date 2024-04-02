from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl = Label(self.root,text="Train data set",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"photos/logo-m2.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)

        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 1530, height=325)
# button
        b1_1=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="white",fg="black")
        b1_1.place(x=0,y=380,width=1530,height=60)


        img_bottom = Image.open(r"photos/logo-m2.png")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)

        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image = self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width = 1530, height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')# gray scale image
            imgageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imgageNp)
            ids.append(id)
            cv2.imshow("trainigng",imgageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #===========Train the classifier and save
        recognizer = cv2.face.LBPHFaceRecognizer_create()


        recognizer.train(faces,ids)
        recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training satas set completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()