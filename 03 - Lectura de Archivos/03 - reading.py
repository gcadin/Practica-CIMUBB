import cv2
imagen = cv2.imread("imagen_reading.jfif", 0) #Con el segundo argumento indicamos si la imagen se lee en escala de grises indicando un 0 o en color con un 1
cv2.imshow("Prueba de imagen", imagen)
cv2.imwrite("imagen_gris.jpg", imagen)
cv2.waitKey(0) #con waitKey(0) se espera a que el usuario presione una tecla
cv2.destroyAllWindows()