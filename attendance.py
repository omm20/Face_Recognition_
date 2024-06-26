from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
#=====================variavles
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar() 
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        
                #first image for student details page
        img = Image.open(r"photos/logo-m2.png")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 800, height=200)

#second image for student 
        img1 = Image.open(r"photos/logo-m2.png")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=800,y=0,width = 800, height=200)

#bg image
        
        img3 = Image.open(r"photos/up_img1.png")
        img3 = img3.resize((1530, 710), Image.LANCZOS)

        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=200,width = 1530, height=710)

        title_lbl = Label(bg_img,text="Attendance System",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#main frame 
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)
#left frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"photos/logo-m2.png")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 720, height=130)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #Labels and entry
#attedance id
        attendanceId_lable = Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

#Name
        rollLable = Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        rollLable.grid(row=0,column=2,padx=4,pady=8)

        atten_roll = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

#date
        nameLable = Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        nameLable.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

#department
        
        depLable = Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        depLable.grid(row=1,column=2)

        atten_dep = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3)

#time
        timeLable = Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timeLable.grid(row=2,column=0)

        atten_time = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

#Date
        dateLable = Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        dateLable.grid(row=2,column=2)

        atten_date = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=8)

#attendance
        attendanceLable = Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendanceLable.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

#buttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



#right frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #===============scroll bat table

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceId")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendane ")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100) 
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
#=============fetchdata
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
          self.AttendanceReportTable.insert("",END,values=i)
#=======import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)

        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    
#==============export csv
    def exportCsv(self):
      try:
          if len(mydata)<1:
              messagebox.showerror("No data","No data Found to export",parent=self.root)
              return False
          fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)       
          with open(fln,mode="w",newline="") as myfile:
              exp_write=csv.writer(myfile,delimiter=",")
              for i in mydata:
                  exp_write.writerow(i)
              messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"Successfully")
      except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self, event=""):
      cursor_row = self.AttendanceReportTable.focus()
      content = self.AttendanceReportTable.item(cursor_row)
    
    # Check if 'values' key exists in the content dictionary
      if 'values' in content:
        rows = content['values']
        if rows:
            # Update the variables if rows exist
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6]) 
        else:
            messagebox.showerror("Error", "No record found", parent=self.root)
      else:
        messagebox.showerror("Error", "No record found", parent=self.root)

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")












if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()