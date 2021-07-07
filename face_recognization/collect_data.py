import cv2
import numpy as np
import pymysql
faceDetect=cv2.CascadeClassifier(r'E:\pycharm_project\Final_year_project\face_recognization\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

conn1 = pymysql.connect(host='localhost', database='final_project', user='root', password='7338272260ksv')
cursor1 = conn1.cursor()
str1 = "select max(id) from register"
cursor1.execute(str1)
row1 = cursor1.fetchone()
id = row1[0] +1
sampleNum=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.25,3)
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite(r'E:\pycharm_project\Final_year_project\face_recognization\dataset/user.'+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if (sampleNum > 100):
        break
cam.release()
cv2.destroyAllWindows()