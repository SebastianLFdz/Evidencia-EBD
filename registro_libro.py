from diccionario import diccionario_libros
from diccionario import diccionario_autores
from diccionario import diccionario_generos
import datetime
from tabulate import tabulate
import sys
import csv
import sqlite3


def registro():
    print("+"+"-"*60+"+")
    fecha_actual = datetime.datetime.now().date()
    tabulado_autores = [["Clave","Nombre","Apellido"]]
    tabulado_generos = [["Clave","Nombre"]]

    for id, lista in diccionario_autores.items():
        tabulado_autores.append([id,lista[0],lista[1]])

    for id, lista in diccionario_generos.items():
        tabulado_generos.append([id,lista[0]])
    
    def ingresar_datos():
        lista_datos = []
        #print(diccionario_generos.items())
        validacion = 0
        validacion_2 = 0

        while True:
            id_libro=max(diccionario_libros, default=0)+1
            while True:
                _titulo=input("Ingresa el titulo del libro que deseas registrar:\n-->")
                if _titulo.isdigit():
                    print("El dato es un entero")
                elif _titulo=="":
                    print("No se admiten valores nulos")
                else:
                    titulo = _titulo.upper()
                    break
            print("+"+"-"*60+"+")

            while True:
                ##Tabla de autores
                print(tabulate(tabulado_autores, tablefmt="grid"))
                while True:
                    try:
                        _autor = int(input("Ingresa la llave del autor deseado: "))
                        if _autor =="":
                            print("No se puede omitir este dato, intente de nuevo.")
                        else:
                            break
                    except Exception:
                        print("Ocurrio un Error inesperado ")
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

                for id, tupla in diccionario_autores.items():
                    if _autor == id:
                        print("El autor se registro bien")
                        autor = tupla[0]
                        validacion += 1
                if validacion > 0 :
                    break
                else:
                    print("No se encontro un autor")

            print("+"+"-"*60+"+")

            while True:
                ##Tabla de Generos
                print(tabulate(tabulado_generos, tablefmt="grid"))
                while True:
                    try:
                        genero = int(input(f"Ingresa el genero del libro {titulo}:\n-->"))
                        #print(type(_genero))
                        if genero =="":
                            print("No se admiten valores nulos")
                        else:
                            break
                    except Exception:
                        print("Ocurrio un Error inesperado ")
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

                for id, nombre in diccionario_generos.items():
                    if genero == id:
                        print("El género se registro bien")
                        _genero = nombre[0]
                        validacion_2 += 1
                    
                if validacion_2 > 0 :
                    break
                else:
                    print("No se encontro el género.")

            print("+"+"-"*60+"+")
            while True:
                isbn=input(f"Ingresa la clave ISBN del libro {titulo}:\n-->")
                if len(isbn) == 13:
                    try:
                        isbn=int(isbn)
                    except ValueError :
                        print("Hay un pequeño error de sintaxis, introduciste ua letra o un simbolo en lugar de un numero")

                    else:
                        break
                else:
                    print("El ISBN debe tener 13 caracteres, Vuelva a Ingresarlos")
                
            while True:
                print("+"+"-"*60+"+")
                try:
                    fecha_publicacion=input(f"Ingresa la fecha de publicacion del libro {titulo} (dd/mm/yyyy):\n-->")
                    fecha_publicacion_procesada = datetime.datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
                except ValueError: 
                    print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                else:
                    publicacion = fecha_publicacion_procesada > fecha_actual
                    if publicacion == True:
                        print(f"La Fecha {fecha_publicacion_procesada}, no es valida, vuelva a ingresarla")
                    else:
                        while True:
                            print("+"+"-"*60+"+")
                            try:
                                fecha_adquisicion=input(f"Ingresa la fecha de adquisicion del libro {titulo} (dd/mm/yyyy):\n-->")
                                fecha_adquisicion_procesada = datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
                            except ValueError: 
                                print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                            else:
                                adquisicion = fecha_adquisicion_procesada > fecha_actual
                                if adquisicion == True:
                                    print(f"La Fecha {fecha_adquisicion_procesada}, no es valida, vuelva a ingresarla")
                                else:
                                    break
                        comparacion = fecha_adquisicion_procesada < fecha_publicacion_procesada
                        if comparacion == True:
                            print(f"La Fecha de Adquisicion no puede ser mayor a la Fecha de Publicacion")
                        else:
                            break
            año_publicacion = fecha_publicacion_procesada.year 
            string_adquisicion = str(fecha_adquisicion_procesada)

            datos_a_grabar = {}
            while True:
                lista_datos = [titulo,autor,_genero, isbn, año_publicacion, string_adquisicion]

                print(f"+{'-'*122}+")
                print(f"|{'ID Clave':^8}|{'Titulo':^15}|{'Autor':^15}|{'Genero':^15}|{'ISBN':^20}|{'Año de publicacion':^20}|{'Fecha de adquisicion':^23}|")
                print(f"+{'='*8:^8}|{'='*15:^15}|{'='*15:^15}|{'='*15:^15}|{'='*20:^20}|{'='*20:^20}|{'='*23:^23}+")
                print(f"|{id_libro:^8}|{lista_datos[0]:^15}|{lista_datos[1]:^15}|{lista_datos[2]:^15}|{lista_datos[3]:^20}|{lista_datos[4]:^20}|{lista_datos[5]:^23}|")
                print(f"+{'-'*122}+")
                validacion = input(f"¿Todos los datos introducidos estan correctos?\n (S/N): ")

                if validacion.upper() == "S":
                    diccionario_libros[id_libro]=[titulo,autor,_genero, isbn, año_publicacion, string_adquisicion]
                    datos_a_grabar[id_libro] = [titulo,autor,_genero, isbn, año_publicacion, string_adquisicion]
                    with open("catalogo_libreria.csv","w", newline="") as archivo:
                        grabador = csv.writer(archivo)
                        grabador.writerows([(id,listado[0],listado[1],listado[2],listado[3],listado[4],listado[5]) for id,listado in datos_a_grabar.items()])
                        print("Se registro correctamente los nuevos registros de libros en la memoria externa")
                    with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn:
                        cursor_biblioteca = conn.cursor()
                        for id_libros, lista_libros in datos_a_grabar.items():
                            cursor_biblioteca.execute("INSERT INTO registros_libros (titulo,autor,genero, isbn, añopub, fechaadq)\
                                          VALUES(?,?,?,?,?,?)", lista_libros)
                    break

                elif validacion.upper() == "N":
                    print("+"+"-"*60+"+")
                    print(f"¿Cual dato quiere modificar?")
                    print(f"1)Titulo\t2)Autor\t\t\t3)Genero\n4)ISBN\t\t5)Fecha de Publicacion\t6)Fecha de Adquisicion")
                    dato_modificar = int(input("--> "))
                    print("+"+"-"*60+"+")

                    if dato_modificar == 1:
                        while True:
                            _titulo=input("Ingresa el titulo del libro que deseas registrar:\n-->")
                            if _titulo.isdigit():
                                print("El dato es un entero")
                            elif _titulo=="":
                                print("No se admiten valores nulos")
                            else:
                                titulo = _titulo.upper()
                                break
                    elif dato_modificar == 2:
                        print(tabulate(tabulado_autores, tablefmt="grid"))
                        validacion_1 = 0
                        while True:
                            try:
                                _autor = int(input("Ingresa la llave del autor deseado: "))
                                if _autor =="":
                                    print("No se puede omitir este dato, intente de nuevo.")
                            except Exception:
                                print("Ocurrio un Error inesperado ")
                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                            else:
                                for id, tupla in diccionario_autores.items():
                                    if _autor == id:
                                        autor = tupla[0]
                                        print("El autor se registro bien")                                        
                                        validacion_1 += 1
                                if validacion_1 > 0 :
                                    break
                    elif dato_modificar == 3:
                        print(tabulate(tabulado_generos, tablefmt="grid"))
                        while True:
                            try:
                                genero = int(input(f"Ingresa el genero del libro {titulo}:\n-->"))
                                #print(type(_genero))
                                if genero =="":
                                    print("No se admiten valores nulos")
                            except Exception:
                                print("Ocurrio un Error inesperado ")
                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                            else:
                                for id, tupla in diccionario_generos.items():
                                    if genero == id:
                                        print("El género se registro bien")
                                        _genero = tupla[0]
                                        validacion_2 += 1
                                if validacion_2 > 0 :
                                    break
                    elif dato_modificar == 4:
                        isbn=input(f"Ingresa la nuev clave ISBN {titulo}: ")
                        if len(isbn) == 13:
                            try:
                                isbn=int(isbn)
                            except ValueError :
                                print("Hay un pequeño error de sintaxis, introduciste ua letra o un simbolo en lugar de un numero")
                            else:
                                break
                        else:
                            print("El ISBN debe tener 13 caracteres, Vuelva a Ingresarlos")
                    elif dato_modificar == 5:
                        while True:
                            try:
                                fecha_publicacion=input(f"Ingresa el nueva fecha de publicacion del libro {titulo} (dd/mm/yyyy): ")
                                fecha_publicacion_procesada = datetime.datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
                            except ValueError:
                                print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                            
                            else:
                                if fecha_publicacion_procesada < fecha_actual:
                                    año_publicacion = fecha_publicacion_procesada.year 
                                    break
                                else:
                                    print(f"La Fecha {fecha_publicacion_procesada}, no es valida, vuelva a ingresarla")
                    elif dato_modificar == 6:
                        while True:
                            try:
                                fecha_adquisicion=input(f"Ingresa la nueva fecha de adquisicion del libro {titulo}: ")
                                fecha_adquisicion_procesada = datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
                            except ValueError:
                                print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                            else:
                                if fecha_adquisicion_procesada < fecha_actual:
                                    if fecha_adquisicion_procesada > fecha_publicacion_procesada:
                                        string_adquisicion = str(fecha_adquisicion_procesada)
                                        break
                                    else:
                                        print(f"La Fecha de Adquisicion no puede ser mayor a la Fecha de Publicacion")
                                else:
                                    print(f"La Fecha {fecha_adquisicion_procesada}, no es valida, vuelva a ingresarla")
                    else:
                        print("Valor erroneo, Vuelva a Intentarlo")
                else:
                    print("Respuesta No Aceptada, Vuelva a Ingresarla")
            if validacion.upper() == "S":
                break 
    ingresar_datos()

