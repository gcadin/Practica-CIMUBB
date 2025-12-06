# Tutoriales de Procesamiento de Imágenes y Reconocimiento Facial

Repositorio con tutoriales progresivos de Python enfocados en procesamiento de imágenes, visión por computadora y reconocimiento facial utilizando OpenCV.

## Descripción

Este proyecto contiene una colección de tutoriales prácticos que van desde los conceptos básicos de Python hasta la implementación de sistemas de reconocimiento facial con interfaces gráficas. Cada tutorial está diseñado para construir sobre los conocimientos previos, proporcionando una ruta de aprendizaje completa.

## Requisitos

- Python 3.x
- OpenCV (cv2)
- NumPy
- Tkinter (incluido con Python)

### Instalación de dependencias

```bash
pip install opencv-python numpy
```

## Estructura del Proyecto

### Tutoriales Básicos

- **00 - Instalación de Python**: Guía de instalación de Visual Studio Code y Python
- **01 - Hola Mundo**: Introducción básica a Python
- **02 - Calculadora**: Implementación de calculadora básica y con GUI
- **03 - Lectura de Archivos**: Manejo de archivos en Python

### Procesamiento de Imágenes y Vídeo

- **04 - Webcam**: Captura de vídeo desde la webcam
- **05 - Grabación y Lectura de Vídeo**: Guardar y reproducir archivos de vídeo
- **06 - npRGB**: Trabajo con arrays NumPy y canales RGB
- **07 - Thresholding**: Técnicas de umbralización de imágenes
- **08 - Edición de Imagen**: Operaciones de suma y resta de imágenes
- **09 - Manejo de Imágenes**: Manipulación avanzada de imágenes

### Procesamiento Avanzado

- **10 - Funciones de Dibujo**: Dibujar formas y texto en imágenes
- **11 - Contornos en Imágenes**: Detección y trazado de contornos
- **12 - Detección de Colores**: Identificación de colores específicos
- **13 - Detección de Movimiento**: Detección de objetos en movimiento

### Reconocimiento Facial

- **14 - Detección de Rostros**: Detección de rostros en imágenes y vídeo
- **15 - Almacenamiento de Rostros**: Captura y almacenamiento de datos faciales
- **16 - Reconocimiento Facial**: Implementación de sistema de reconocimiento

### Interfaces Gráficas

- **17 - GUI Tkinter Imagen**: Interfaz gráfica para procesamiento de imágenes
- **18 - GUI Tkinter Vídeos**: Interfaz gráfica para procesamiento de vídeo
- **19 - GUI Tkinter Reconocimiento Facial**: Sistema completo con GUI

## Uso

Cada carpeta contiene los archivos Python correspondientes al tutorial. Para ejecutar un tutorial:

```bash
python "ruta/al/tutorial.py"
```

### Ejemplo

```bash
python "01 - Hola Mundo/tutorial_00_hola_mundo.py"
```

## Contenido por Tutorial

### Tutorial 01: Hola Mundo
Introducción básica a Python con impresión de texto en consola.

### Tutorial 04: Webcam
Captura de vídeo en tiempo real desde la cámara web utilizando OpenCV.

### Tutorial 07: Thresholding
Aplicación de técnicas de umbralización para segmentación de imágenes.

### Tutorial 11: Contornos
Detección y visualización de contornos en imágenes para identificación de objetos.

### Tutorial 14: Detección de Rostros
Implementación de detección facial usando clasificadores Haar Cascade en imágenes y vídeo en tiempo real.

### Tutorial 16: Reconocimiento Facial
Sistema completo de reconocimiento facial capaz de identificar personas previamente registradas.

### Tutorial 19: GUI Reconocimiento Facial
Aplicación con interfaz gráfica completa que integra todas las funcionalidades de reconocimiento facial.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **OpenCV**: Biblioteca de visión por computadora
- **NumPy**: Procesamiento numérico y manipulación de arrays
- **Tkinter**: Creación de interfaces gráficas

## Recursos Adicionales

El repositorio incluye imágenes de prueba y ejemplos para practicar con los diferentes tutoriales.

## Notas

- Asegúrate de tener una cámara web conectada para los tutoriales que requieren captura de vídeo
- Algunos tutoriales requieren imágenes de entrada que se encuentran en el directorio raíz
- Los clasificadores Haar Cascade para detección facial se obtienen de la instalación de OpenCV

## Contribuciones

Este es un proyecto educativo. Si encuentras errores o tienes sugerencias de mejora, no dudes en contribuir.

## Licencia

Proyecto con fines educativos.
