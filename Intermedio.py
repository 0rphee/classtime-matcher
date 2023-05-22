# Generador de archivo intermedio (Lectura de Datos)

#materia,profesor,clave,lunes,martes,jueves,viernes,sabado,domingo
#comerialización,alan,01,11:30-13:00,NULL,15:30-17:00,NULL,NULL,NULL,NULL

import sys
import os
import main
import re

# Metodos
time_pattern = re.compile(r'^\d{2}:\d{2}-\d{2}:\d{2}$')
days_of_week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def validate_time_input(day):
    while True:
        time_input = input(day + ": ")
        if time_input.upper() == "NULL":
            return time_input
        elif time_pattern.match(time_input):
            return time_input
        else:
            print("Formato de tiempo inválido. Intente nuevamente.")

def escribir_archivo(lista):
    #Abrir archivo csv
    with open("intermedio.csv", "a") as f:
        #Escribir en el archivo csv
        for i, elemento in enumerate(lista):
            # separar elementos de la lista por comas excepto el ultimo
            f.write(elemento)
            if i != len(lista) - 1:
                f.write(",")
        f.write("\n")
        #Cerrar archivo csv
    print(f"\nMateria {lista[2]} añadida con exito")

# Menu
def ingreso_materias():
    materialist = []

    opcion = 0
    val = -1

    while(opcion != 3):

        #Borrar pantalla
        if sys.platform == "win32":
            os.system("cls")

        print("""Bienvenido a ClasstimeMatcher\n
Con este programa podrás validar las materias que cursarás en tu 
próximo semestre. Ingresa todas las clases que te interesen, y 
ClasstimeMatcher generará todos los horarios válidos para cursar 
todas las materias que te interesan. 

(Puedes ingresar la misma materia con múltiples profesores sin 
problema, se resolverán los conflictos)\n""")
        print("1- Ingresar Materias")
        print("2- Ver materias ingresadas")
        print("3- Salir")

        opcion = int(input("Ingrese una opcion: "))

        if(opcion == 1):
            #Borrar pantalla

            if sys.platform == "win32":            
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
                # Metodo de validacion de tiempo para los horarios de las materias
                for day in days_of_week:
                    temp_list.append(validate_time_input(day))
                materialist.append(temp_list)
                #Generar archivo intermedio
                escribir_archivo(temp_list)
                #Borrar pantalla
                if sys.platform == "win32":
                    os.system("cls")
                val = 1
                #Coninuar añaadiendo materias
                print("\nDesea añadir otra materia? (S/N) ")
                validacion = input().upper()
        
        elif(opcion == 2):
            if(val == -1):
                print("No se han ingresado materias")
                if sys.platform == "win32":
                    os.system("pause")
                continue
            else:
                #Borrar pantalla
                if sys.platform == "win32":
                    os.system("cls")

                print("Materias ingresadas\n")
                #Mostrar materias ingresadas
                for materia in materialist:
                    print(f"{materia} \n")
                if sys.platform == "win32":
                    os.system("pause")
                continue

        elif(opcion == 3):
            print("Gracias por usar el generador de archivo intermedio")
            if sys.platform == "win32":
                os.system("pause")
            exit()

        else:
            print("Opcion invalida")
            if sys.platform == "win32":
                os.system("pause")
            continue

def main_intermedio():
    ingreso_materias()

if __name__ == "__main__":
       main_intermedio()
