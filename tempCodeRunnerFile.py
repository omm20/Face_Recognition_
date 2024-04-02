 img_left = Image.open(r"C:\Users\omm_s\OneDrive\Desktop\Facial_Recognition_System/logo-m2.png")
        img_left = img_left.resize((720, 130), Image.LANCZOS)

        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 720, height=130)
