import cv2
captura = cv2.VideoCapture("video_salida.avi") #Con "nombre_video" se indica el nombre dle video a leer

while(captura.isOpened()):
    ret, imagen = captura.read() #Utilizaremos ret para determinar si la imagen si puede leer
    if ret == True:
        cv2.imshow("Video", imagen)
        if cv2.waitKey(30) & 0xFF == ord("s"): #0xFF es para indicar SO de 64 bits, con ord("s) indicamos la tecla esperada")
            break
    else: break
captura.release()
cv2.destroyAllWindows()