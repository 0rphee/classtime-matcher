# Generador de archivo intermedio (Lectura de Datos)

#materia,profesor,clave,lunes,martes,jueves,viernes,sabado,domingo
#comerialización,alan,01,11:30-13:00,NULL,15:30-17:00,NULL,NULL,NULL,NULL

import os
# Menu

materialist = [["Materia", "Profesor", "Clave", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]]

opcion = 0
val = -1
validacion = "S"

while(opcion != 3):

    #Borrar pantalla
    os.system("cls")

    print("Bienvenido al generador de archivo intermedio\n")
    print("1- Ingresar Materias")
    print("2- Generar Archivo Intermedio")
    print("3- Salir")

    opcion = int(input("Ingrese una opcion: "))

    if(opcion == 1):
        #Borrar pantalla
        os.system("cls")

        print("Ingrese la informacion de las materias\n")
        #Se ingresa la informacion de las materias
        validacion = "S"
        while(validacion == "S"):
            #Añadir materia
            temp_list = []
            temp_list.append(input("\nIngrese el nombre de la materia: "))
            temp_list.append(input("Ingrese el nombre del profesor: "))
            temp_list.append(input("Ingrese la clave de la materia: "))
            print('\nIngrese el horario de la materia ( 00:00-00:00 || NULL )\n')
            temp_list.append(input("Lunes: "))
            temp_list.append(input("Martes: "))
            temp_list.append(input("Miercoles: "))
            temp_list.append(input("Jueves: "))
            temp_list.append(input("Viernes: "))
            temp_list.append(input("Sabado: "))
            temp_list.append(input("Domingo: "))
            materialist.append(temp_list)
            print("\nMateria añadida con exito")
            val = 1

            #Coninuar añaadiendo materias
            print("\nDesea añadir otra materia? (S/N) ")
            if(input().upper == "S"):
                validacion = "S"
            else:
                validacion = "N"
                continue
    

    elif(opcion == 2):
        if(val == -1):
            print("No se han ingresado materias")
            os.system("pause")
            continue
        else:
            print("Generando archivo intermedio...")
            #Generar archivo intermedio
            #Abrir archivo
            f = open("Intermedio.txt", "w")
            #Escribir en el archivo
            for i in range(len(materialist)):
                for j in range(10):
                    f.write(materialist[i][j])
                    f.write(",")
                f.write("\n")
            os.system("pause")
            continue
        

    elif(opcion == 3):
        print("Gracias por usar el generador de archivo intermedio")
        os.system("pause")
        exit()

    else:
        print("Opcion invalida")
        os.system("pause")
        continue
    
