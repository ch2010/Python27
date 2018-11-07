import cv2
import numpy
 
cam = cv2.VideoCapture(0)#Captura por camera
kernel = numpy.ones((5 ,5), numpy.uint8)

#A ideia é simples. Vamos criar uma máscara.
#Nossa máscara é uma imagem em preto e branco onde cada pixel azul se transformará em um branco e o restantes dos pixels será preto.

 
while (True):
    ret, frame = cam.read()
    rangomax = numpy.array([255, 50, 50]) # B, G, R
    rangomin = numpy.array([51, 0, 0])
    mask = cv2.inRange(frame, rangomin, rangomax)
   
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
 
    x, y, w, h = cv2.boundingRect(opening)
 
     

    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)    
    #cv2.circle(frame, (x+w/2, y+h/2), 5, (0, 0, 255), -1)

    (b, g, r) = frame[200, 200]
     
    #frame[598:402, 598:402] 
    frame[10:90, 10:90] = (rangomax)  #Colocamos a cor  desejada  no canto da tela
    
    cv2.imshow('frame',opening)
    
    cv2.imshow('camera', frame)
 
    k = cv2.waitKey(1) & 0xFF
 
    if k == 27:
        break
