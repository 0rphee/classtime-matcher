# ClassTime-Matcher

#materia,profesor,clave,lunes,martes,jueves,viernes,sabado,domingo
#comerialización,alan,01,11:30-13:00,NULL,15:30-17:00,NULL,NULL,NULL,NULL

import sys
import os
import main
import re
import pandas as pd
import csv
from styleframe import StyleFrame, Styler

# Regex for time validation
time_pattern = re.compile(r'^\d{2}:\d{2}-\d{2}:\d{2}$')
days_of_week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def get_unique_values(csv_file) -> list[str]:
    unique_values = set()
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            unique_values.add(row[0])
    
    return list(unique_values)
# Validate time input
def validate_time_input(day):
    while True:
        time_input = input(day + ": ").strip()
        if (time_input.upper() == "NULL") | (time_input == "n"):
            return "NULL"
        elif time_pattern.match(time_input):
            return time_input
        else:
            print("Formato de tiempo inválido. Intente nuevamente.")

# Method tp write the intermediate file
def escribir_archivo(lista):
    #Open csv file
    with open("intermedio.csv", "a") as f:
        #Write the list in the csv file
        for i, elemento in enumerate(lista):
            # Split the elements of the list by commas except the last one
            f.write(elemento)
            if i != len(lista) - 1:
                f.write(",")
        f.write("\n")
        #Close the file
    print(f"\nMateria {lista[2]} añadida con exito")

def ingreso_materias():
    materialist = []

    opcion = 0

    print("""Bienvenido a Classtime-Matcher\n
Con este programa podrás validar las materias que cursarás en tu 
próximo semestre. Ingresa todas las clases que te interesen, y 
ClasstimeMatcher generará todos los horarios válidos para cursar 
todas las materias que te interesan. 

(Puedes ingresar la misma materia con múltiples profesores sin 
problema, se resolverán los conflictos)\n""")

    while(opcion != 4):

        #Clear screen
        if sys.platform == "win32":
            os.system("cls")

        #Menu options
        print("1- Ingresar Materias")
        print("2- Ver materias ingresadas")
        print("3- Generar archivos excel con cada horario válido")
        print("4- Salir")

        opcion = int(input("Ingrese una opcion: "))

        if(opcion == 1):
            #Clear screen
            if sys.platform == "win32":            
                os.system("cls")

            print("Ingrese la informacion de las materias\n")
            #User input of the subjects
            validacion = "S"
            while(validacion == "S"):
                #Add the subject to the list
                temp_list = []
                unique_vals = get_unique_values("intermedio.csv")
                for index, val in enumerate(unique_vals):
                    print(f"{index+1} - {val}")

                userInput = int(input("0 para continuar, resto para nuevo nombre de materia: ").strip())
                if userInput > 0:
                    temp_list.append(unique_vals[userInput-1])
                else:
                    temp_list.append(input("\nIngrese el nombre de la materia: ").strip())
                temp_list.append(input("Ingrese el nombre del profesor: ").strip())
                temp_list.append(input("Ingrese la clave de la materia: ").strip())
                print('\nIngrese el horario de la materia ( 00:00-00:00 || NULL )\n')
                # Method to validate the time input
                for day in days_of_week:
                    temp_list.append(validate_time_input(day))
                temp_list.append(input("Ingrese el número de créditos de la materia: ").strip())
                materialist.append(temp_list)
                #Generate the intermediate file
                escribir_archivo(temp_list)
                #Clear screen
                if sys.platform == "win32":
                    os.system("cls")
                #Continue adding subjects
                print("\nDesea añadir otra materia? (S/N) ")
                validacion = input().upper().strip()
        
        elif(opcion == 2):
            #Clear screen
            if sys.platform == "win32":
                os.system("cls")

            #show the current added subjects 
            try:
                #if the file is empty, it will raise an exception
                subjects = main.readSubjectFile("intermedio.csv")
                for subj in subjects:
                    print(subj)
            except FileNotFoundError:
                print("\nNo se han ingresado materias\n")
                if sys.platform == "win32":
                    os.system("pause")
                continue

        elif(opcion == 3):
            #Clear screen
            if sys.platform == "win32":
                os.system("cls")
            #Generate the excel files with the valid schedules
            try:
                #Read the subjects from the intermediate file
                subjects = main.readSubjectFile("intermedio.csv")
                counter = 0
                #Validate the schedules
                if (valid_schedules := main.validate_schedules(subjects)):
                    if not os.path.exists("horarios"):
                        os.makedirs("horarios")
                        #Create the folder to save the excel files
                        print("Creando carpeta para guardar archivos excel: 'horarios'")
                    print()
                    #Create the excel files
                    dataFrames = []
                    with pd.ExcelWriter("horarios/horarios.xlsx") as writer:
                        for valid_schedule in valid_schedules:
                            counter += 1
                            nombrePaginaActual = f'horario{counter}'
                            print(f"Generando horario {counter} para pagina {nombrePaginaActual}")
                            crear_dataframe(valid_schedule).to_excel(writer, sheet_name=nombrePaginaActual, index=False)

                    #     dataFrames.append(crear_dataframe(valid_schedule))
                    # crear_excel(dataFrames, nombrePaginaActual)
                    print()
                else:
                    #Clear screen
                    if sys.platform == "win32":
                        os.system("cls")
                    print("No hay horarios válidos con las materias que hay registradas :(")
            #If the file is empty, it will raise an exception
            except FileNotFoundError:
                print("\nNo se han ingresado materias aún\n")
                if sys.platform == "win32":
                    os.system("pause")

        elif(opcion == 4):
            #Clear screen
            if sys.platform == "win32":
                os.system("cls")
            #Exit the program
            print("Gracias por susar Classtime-Matcher")
            if sys.platform == "win32":
                os.system("pause")
            exit()

        else:
            #Invalid option selected
            print("Opcion invalida")
            if sys.platform == "win32":
                os.system("pause")
            continue

