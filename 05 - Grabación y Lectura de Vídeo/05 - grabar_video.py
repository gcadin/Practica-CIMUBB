import cv2
captura = cv2.VideoCapture(0) #Con "0" se indica el dispositivo para capturar el video
salida = cv2.VideoWriter("video_salida.avi", cv2.VideoWriter_fourcc(*"XVID"), 30, (640,480))

while(captura.isOpened()):
    ret, imagen = captura.read() #Utilizaremos ret para determinar si la imagen si puede leer
    if ret == True:
        cv2.imshow("Video", imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord("s"): #0xFF es para indicar SO de 64 bits, con ord("s) indicamos la tecla esperada")
            break
salida.release()
captura.release()
cv2.destroyAllWindows()