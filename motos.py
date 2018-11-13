#importa a bliblioteca python opencv
import cv2
import numpy as np

#abreo video
cap = cv2.VideoCapture('moto.avi')
#usamos aqui o xml de treinamento moto
moto_cascade = cv2.CascadeClassifier('moto.xml')

#exibe  ate  o fim do video
while True:
    #captura quadro a quadro
    ret, frame = cap.read()
    #converte o video em escala de cinza a cada quadro
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #aqui as  motos sao detectas
    motos = moto_cascade.detectMultiScale(gray, 1.1,1 )

    #desenha em volta da moto
    for (x,y,w,h) in motos:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)      

    #exibe  o resultado
    cv2.imshow('video', frame)
    #pressionar E pra sair
    if cv2.waitKey(25) & 0xFF == ord('e'):
        break

cap.release()

cv2.destroyAllWindows()
