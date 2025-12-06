import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Definir los rangos de color para verde en formato HSV
verde_min = np.array([45, 40, 10], np.uint8)
verde_max = np.array([70, 255, 255], np.uint8)

azul_min = np.array([100,40,10], np.uint8)
azul_max = np.array([130,255,255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        # Convertir el frame a espacio de color HSV
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Crear una máscara para detectar el color verde
        mascara_verde = cv2.inRange(frameHSV, verde_min, verde_max)
        mascara_azul = cv2.inRange(frameHSV, azul_min, azul_max)
        mascara_combinada = cv2.bitwise_or(mascara_verde, mascara_azul)

        # Aplicar la máscara a la imagen original
        # Toma la imagen de la camara y realiza la operación con la misma imagen, utilizando la 
        # mascara que indica el color verde encontrado en la imagen
        frame_mascara_verde = cv2.bitwise_and(frame, frame, mask = mascara_verde)
        frame_mascara_azul = cv2.bitwise_and(frame, frame, mask = mascara_azul)
        frame_resultante = cv2.bitwise_and(frame, frame, mask = mascara_combinada)

        # Mostrar los resultados
        cv2.imshow('Original', frame)
        cv2.imshow('Mascara Verde', frame_mascara_verde)
        cv2.imshow('Mascara Azul', frame_mascara_azul)
        cv2.imshow('Combinado', frame_resultante)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()