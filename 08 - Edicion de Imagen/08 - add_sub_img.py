# Podemos agregar tecla para cerrar todas las ventanas
import cv2

imagen1 = cv2.imread("lapiz.jpg", 0)
imagen2 = cv2.imread("cuerda.jpg", 0)

resultado_add = cv2.add(imagen1, imagen2)
resultado_addw = cv2.addWeighted(imagen1, 0.5, imagen2, 0.5, 0)
resultado_sub = cv2.subtract(imagen1,imagen2)
resultado_absdiff = cv2.absdiff(imagen1,imagen2)

print("Matriz imagen1\n")
print (imagen1[0:3,0:3])

print("\nMatriz imagen2\n")
print (imagen2[0:3,0:3])

print("\nMatriz resultado_add\n")
print (resultado_add[0:3,0:3])

print("\nMatriz addWeighted\n")
print (resultado_addw[0:3,0:3])

print("\nMatriz sub\n")
print (resultado_sub[0:3,0:3])

print("\nMatriz absdiff\n")
print (resultado_absdiff[0:3, 0:3])

cv2.imshow("Resultado add", resultado_add)
cv2.imshow("Resultado addWeighted", resultado_addw)
cv2.imshow("Resultado sub", resultado_sub)
cv2.imshow("Resultado absdiff", resultado_absdiff)
cv2.imshow("Imagen 1",imagen1)
cv2.imshow("imagen 2", imagen2)

cv2.waitKey(0)
cv2.destroyAllWindows()