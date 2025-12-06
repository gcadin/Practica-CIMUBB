import cv2
import numpy as np

def detectar_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        frame = param['frame']
        color_bgr = frame[y, x]
        color_hsv = cv2.cvtColor(np.uint8([[color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]
        print("Color (BGR) en la posición del ratón:", color_bgr)
        print("Color (HSV) en la posición del ratón:", color_hsv)

def procesar_frame(frame, verde_min, verde_max, azul_min, azul_max):
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mascara_verde = cv2.inRange(frame_hsv, verde_min, verde_max)
    mascara_azul = cv2.inRange(frame_hsv, azul_min, azul_max)
    mascara_combinada = cv2.bitwise_or(mascara_verde, mascara_azul)
    return mascara_verde, mascara_azul, mascara_combinada

def dibujar_contornos(frame, contornos, color):
    contador = 0
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 3000:
            epsilon = 0.09 * cv2.arcLength(contorno, True)
            approx = cv2.approxPolyDP(contorno, epsilon, True)
            cv2.drawContours(frame, [approx], 0, color, 3)
            contador += 1
    return contador

def main():
    cap = cv2.VideoCapture(0)

    verde_min = np.array([55, 40, 10], np.uint8)
    verde_max = np.array([90, 255, 255], np.uint8)

    azul_min = np.array([100, 80, 10], np.uint8)
    azul_max = np.array([130, 255, 255], np.uint8)

    while not cap.isOpened():
        pass

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        mascara_verde, mascara_azul, mascara_combinada = procesar_frame(frame, verde_min, verde_max, azul_min, azul_max)

        contornos_verdes, _ = cv2.findContours(mascara_verde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contador_verde = dibujar_contornos(frame, contornos_verdes, (0, 255, 0))
        
        contornos_azules, _ = cv2.findContours(mascara_azul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contador_azul = dibujar_contornos(frame, contornos_azules, (255, 0, 0))

        cv2.putText(frame, f'Contornos verdes: {contador_verde}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'Contornos azules: {contador_azul}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Original', frame)
        cv2.imshow('Mascara Verde', cv2.bitwise_and(frame, frame, mask=mascara_verde))
        cv2.imshow('Mascara Azul', cv2.bitwise_and(frame, frame, mask=mascara_azul))
        cv2.imshow('Combinado', cv2.bitwise_and(frame, frame, mask=mascara_combinada))
        
        cv2.setMouseCallback('Original', detectar_color, {'frame': frame})
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()