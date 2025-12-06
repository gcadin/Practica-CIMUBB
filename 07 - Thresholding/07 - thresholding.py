import cv2
import numpy as np
import imutils

imagen = cv2.imread("img_thresholding.jpg", 1)
imagen = 255 - imagen
imagen = imutils.resize(imagen, width=400)#Se puede omitir esta línea
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


_, binarizada = cv2.threshold(imagen_gris, 120, 255, cv2.THRESH_BINARY)
_, binarizadaInv = cv2.threshold(imagen_gris, 120, 255, cv2.THRESH_BINARY_INV)
_, trunc = cv2.threshold(imagen_gris, 120, 255, cv2.THRESH_TRUNC)
_, to_zero = cv2.threshold(imagen_gris, 120, 255, cv2.THRESH_TOZERO)
_, to_zero_inv = cv2.threshold(imagen_gris, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Original", imagen)
cv2.imshow("Gris", imagen_gris)
cv2.imshow("Thresholding Binary",binarizada)
cv2.imshow("Thresholding Binary Inverted", binarizadaInv)
cv2.imshow("Thresholding Truncate", trunc)
cv2.imshow("Thresholding To Zero", to_zero)
cv2.imshow("Thresholding To Zero Inverted", to_zero_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()