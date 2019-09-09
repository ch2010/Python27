import cv2,os #opencv
import numpy as np # manipula a matriz
from PIL import Image # transformar o arquivo de imagem em matriz

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-30,y-30),(x+w+30,y+h+30),(148,0,211),2)

         
        
        if(nbr_predicted==1):
              nbr_predicted='Rocha'
        elif(nbr_predicted==2):
              nbr_predicted='Framil'
        if (conf > 82.000) :        
         cv2.cv.PutText(cv2.cv.fromarray(im),str(nbr_predicted)+"--"+str(conf), (x,y+h),font, 240) #Draw the text
         cv2.imshow('Face Detection',im)
    cv2.waitKey(10)









