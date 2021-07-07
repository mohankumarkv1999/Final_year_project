from tkinter import *
import os
from PIL import Image, ImageTk
import pymysql
class app:
    def __init__(self , root):
        self.frame = Frame(root, width=3000, height=3000)
        self.frame.pack()
        self.image1 = Image.open(r'E:\pycharm_project\Final_year_project\project_images\entry_page.jpg')
        self.test = ImageTk.PhotoImage(self.image1)
        self.t11 = Text(self.frame, width=1000, height=1000)
        self.t11.image_create(END, image=self.test)
        self.t11.pack()
        self.butt = Button(self.frame , bg = "black", fg = "white" , text = "Process ===>",
                        font = ('verdana', 10, 'bold'), width = 13, height = 2, command = self.first_page)
        self.butt.place(x = 700 , y=600)
    def first_page(self):
        self.frame.destroy()
        self.frame = Frame(root , width = 3000 , height = 3000)
        self.frame.pack()
        self.image1 = Image.open(r'E:\pycharm_project\Final_year_project\project_images\first_page.jpg')
        self.test = ImageTk.PhotoImage(self.image1)
        self.t11 = Text(self.frame ,width = 1000 , height =1000)
        self.t11.image_create(END , image = self.test)
        self.t11.pack()
        self.label = Label(self.frame, text='FACE MASK DETECTION',  compound='center' , fg = 'black',
                           bg = '#eaf7ff', font = ('French Script MT ' ,70,'bold')).place(x=150 , y=20)
        self.b11 = Button(self.frame ,bg ='#fbce8b',fg='Black', text = "register" ,
                         font=('verdana', 10, 'bold'),width = 13 , height =2 , command = self.register)
        self.b11.place(x = 200 , y=600)
        self.b12 = Button(self.frame,bg ='#fbce8b',fg='Black', text="Detect",
                         font = ('verdana', 10, 'bold'), width = 13, height = 2 ,command = self.detect)
        self.b12.place(x=600, y=600)
        self.b13 = Button(self.frame, text="Exit",bg ='#fbce8b',fg='Black',
                         font=('verdana', 10, 'bold'), width=13, height=2, command = self.exit)
        self.b13.place(x=1000, y=600)
    def register(self):
        self.frame.destroy()
        self.frame = Frame(root, width=5000, height=5000, bg='#fbce8b')
        self.frame.pack()
        self.label2 = Label(self.frame, text='FILL ALL THE REQUIRED DETAILS', fg='black',
                           bg='#fbce8b', font=('French Script MT ', 50, 'bold')).place(x=150, y=20)
        self.label21 = Label(self.frame, text='Enter your user name =>', fg='black',
                            bg='#fbce8b', font=('French Script MT ', 20, 'bold')).place(x=50, y=150)
        self.enter21 = Entry(self.frame, width=50, fg='black', bg='white', font=('arial', 15))
        self.enter21.place(x=650, y=150)
        self.label22 = Label(self.frame, text='Enter your email_id =>', fg='black',
                           bg='#fbce8b', font=('French Script MT ', 20, 'bold')).place(x=50, y=250)
        self.enter22 = Entry(self.frame, width=50, fg='black', bg='white', font=('arial', 15))
        self.enter22.place(x=650, y=250)
        self.b23 = Button(self.frame, text="Upload Images", bg='blue', fg='Black',
                          font=('verdana', 10, 'bold'), width=13, height=2, command=self.upload_image)
        self.b23.place(x=200, y=600)
        self.b24 =Button(self.frame, text="Back", bg='blue', fg='Black',
                          font=('verdana', 10, 'bold'), width=13, height=2, command=self.first_page)
        self.b24.place(x=600, y=600)
    def upload_image(self):
        os.system(r'python "E:\pycharm_project\Final_year_project\face_recognization\collect_data.py"')
        self.b24 = Button(self.frame, text='submit', bg='blue', fg='black',
                         font=('verdana', 10, 'bold'), width=13, height=2, command=self.insert)
        self.b24.place(x=1000, y=600)
    def insert(self):
        username = self.enter21.get()
        email = self.enter22.get()
        conn1 = pymysql.connect(host='localhost', database='final_project', user='root', password='7338272260ksv')
        cursor1 = conn1.cursor()
        str1 = "select max(id) from register"
        cursor1.execute(str1)
        row1 = cursor1.fetchone()
        id = row1[0] +1

        # save the data in Database
        conn2 = pymysql.connect(host='localhost', database='final_project', user='root', password='7338272260ksv')
        cursor2 = conn2.cursor()
        str = "insert into register(id , username , email) values ('%d' , '%s' , '%s')"
        args = (id, username, email)
        cursor2.execute(str % args)
        conn2.commit()
        os.system(r'python "E:\pycharm_project\Final_year_project\face_recognization\training_data.py"')
        self.frame.destroy()
        self.frame = Frame(root, width=5000, height=5000, bg='#fbce8b')
        self.frame.pack()
        self.label2 = Label(self.frame, text='Thank you for giving the Details', fg='black',
                            bg='#fbce8b', font=('French Script MT ', 50, 'bold')).place(x=150, y=20)

        self.b = Button(self.frame, text='exit', bg='#fbce8b', fg='Red',
                      font=('verdana', 10, 'bold'), width=13, height=2, command=self.first_page)
        self.b.place(x=600 , y = 600)

    def detect(self):
        os.system(r'python "E:\pycharm_project\Final_year_project\Face-Mask-Detection-master\Face-Mask-Detection-master\detect_mask_video.py"')
        self.frame.destroy()
        self.frame = Frame(root, width=3000, height=3000)
        self.frame.pack()
        self.image1 = Image.open(r'E:\pycharm_project\Final_year_project\project_images\without_mask_alert.jpg')
        self.test = ImageTk.PhotoImage(self.image1)
        self.t11 = Text(self.frame, width=1000, height=1000)
        self.t11.image_create(END, image=self.test)
        self.t11.pack()
        self.butt = Button(self.frame, fg="black", text="Exit",
                           font=('verdana', 10, 'bold'), width=13, height=2, command=self.exit)
        self.butt.place(x=1100, y=400)

    def exit(self):
        exit()
root = Tk()
mb = app(root)
root.mainloop()