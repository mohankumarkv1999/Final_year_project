# USAGE
# python detect_mask_video.py

# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import cv2
import test

def detect_and_predict_mask(frame, faceNet, maskNet):
	# grab the dimensions of the frame and then construct a blob
	# from it
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
		(104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the face detections
	faceNet.setInput(blob)
	detections = faceNet.forward()

	# initialize our list of faces, their corresponding locations,
	# and the list of predictions from our face mask network
	faces = []
	locs = []
	preds = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the detection
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the confidence is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# compute the (x, y)-coordinates of the bounding box for
			# the object
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of
			# the frame
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extract the face ROI, convert it from BGR to RGB channel
			# ordering, resize it to 224x224, and preprocess it
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)

			# add the face and bounding boxes to their respective
			# lists
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	# only make a predictions if at least one face was detected
	if len(faces) > 0:
		# for faster inference we'll make batch predictions on *all*
		# faces at the same time rather than one-by-one predictions
		# in the above `for` loop
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

	# return a 2-tuple of the face locations and their corresponding
	# locations
	return (locs, preds)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", type=str,
	default=r"E:\pycharm_project\Final_year_project\Face-Mask-Detection-master\Face-Mask-Detection-master\face_detector",
	help="path to face detector model directory")
ap.add_argument("-m", "--model", type=str,
	default=r"E:\pycharm_project\Final_year_project\Face-Mask-Detection-master\Face-Mask-Detection-master\mask_detector.model",
	help="path to trained face mask detector model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized face detector model from disk
print("[INFO] loading face detector model...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"],
	"res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
print("[INFO] loading face mask detector model...")
maskNet = load_model(args["model"])

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
flag = 0
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# detect faces in the frame and determine if they are wearing a
	# face mask or not
	(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

	# loop over the detected face locations and their corresponding
	# locations
	for (box, pred) in zip(locs, preds):
		# unpack the bounding box and predictions
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred

		# determine the class label and color we'll use to draw
		# the bounding box and text
		label = "Mask" if mask > withoutMask else "No Mask"
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
			
		# include the probability in the label
		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

		# display the label and bounding box rectangle on the output
		# frame
		cv2.putText(frame, label, (startX, startY - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
		if color == (0, 0, 255):
			flag = 1
			break
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if flag == 1:
		break
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
if flag == 1:
	cv2.destroyAllWindows()
	vs.stop()
	import cv2
	import numpy as np

	faceDetect = cv2.CascadeClassifier(
		r'E:\pycharm_project\Final_year_project\face_recognization\haarcascade_frontalface_default.xml')
	cam = cv2.VideoCapture(0)
	rec = cv2.face_LBPHFaceRecognizer.create()
	rec.read(r'E:\pycharm_project\Final_year_project\face_recognization\recognizer\trainningData.yml')
	id = 0
	font = cv2.FONT_HERSHEY_SIMPLEX
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray, 1.25, 3)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
		id, conf = rec.predict(gray[y:y + h, x:x + w])
		cv2.putText(img, str(id), (x, y + h), font, 1, 255, 2)
	cv2.imshow("Face", img)
	cv2.imshow("Face", img)
	id1 = id
	print("without_mask employ = " , id1)
	cam.release()
	cv2.destroyAllWindows()
	import smtplib
	import pymysql
	conn = pymysql.connect(host='localhost', database='final_project', user='root', password='7338272260ksv')
	cursor = conn.cursor()
	str = "select * from register where id ='%d'"
	args = (id1)
	cursor.execute(str % args)
	row = cursor.fetchone()
	from email.mime.text import MIMEText
	from email.mime.image import MIMEImage
	from email.mime.multipart import MIMEMultipart

	file = 'E:\pycharm_project\Final_year_project\without_mask_image/not_mask.jpg'
	cv2.imwrite(file, img)
	ImgFileName = file
	with open(ImgFileName, 'rb') as f:
		img_data = f.read()

		msg = MIMEMultipart()
		msg['Subject'] = 'detected face with out mask'
		msg['From'] = 'mohankumarkv2016@gmail.com'
		msg['To'] = row[2]

		text = MIMEText('This is the alert mail to ware the Face mask')
		msg.attach(text)
		image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
		msg.attach(image)
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login('mohankumarkv2016@gmail.com', '7338272260ksv')
		s.sendmail(msg['From'], msg['To'], msg.as_string())
		s.quit()
	print("message with photo sended")
	os.remove(file)
	print("file deleted")
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
