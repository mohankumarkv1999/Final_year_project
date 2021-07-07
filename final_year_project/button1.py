from tkinter import *
from PIL import Image, ImageTk

root = Tk()
frame = Frame(root , width = 3000 , height = 3000)
frame.pack()
# Create a photoimage object of the image in the path
image1 = Image.open(r'E:\mohan\final_year_paroject\first_page.jpg')
test = ImageTk.PhotoImage(image1)
image2 = Image.open(r'E:\mohan\final_year_paroject\train.jpg')
test2 = ImageTk.PhotoImage(image1)

label = Label(root, text='FACE MASK DETECTION', image = test,
              fg = 'black',bg = '#eaf7ff',font = ('French Script MT ' ,70,'bold'))
label.pack()
b1 = Button(frame , text = "click me " ,width = 10 , height =5)
b1.place(x = 200 , y=200)
root.mainloop()