# Creates DataFrame with the information of each class organized by columns
def crear_dataframe(materias): # materias: list[main.Subject]
    dd = altDt(materias)
    # materias = map(lambda x: x.format_subject(), materias)
    # columnas = ["MATERIA", "PROFESOR", "ID DE CLASE", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
    # df = pd.DataFrame(materias, columns=columnas)
    # return df
    return dd

def genDictDia() -> dict:
    dia = dict()
    for i in range(6,21):
        hora_inicio1, min_inicio1 = str(i), "00"

        hora_final2 = str(i+1)
        if i < 10:
            hora_inicio1 = "0" + hora_inicio1
        if (i+1) < 10:
            hora_final2 = "0" + hora_final2
        hora_final1, min_final1 = hora_inicio1, "30"

        bloque1 = hora_inicio1 + ":" + min_inicio1 + "-" + hora_final1 + ":" + min_final1

        hora_inicio2 = hora_final1
        min_inicio2 = min_final1
        min_final2 = min_inicio1

        bloque2 = hora_inicio2 + ":" + min_inicio2 + "-" + hora_final2 + ":" + min_final2

        dia[bloque1] = ""
        dia[bloque2] = ""
    return dia


# list[Subject]
def altDt(materias):
    def incrementHourStr(string:str) -> str:
        st = int(string) + 1
        if st < 10:
            return "0" + str(st)
        else :
            return str(st)

    def incrementTimeStr(hour: str, min:str) -> (str, str):
        if min == "00":
            return (hour, "30")
        else:
            return (incrementHourStr(hour), "00")

    def compareStrTimes(start: str, end: str) -> list((int,int)): # list of divided intervals
        # 10:00 - 09:30
        h1, h2 = start[:2], end[:2]
        min1, min2 = start[3:], end[3:]


        inters = [(h1,min1)]

        
        next = incrementTimeStr(h1,min1)

        while next != (h2,min2):
            # print((h1,min1), (h2,min2))
            inters.append(next)
            next = incrementTimeStr(next[0], next[1])
        else:
            inters.append((next))

        print(inters)
        intt = [hh + ":" + mm for hh, mm in inters]        
        pairs = [ (s, e) for s, e in zip(intt,intt[1:])]

        return pairs

    semana = {  "info" : {key:key for key in [f"#materias: {materias.__len__()}"
                                            , f"#cred: {sum([subj.credits for subj in materias])}"]
                            },
                "horas" : {key:key for key in genDictDia().keys()},
                "lunes": genDictDia(),
                "martes": genDictDia(),
                "miercoles": genDictDia(),
                "jueves": genDictDia(),
                "viernes": genDictDia() ,
                # "sabado": genDictDia(),
                # "domingo": genDictDia(),
            }
    for subj in materias:
        for clss in subj.classes:
            print(subj.name, clss)
            for strt,end in compareStrTimes(clss.start_time.__str__(), clss.end_time.__str__()):
                semana[f"{clss.day}"][f"{strt}-{end}"] = f"{subj.name}\n{subj.professor}" 
            
    print(semana)
    df = StyleFrame(pd.DataFrame.from_dict(semana).fillna(""))
    df.apply_column_style(cols_to_style="info", styler_obj=Styler(), width=20)
    df.apply_column_style(cols_to_style="horas", styler_obj=Styler(), width=15)
    df.apply_column_style(cols_to_style=["lunes","martes", "miercoles", "jueves", "viernes"], styler_obj=Styler(), width=30)  
    return df


    

#Creates an Excel file from the DataFrame
def crear_excel(dataFrames, pageName):
    # Create an ExcelWriter o
    with pd.ExcelWriter("horarios/horarios.xlsx") as writer:
        for df in dataFrames:
            df.to_excel(writer, sheet_name=pageName, index=False)

def main_intermedio():
    ingreso_materias()

if __name__ == "__main__":
       main.main()
