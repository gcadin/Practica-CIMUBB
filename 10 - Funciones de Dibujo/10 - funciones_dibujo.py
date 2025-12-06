import cv2
import numpy as np

imagen = 255*np.ones((480,640,3),dtype=np.uint8)

#Dibujando lineas
cv2.line(imagen,(320,0),(320,240),(0,0,0),4)
cv2.line(imagen,(0,240),(640,240),(255,0,0),6)

#Dibujando cuadrilateros
cv2.rectangle(imagen, (290,210), (350,270), (0,0,255), 3)
cv2.rectangle(imagen, (50,50), (270,190), (0,255,0), -1)

#Dibujando circulos
cv2.circle(imagen, (480, 120), 50, (0,0,0), -1)

#Dibujando texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'Texto HERSHEY SIMPLEX',(50,320),font,1,(70,20,195),2)
cv2.putText(imagen,'Texto HERSHEY PLAIN',(50,345),1,1,(255,0,0),2)
cv2.putText(imagen,'Texto HERSHEY TRIPLEX',(50,375),4,1,(255,0,0),2)
cv2.putText(imagen,'Texto HERSHEY SCRIPT SIMPLEX',(50,410),6,1,(255,0,0),2)

cv2.imshow('imagen',imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()