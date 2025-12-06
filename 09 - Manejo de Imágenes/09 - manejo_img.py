import cv2
import numpy as np
import imutils

imagen = cv2.imread("pudu.jpg")
ancho = imagen.shape[1] #columnas
alto = imagen.shape[0] # filas

# Traslación
M = np.float32([[1,0,100],[0,1,150]])
img_traslacion = cv2.warpAffine(imagen,M,(ancho,alto))

# Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),15,1)
img_rotacion = cv2.warpAffine(imagen,M,(ancho,alto))

# Escalado con cv2
img_escalado = cv2.resize(imagen, (600,300), interpolation = cv2.INTER_CUBIC)

# Escalado con imutils
img_escalado_imutils = imutils.resize(imagen, width = 300)

# Recorte
img_recortada = imagen[80:280,140:300]

cv2.imshow("Imagen", imagen)
cv2.imshow("Traslacion", img_traslacion)
cv2.imshow("Rotacion", img_rotacion)
cv2.imshow("Escalado cv2", img_escalado)
cv2.imshow("Escalado imutils", img_escalado_imutils)
cv2.imshow("Recortada", img_recortada)
cv2.waitKey(0)
cv2.destroyAllWindows()