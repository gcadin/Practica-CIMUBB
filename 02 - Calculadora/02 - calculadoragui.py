import tkinter as tk
from tkinter import ttk
import math


class Calculadora:
    def __init__(self):
        # Variables de instancia
        self.fue_calculado = 0
        self.calculo_raiz = 0
        self.contador_parentesis = 0
        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.geometry("+500+80")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        
        # Variables de entrada
        self.entrada1 = tk.StringVar()
        self.entrada2 = tk.StringVar()
        
        # Estilos e interfaz
        self.crear_estilos()
        self.crear_interfaz()
        self.configurar_eventos()
    
    def crear_estilos(self):
        """Configura todos los estilos de la aplicación"""
        # Estilo contenedor
        self.estilo_contenedor = ttk.Style()
        self.estilo_contenedor.theme_use("clam")
        self.estilo_contenedor.configure("Contenedor.TFrame")
        
        # Estilos labels
        self.estilo_etiqueta1 = ttk.Style()
        self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 30")
        
        self.estilo_etiqueta2 = ttk.Style()
        self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 15", anchor="e")
        
        # Estilos botones numéricos
        self.estilo_botones_numeros = ttk.Style()
        self.estilo_botones_numeros.configure("Botones_numeros.TButton", 
                                             font="arial 22", width=5, 
                                             background="#FFFFFF", relief="flat")
        self.estilo_botones_numeros.map("Botones_numeros.TButton", 
                                       background=[("active", "#B9B9B9")])
        
        # Estilos botones de operaciones
        self.estilo_boton_parentesis_izq = ttk.Style()
        self.estilo_boton_parentesis_izq.configure("Boton_parentesis_izq.TButton", 
                                                   font="arial 22", width=5, 
                                                   background="#CECECE", relief="flat")
        self.estilo_boton_parentesis_izq.map("Boton_parentesis_izq.TButton", 
                                            background=[("active", "#858585")])
        
        self.estilo_boton_parentesis_der = ttk.Style()
        self.estilo_boton_parentesis_der.configure("Boton_parentesis_der.TButton", 
                                                   font="arial 22", width=5, 
                                                   background="#CECECE", relief="flat")
        self.estilo_boton_parentesis_der.map("Boton_parentesis_der.TButton", 
                                            background=[("active", "#858585")])
        
        self.estilo_boton_borrar_todo = ttk.Style()
        self.estilo_boton_borrar_todo.configure("Boton_borrar_todo.TButton", 
                                               font="arial 22", width=5, 
                                               background="#CECECE", relief="flat")
        self.estilo_boton_borrar_todo.map("Boton_borrar_todo.TButton", 
                                         foreground=[("active", "#FF0000")], 
                                         background=[("active", "#858585")])
        
        self.estilo_boton_borrar = ttk.Style()
        self.estilo_boton_borrar.configure("Boton_borrar.TButton", 
                                          font="arial 22", width=5, 
                                          background="#CECECE", relief="flat")
        self.estilo_boton_borrar.map("Boton_borrar.TButton", 
                                    foreground=[("active", "#FF0000")], 
                                    background=[("active", "#858585")])
        
        self.estilo_boton_punto = ttk.Style()
        self.estilo_boton_punto.configure("Boton_punto.TButton", 
                                         font="arial 22", width=5, 
                                         background="#CECECE", relief="flat")
        self.estilo_boton_punto.map("Boton_punto.TButton", 
                                   background=[("active", "#858585")])
        
        self.estilo_boton_raiz = ttk.Style()
        self.estilo_boton_raiz.configure("Boton_raiz.TButton", 
                                        font="arial 22", width=5, 
                                        background="#CECECE", relief="flat")
        self.estilo_boton_raiz.map("Boton_raiz.TButton", 
                                  background=[("active", "#858585")])
        
        self.estilo_boton_igual = ttk.Style()
        self.estilo_boton_igual.configure("Boton_igual.TButton", 
                                         font="arial 22", width=5, 
                                         background="#CECECE", relief="flat")
        self.estilo_boton_igual.map("Boton_igual.TButton", 
                                   background=[("active", "#858585")])
        
        self.estilo_boton_division = ttk.Style()
        self.estilo_boton_division.configure("Boton_division.TButton", 
                                            font="arial 22", width=5, 
                                            background="#CECECE", relief="flat")
        self.estilo_boton_division.map("Boton_division.TButton", 
                                      background=[("active", "#858585")])
        
        self.estilo_boton_multiplicacion = ttk.Style()
        self.estilo_boton_multiplicacion.configure("Boton_multiplicacion.TButton", 
                                                   font="arial 22", width=5, 
                                                   background="#CECECE", relief="flat")
        self.estilo_boton_multiplicacion.map("Boton_multiplicacion.TButton", 
                                            background=[("active", "#858585")])
        
        self.estilo_boton_suma = ttk.Style()
        self.estilo_boton_suma.configure("Boton_suma.TButton", 
                                        font="arial 22", width=5, 
                                        background="#CECECE", relief="flat")
        self.estilo_boton_suma.map("Boton_suma.TButton", 
                                  background=[("active", "#858585")])
        
        self.estilo_boton_resta = ttk.Style()
        self.estilo_boton_resta.configure("Boton_resta.TButton", 
                                         font="arial 22", width=5, 
                                         background="#CECECE", relief="flat")
        self.estilo_boton_resta.map("Boton_resta.TButton", 
                                   background=[("active", "#858585")])
    
    def crear_interfaz(self):
        """Crea todos los widgets de la interfaz"""
        # Crear contenedor principal
        self.contenedor = ttk.Frame(self.ventana, style="Contenedor.TFrame")
        self.contenedor.grid(column=0, row=0, sticky="nesw")
        
        # Configurar grid del contenedor
        for i in range(4):
            self.contenedor.columnconfigure(i, weight=1)
        for i in range(8):
            self.contenedor.rowconfigure(i, weight=1)
        
        # Crear etiquetas de display
        self.etiqueta1 = ttk.Label(self.contenedor, textvariable=self.entrada1, 
                                   style="Label1.TLabel")
        self.etiqueta1.grid(column=0, row=0, columnspan=4, sticky="e")
        
        self.etiqueta2 = ttk.Label(self.contenedor, textvariable=self.entrada2, 
                                   style="Label2.TLabel")
        self.etiqueta2.grid(column=0, row=1, columnspan=4, sticky="e")
        
        # Crear botones numéricos
        self.botones_numeros = []
        for i in range(10):
            boton = ttk.Button(self.contenedor, text=str(i), 
                             style="Botones_numeros.TButton",
                             command=lambda n=str(i): self.ingresar_valores(n))
            self.botones_numeros.append(boton)
        
        # Crear botones de operaciones
        self.boton_parentesis_izq = ttk.Button(self.contenedor, text="(", 
                                              style="Boton_parentesis_izq.TButton",
                                              command=lambda: self.ingresar_valores("("))
        self.boton_parentesis_der = ttk.Button(self.contenedor, text=")", 
                                              style="Boton_parentesis_der.TButton",
                                              command=lambda: self.ingresar_valores(")"))
        self.boton_borrar_todo = ttk.Button(self.contenedor, text="C", 
                                           style="Boton_borrar_todo.TButton",
                                           command=self.borrar_todo)
        self.boton_borrar = ttk.Button(self.contenedor, text=chr(9003), 
                                      style="Boton_borrar.TButton",
                                      command=self.borrar)
        self.boton_punto = ttk.Button(self.contenedor, text=".", 
                                     style="Boton_punto.TButton",
                                     command=lambda: self.ingresar_valores("."))
        self.boton_raiz = ttk.Button(self.contenedor, text="√x", 
                                    style="Boton_raiz.TButton",
                                    command=self.raiz_cuadrada)
        self.boton_igual = ttk.Button(self.contenedor, text="=", 
                                     style="Boton_igual.TButton",
                                     command=lambda: self.ingresar_valores("="))
        self.boton_division = ttk.Button(self.contenedor, text=chr(247), 
                                        style="Boton_division.TButton",
                                        command=lambda: self.ingresar_valores("/"))
        self.boton_multiplicacion = ttk.Button(self.contenedor, text="X", 
                                              style="Boton_multiplicacion.TButton",
                                              command=lambda: self.ingresar_valores("*"))
        self.boton_suma = ttk.Button(self.contenedor, text="+", 
                                    style="Boton_suma.TButton",
                                    command=lambda: self.ingresar_valores("+"))
        self.boton_resta = ttk.Button(self.contenedor, text="-", 
                                     style="Boton_resta.TButton",
                                     command=lambda: self.ingresar_valores("-"))
        
        # Posicionar botones en el grid
        self.boton_parentesis_izq.grid(column=0, row=2, sticky="nsew")
        self.boton_parentesis_der.grid(column=1, row=2, sticky="nsew")
        self.boton_borrar_todo.grid(column=2, row=2, sticky="nsew")
        self.boton_borrar.grid(column=3, row=2, sticky="nsew")
        
        self.botones_numeros[7].grid(column=0, row=3, sticky="nsew")
        self.botones_numeros[8].grid(column=1, row=3, sticky="nsew")
        self.botones_numeros[9].grid(column=2, row=3, sticky="nsew")
        self.boton_division.grid(column=3, row=3, sticky="nsew")
        
        self.botones_numeros[4].grid(column=0, row=4, sticky="nsew")
        self.botones_numeros[5].grid(column=1, row=4, sticky="nsew")
        self.botones_numeros[6].grid(column=2, row=4, sticky="nsew")
        self.boton_multiplicacion.grid(column=3, row=4, sticky="nsew")
        
        self.botones_numeros[1].grid(column=0, row=5, sticky="nsew")
        self.botones_numeros[2].grid(column=1, row=5, sticky="nsew")
        self.botones_numeros[3].grid(column=2, row=5, sticky="nsew")
        self.boton_suma.grid(column=3, row=5, sticky="nsew")
        
        self.botones_numeros[0].grid(column=0, row=6, columnspan=2, sticky="nsew")
        self.boton_punto.grid(column=2, row=6, sticky="nsew")
        self.boton_resta.grid(column=3, row=6, sticky="nsew")
        
        self.boton_igual.grid(column=0, row=7, columnspan=3, sticky="nsew")
        self.boton_raiz.grid(column=3, row=7, sticky="nsew")
        
        # Configurar padding para todos los widgets
        for child in self.contenedor.winfo_children():
            child.grid_configure(ipady=10, padx=1, pady=1)
    
    def configurar_eventos(self):
        """Configura los bindings de teclado"""
        self.ventana.bind("<KeyPress-o>", self.tema_oscuro)
        self.ventana.bind("<KeyPress-c>", self.tema_claro)
        self.ventana.bind("<Key>", self.ingresar_valores_teclado)
        self.ventana.bind("<KeyPress-b>", self.borrar)
        self.ventana.bind("<KeyPress-q>", self.borrar_todo)
    
    def tema_oscuro(self, _event=None):
        """Aplica el tema oscuro a la calculadora"""
        self.estilo_contenedor.configure("Contenedor.TFrame", background="#010924")
        
        self.estilo_etiqueta1.configure("Label1.TLabel", background="#010924", 
                                       foreground="white")
        self.estilo_etiqueta2.configure("Label2.TLabel", background="#010924", 
                                       foreground="white")
        
        self.estilo_botones_numeros.configure("Botones_numeros.TButton", 
                                             background="#00044A", foreground="white")
        self.estilo_botones_numeros.map("Botones_numeros.TButton", 
                                       background=[("active", "#020A90")])
        
        self.estilo_boton_parentesis_izq.configure("Boton_parentesis_izq.TButton", 
                                                   background="#010924", foreground="white")
        self.estilo_boton_parentesis_izq.map("Boton_parentesis_izq.TButton", 
                                            background=[("active", "#000AB1")])
        
        self.estilo_boton_parentesis_der.configure("Boton_parentesis_der.TButton", 
                                                   background="#010924", foreground="white")
        self.estilo_boton_parentesis_der.map("Boton_parentesis_der.TButton", 
                                            background=[("active", "#000AB1")])
        
        self.estilo_boton_borrar_todo.configure("Boton_borrar_todo.TButton", 
                                               background="#010924", foreground="white")
        self.estilo_boton_borrar_todo.map("Boton_borrar_todo.TButton", 
                                         background=[("active", "#000AB1")])
        
        self.estilo_boton_borrar.configure("Boton_borrar.TButton", 
                                          background="#010924", foreground="white")
        self.estilo_boton_borrar.map("Boton_borrar.TButton", 
                                    background=[("active", "#000AB1")])
        
        self.estilo_boton_division.configure("Boton_division.TButton", 
                                            background="#010924", foreground="white")
        self.estilo_boton_division.map("Boton_division.TButton", 
                                      background=[("active", "#000AB1")])
        
        self.estilo_boton_multiplicacion.configure("Boton_multiplicacion.TButton", 
                                                   background="#010924", foreground="white")
        self.estilo_boton_multiplicacion.map("Boton_multiplicacion.TButton", 
                                            background=[("active", "#000AB1")])
        
        self.estilo_boton_suma.configure("Boton_suma.TButton", 
                                        background="#010924", foreground="white")
        self.estilo_boton_suma.map("Boton_suma.TButton", 
                                  background=[("active", "#000AB1")])
        
        self.estilo_boton_resta.configure("Boton_resta.TButton", 
                                         background="#010924", foreground="white")
        self.estilo_boton_resta.map("Boton_resta.TButton", 
                                   background=[("active", "#000AB1")])
        
        self.estilo_boton_punto.configure("Boton_punto.TButton", 
                                         background="#010924", foreground="white")
        self.estilo_boton_punto.map("Boton_punto.TButton", 
                                   background=[("active", "#000AB1")])
        
        self.estilo_boton_raiz.configure("Boton_raiz.TButton", 
                                        background="#010924", foreground="white")
        self.estilo_boton_raiz.map("Boton_raiz.TButton", 
                                  background=[("active", "#000AB1")])
        
        self.estilo_boton_igual.configure("Boton_igual.TButton", 
                                         background="#010924", foreground="white")
        self.estilo_boton_igual.map("Boton_igual.TButton", 
                                   background=[("active", "#000AB1")])
    
    def tema_claro(self, _event=None):
        """Aplica el tema claro a la calculadora"""
        self.estilo_contenedor.configure("Contenedor.TFrame", background="#DBDBDB")
        
        self.estilo_etiqueta1.configure("Label1.TLabel", background="#DBDBDB", 
                                       foreground="black")
        self.estilo_etiqueta2.configure("Label2.TLabel", background="#DBDBDB", 
                                       foreground="black")
        
        self.estilo_botones_numeros.configure("Botones_numeros.TButton", 
                                             background="#FFFFFF", foreground="black")
        self.estilo_botones_numeros.map("Botones_numeros.TButton", 
                                       background=[("active", "#B9B9B9")])
        
        self.estilo_boton_borrar_todo.configure("Boton_borrar_todo.TButton", 
                                               background="#CECECE", foreground="black")
        self.estilo_boton_borrar_todo.map("Boton_borrar_todo.TButton", 
                                         background=[("active", "#858585")])
        
        self.estilo_boton_borrar.configure("Boton_borrar.TButton", 
                                          background="#CECECE", foreground="black")
        self.estilo_boton_borrar.map("Boton_borrar.TButton", 
                                    background=[("active", "#858585")])
        
        self.estilo_boton_parentesis_izq.configure("Boton_parentesis_izq.TButton", 
                                                   background="#CECECE", foreground="black")
        self.estilo_boton_parentesis_izq.map("Boton_parentesis_izq.TButton", 
                                            background=[("active", "#858585")])
        
        self.estilo_boton_parentesis_der.configure("Boton_parentesis_der.TButton", 
                                                   background="#CECECE", foreground="black")
        self.estilo_boton_parentesis_der.map("Boton_parentesis_der.TButton", 
                                            background=[("active", "#858585")])
        
        self.estilo_boton_punto.configure("Boton_punto.TButton", 
                                         background="#CECECE", foreground="black")
        self.estilo_boton_punto.map("Boton_punto.TButton", 
                                   background=[("active", "#858585")])
        
        self.estilo_boton_raiz.configure("Boton_raiz.TButton", 
                                        background="#CECECE", foreground="black")
        self.estilo_boton_raiz.map("Boton_raiz.TButton", 
                                  background=[("active", "#858585")])
        
        self.estilo_boton_igual.configure("Boton_igual.TButton", 
                                         background="#CECECE", foreground="black")
        self.estilo_boton_igual.map("Boton_igual.TButton", 
                                   background=[("active", "#858585")])
        
        self.estilo_boton_division.configure("Boton_division.TButton", 
                                            background="#CECECE", foreground="black")
        self.estilo_boton_division.map("Boton_division.TButton", 
                                      background=[("active", "#858585")])
        
        self.estilo_boton_multiplicacion.configure("Boton_multiplicacion.TButton", 
                                                   background="#CECECE", foreground="black")
        self.estilo_boton_multiplicacion.map("Boton_multiplicacion.TButton", 
                                            background=[("active", "#858585")])
        
        self.estilo_boton_suma.configure("Boton_suma.TButton", 
                                        background="#CECECE", foreground="black")
        self.estilo_boton_suma.map("Boton_suma.TButton", 
                                  background=[("active", "#858585")])
        
        self.estilo_boton_resta.configure("Boton_resta.TButton", 
                                         background="#CECECE", foreground="black")
        self.estilo_boton_resta.map("Boton_resta.TButton", 
                                   background=[("active", "#858585")])
    
    def ingresar_valores(self, tecla):
        """Procesa la entrada de valores desde los botones"""
        if self.fue_calculado == 1:
            if tecla.isdigit():
                self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 30")
                self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 15")
                self.entrada1.set(tecla)
                try:
                    self.entrada2.set("= " + str(eval(self.entrada1.get())))
                except ZeroDivisionError:
                    self.entrada2.set("Error division por 0")
                except SyntaxError:
                    self.entrada2.set("Error de sintaxis")
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla in ["+", "-", "*", "/"]:
                if len(self.entrada1.get()) == 0:
                    self.entrada1.set(tecla)
                else:
                    if self.calculo_raiz == 1:
                        self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 30")
                        self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 15")
                        self.entrada1.set(self.entrada2.get() + tecla)
                        expresion = self.entrada1.get()[:-1]
                        for _ in range(self.contador_parentesis):
                            expresion = expresion + ")"
                        try:
                            self.entrada2.set("= " + str(eval(expresion)))
                        except ZeroDivisionError:
                            self.entrada2.set("Error division por 0")
                        except SyntaxError:
                            self.entrada2.set("Error de sintaxis")
                    else:
                        self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 30")
                        self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 15")
                        try:
                            resultado = eval(self.entrada1.get())
                            self.entrada1.set(self.entrada2.get()[1:] + tecla)
                            self.entrada2.set("= " + str(resultado))
                        except ZeroDivisionError:
                            self.entrada2.set("Error division por 0")
                        except SyntaxError:
                            self.entrada2.set("Error de sintaxis")
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == ".":
                if self.calculo_raiz == 1 or self.fue_calculado == 1:
                    self.entrada1.set(tecla)
                else:
                    self.entrada1.set(self.entrada1.get() + tecla)
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == "(":
                if self.calculo_raiz == 1 or self.fue_calculado == 1:
                    self.entrada1.set(tecla)
                else:
                    if len(self.entrada1.get()) == 0:
                        self.entrada1.set(tecla)
                    elif self.entrada1.get()[-1] not in ["*", "/", "+", "-"]:
                        self.entrada1.set(self.entrada1.get() + "*" + tecla)
                    else:
                        self.entrada1.set(self.entrada1.get() + tecla)
                self.contador_parentesis += 1
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == ")":
                self.entrada1.set(self.entrada1.get() + tecla)
                self.contador_parentesis -= 1
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == "=":
                self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 15")
                self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 30")
                try:
                    resultado = eval(self.entrada1.get())
                    self.entrada2.set("= " + str(resultado))
                except ZeroDivisionError:
                    self.entrada2.set("Error division por 0")
                except SyntaxError:
                    self.entrada2.set("Error de sintaxis")
                self.fue_calculado = 1
                self.calculo_raiz = 0
        else:
            if tecla.isdigit():
                self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 30")
                self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 15")
                self.entrada1.set(self.entrada1.get() + tecla)
                expresion = self.entrada1.get()
                for _ in range(self.contador_parentesis):
                    expresion = expresion + ")"
                try:
                    self.entrada2.set("= " + str(eval(expresion)))
                except ZeroDivisionError:
                    self.entrada2.set("Error division por 0")
                except SyntaxError:
                    self.entrada2.set("Error de sintaxis")
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla in ["+", "-", "*", "/"]:
                if len(self.entrada1.get()) == 0:
                    self.entrada1.set(tecla)
                else:
                    self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 30")
                    self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 15")
                    expresion = self.entrada1.get()
                    for _ in range(self.contador_parentesis):
                        expresion = expresion + ")"
                    try:
                        resultado = eval(expresion)
                        self.entrada1.set(self.entrada1.get() + tecla)
                        self.entrada2.set("= " + str(resultado))
                    except ZeroDivisionError:
                        self.entrada2.set("Error division por 0")
                    except SyntaxError:
                        self.entrada2.set("Error de sintaxis")
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == ".":
                if self.calculo_raiz == 1 or self.fue_calculado == 1:
                    self.entrada1.set(tecla)
                else:
                    self.entrada1.set(self.entrada1.get() + tecla)
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == "(":
                if self.calculo_raiz == 1 or self.fue_calculado == 1:
                    self.entrada1.set(tecla)
                else:
                    if len(self.entrada1.get()) == 0:
                        self.entrada1.set(tecla)
                    elif self.entrada1.get()[-1] not in ["*", "/", "+", "-"]:
                        self.entrada1.set(self.entrada1.get() + "*" + tecla)
                    else:
                        self.entrada1.set(self.entrada1.get() + tecla)
                self.contador_parentesis += 1
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == ")":
                self.entrada1.set(self.entrada1.get() + tecla)
                self.contador_parentesis -= 1
                self.fue_calculado = 0
                self.calculo_raiz = 0
            elif tecla == "=":
                self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 15")
                self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 30")
                try:
                    resultado = eval(self.entrada1.get())
                    self.entrada2.set("= " + str(resultado))
                except ZeroDivisionError:
                    self.entrada2.set("Error division por 0")
                except SyntaxError:
                    self.entrada2.set("Error de sintaxis")
                self.fue_calculado = 1
                self.calculo_raiz = 0
    
    def ingresar_valores_teclado(self, event):
        """Procesa la entrada de valores desde el teclado"""
        tecla = event.char
        if tecla in "0123456789+-*/.()=":
            self.ingresar_valores(tecla)
    
    def raiz_cuadrada(self):
        """Calcula la raíz cuadrada del valor actual"""
        self.estilo_etiqueta1.configure("Label1.TLabel", font="arial 15")
        self.estilo_etiqueta2.configure("Label2.TLabel", font="arial 30")
        self.entrada1.set("raiz(" + self.entrada2.get()[2:] + ")")
        resultado = math.sqrt(float(self.entrada2.get()[2:]))
        self.entrada2.set(str(resultado))
        self.calculo_raiz = 1
        self.fue_calculado = 1
    
    def borrar(self, _event=None):
        """Borra el último carácter ingresado"""
        if len(self.entrada1.get()) > 0:
            if self.entrada1.get()[-1] == ")":
                self.contador_parentesis += 1
            elif self.entrada1.get()[-1] == "(":
                self.contador_parentesis -= 1
            self.entrada1.set(self.entrada1.get()[:-1])
    
    def borrar_todo(self, _event=None):
        """Limpia todos los valores"""
        self.entrada1.set("")
        self.entrada2.set("")
        self.contador_parentesis = 0
        self.fue_calculado = 0
        self.calculo_raiz = 0
    
    def ejecutar(self):
        """Inicia el loop principal de la aplicación"""
        self.ventana.mainloop()


if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.ejecutar()
