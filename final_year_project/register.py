from tkinter import *
class register:
    def __init__(self , root):
        self.frame2 = Frame(root, bg='#eaf7ff', width=3000, height=3000)
        self.frame2.pack()
        self.label1 = Label(self.frame2, text='FACE MASK DETECTION', compound='center', fg='black',
                           bg='#eaf7ff', font=('French Script MT ', 70, 'bold')).place(x=150, y=20)

root = Tk()

root.mainloop()
