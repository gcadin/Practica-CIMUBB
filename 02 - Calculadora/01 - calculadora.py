#Calculadora sin GUI que nos permita realizar ciertas operaciones básicas con números

import time

#Función que suma dos numeros
def suma(numero1, numero2):
    return numero1+numero2

#Función que resta dos numeros
def resta(numero1, numero2):
    return numero1-numero2

#Función que multiplica dos numeros
def multiplicacion(numero1, numero2):
    return numero1*numero2

#Función que divide dos numeros
def division(numero1, numero2):
    return numero1/numero2

#Función que comprueba si una variable puede convertirse en una variable numerica del tipo FLOAT
def es_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

#Segmento principalde código main
if __name__ == "__main__":
    eleccion = 0
    flag = 0
    while(eleccion not in [1,2,3,4]):
        print("\nCalculadora básica\n"
              "1.- SUMA\n"
              "2.- RESTA\n"
              "3.- MULTIPLICACIÓN\n"
              "4.- DIVISIÓN")
        eleccion = input("Ingrese la opcion deseada: ")
        print("\n")
        #Validamos que sea un numero y que sea un numero (opcion) valida
        if(es_numero(eleccion)):
            eleccion = float(eleccion)
            if(eleccion not in [1,2,3,4]):
                print("La opción ingresada no es válida")
                time.sleep(2)
        else:
            print("La opcion ingresada debe ser un valor numerico")
            time.sleep(2)
            eleccion = 0
        
    if(eleccion == 1):
        while(flag == 0):
            print("Ingrese los numeros que desea sumar")
            numero1 = input("Número 1: ")
            numero2 = input("Número 2: ")
            if(es_numero(numero1) and es_numero(numero2)):
                numero1 = float(numero1)
                numero2 = float(numero2)
                flag = 1
            else:
                print("Los valores ingresados deben ser numericos\nIntente nuevamente\n")
                time.sleep(2)

        resultado = suma(numero1, numero2)
        print("El resultado de la operación es: ", resultado)
        print("\n")

    if(eleccion == 2):
        while(flag == 0):
            print("Ingrese los numeros que desea restar")
            numero1 = input("Número 1: ")
            numero2 = input("Número 2: ")
            if( es_numero(numero1) and es_numero(numero2)):
                numero1 = float(numero1)
                numero2 = float(numero2)
                flag = 1
            else:
                print("Los valores ingresados deben ser numericos\nIntente nuevamente\n")
                time.sleep(2)
            
        resultado= resta(numero1, numero2)
        print("El resultado de la operación es: ", resultado)
        print("\n")

    if(eleccion == 3):
        while(flag == 0):
            print("Ingrese los numeros que desea multiplicar")
            numero1 = input("Número 1: ")
            numero2 = input("Número 2: ")
            if( es_numero(numero1) and es_numero(numero2)):
                numero1 = float(numero1)
                numero2 = float(numero2)
                flag = 1
            else:
                print("Los valores ingresados deben ser numericos\nIntente nuevamente\n")
                time.sleep(2)

        resultado= multiplicacion(numero1, numero2)
        print("El resultado de la operación es: ", resultado)
        print("\n")

    if(eleccion == 4):
        while(flag == 0):
            print("Ingrese los numeros que desea dividir")
            numero1 = input("Numerador: ")
            numero2 = input("Denominador: ")
            if( es_numero(numero1) and es_numero(numero2)):
                numero1 = float(numero1)
                numero2 = float(numero2)
                if(numero2 != 0):
                    flag = 1
                else:
                    print("El denominador debe ser distinto de 0")
                    time.sleep(2)
            else:
                print("Los valores ingresados deben ser numericos\nIntente nuevamente\n")
                time.sleep(2)

        resultado = division(numero1, numero2)
        print("El resultado de la operación es: ", resultado)
        print("\n")