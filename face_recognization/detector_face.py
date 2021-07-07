import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier(r'E:\pycharm_project\Final_year_project\face_recognization\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face_LBPHFaceRecognizer.create()
rec.read(r'E:\pycharm_project\Final_year_project\face_recognization\recognizer\trainningData.yml')
id =0
font= cv2.FONT_HERSHEY_SIMPLEX
ret,img=cam.read()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceDetect.detectMultiScale(gray,1.25,3)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    id, conf = rec.predict(gray[y:y+h,x:x+w])
    cv2.putText(img,str(id),(x,y+h),font,1,255,2)
    print(id)
cv2.imshow("Face",img)
cv2.imshow("Face",img)

cam.release()
cv2.destroyAllWindows()