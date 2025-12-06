import cv2
import numpy as np

#Inicializa un array con dimensión de 300x300 con 3 canales de colores
bgr = np.zeros((300,300,3), dtype = np.uint8)

#Modificando los valores en la matriz se modificaran los colores
#correspondientes en los canales, formando colores compuestos
bgr[:,:,:] = (255,0,0)
cv2.imshow("BGR", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()