# Generador de archivo intermedio (Lectura de Datos)
import os
# Menu

materialist = {}

while(opcion != (1 or 2)):

    #Borrar pantalla
    os.system("cls")

    print("Bienvenido al generador de archivo intermedio\n")
    print("1- Ingresar Materias")
    print("2- Salir")

    opcion = int(input("Ingrese una opcion: "))

    if(opcion == 1):
        print("Ingrese la informacion de las materias\n")
        #Se ingresa la informacion de las materias y se guarda en un diccionario que se guardara en un archivo csv
        while(True):
            i =+ 1
            materialist[f"M {i}"]["Nombre"] = input("Ingrese el nombre de la materia: ")

    elif(opcion == 2):
        print("Gracias por usar el generador de archivo intermedio")
        exit()

    else:
        print("Opcion invalida")
        exit()
