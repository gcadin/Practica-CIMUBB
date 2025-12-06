import tkinter as tk
import imutils
import cv2
from PIL import Image, ImageTk

def iniciar():
    ret, frame = capture.read()
    if ret:
        frame = imutils.resize(frame, width=311, height=241)
        imagen_camera = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imagen_camera)
        img = ImageTk.PhotoImage(image=im)
        LImagen.configure(image=img)
        LImagen.image = img
        LImagen.after(0, iniciar) 

def camara():
    global capture
    try:
        capture = cv2.VideoCapture(0)
        if capture is not None and capture.isOpened():
            iniciar()
        else:
            print("No se pudo iniciar la cámara.")
    except Exception as e:
        print("Error al iniciar la cámara:", e)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("400x370")
    ventana.resizable(0, 0)
    ventana.title("Iniciar webcam")

    capture = None

    # Botones
    BCamara = tk.Button(ventana, text="Iniciar cámara", command=camara)
    BCamara.place(x=150, y=330, width=120, height=23)

    # Etiqueta para la imagen
    LImagen = tk.Label(ventana, background = "gray")
    LImagen.place( x = 50, y = 50, width = 300, height = 240)

    ventana.mainloop()