from sqlite3 import Error
import sqlite3
from consultas_Y_reportes import consulta_Y_reporte 
from registro_libro import registro
from diccionario import diccionario_libros
from diccionario import diccionario_autores
from diccionario import diccionario_generos
from registros import registros_autores
from registros import registros_generos
import csv
import sys

##Busqueda de CSV de Diccionario de Libros
try:   
    with open("catalogo_libreria.csv","r", newline="") as archivo:
        lector = csv.reader(archivo)
        for id, titulo, nombre, genero, isbn, año, fecha in lector:
            diccionario_libros[int(id)] = ([titulo, nombre, genero, isbn, año, fecha])
except FileNotFoundError:
    pass
except Exception:
    print("Ocurrio un Error Inesperado al buscar el respaldo de las librerias")

##Busqueda de CSV de Diccionario de Autores
try:   
    with open("catalogo_autores.csv","r", newline="") as archivo:
        lector = csv.reader(archivo)
        for id, nombre, apellidos in lector:
            diccionario_autores[int(id)] = ([nombre, apellidos])
except FileNotFoundError:
    pass
except Exception:
    print("Ocurrio un Error Inesperado al buscar el respaldo")

##Busqueda de CSV de Diccionario de Generos
try:   
    with open("catalogo_generos.csv","r", newline="") as archivo:
        lector = csv.reader(archivo)
        for id, nombre in lector:
            diccionario_generos[int(id)] = ([nombre])
except FileNotFoundError:
    pass
except Exception:
    print("Ocurrio un Error Inesperado al buscar el respaldo")


def menu():
    while True:
        print("""
                     __,                     ,__
                  __/==+\ J. FELIX GARCIA /+==\__
                    "  "`  ===============  '"  "
                                 ,   ,
                                /////|
                               ///// |
                              /////  |
                             /////   |
                            |~~~|    |
                            |===|    |
                            | P |    |
                            | Y |    |
                            | T |    |
                            | H |   /
                            | O |  /
                            | N | /
                            |===|/
                            '---'
            BIENVENIDO A LA BIBLIOTECA J. FELIX GARCIA
                           EL MENU
                1.- Registrar un nuevo ejemplar
                2.- Registrar un nuevo autor
                3.- Registrar un nuevo genero
                4.- Consultar y reportes
                5.- Salir""")
        print("\nNOTA: Para indicar que opcion desea realizar introduzca el numero de la opcion deseada")
        try:
            opciones=int(input("\nIngrese la opcion que desee realizar: "))
            if opciones ==1:
                registro()
            elif opciones==2:
                registros_autores()
            elif opciones ==3:
                registros_generos()              
            elif opciones ==4:
                consulta_Y_reporte()
            elif opciones==5:
                print("Gracias por visitar la biblioteca J. FELIX GARCIA")
                break
        except ValueError: 
            print("Hay un pequeño error de sintaxis, introduciste una letra o un simbolo en lugar de un numero")
        except Exception:
            print("Error hay un error intentalo de nuevo")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
menu()

print("*"*80)

#Guardar los Diccionarios en SQLite3
while True:
    try:
        with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn:
            cursor_biblioteca = conn.cursor()
            ##Sobreescritura de la Tabla registros_autores
            cursor_biblioteca.execute("DROP TABLE IF EXISTS registros_autores")
            cursor_biblioteca.execute("CREATE TABLE IF NOT EXISTS registros_autores \
                                (clave INTEGER PRIMARY KEY,\
                                nombre TEXT NOT NULL, apellido TEXT NOT NULL)")
            for id_autores, lista_autores in diccionario_autores.items():
                cursor_biblioteca.execute("INSERT INTO registros_autores (nombre,apellido)\
                                    VALUES(?,?)", lista_autores)
            print("Se registro correctamente los nuevos autores en la base de datos")

        with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn:
            cursor_biblioteca = conn.cursor()
            ##Sobreescritura de la Tabla registros_generos
            cursor_biblioteca.execute("DROP TABLE IF EXISTS registros_generos")
            cursor_biblioteca.execute("CREATE TABLE IF NOT EXISTS registros_generos\
                                (clave INTEGER PRIMARY KEY,\
                                nombre TEXT NOT NULL)")
            for id_generos, lista_generos in diccionario_generos.items():
                cursor_biblioteca.execute("INSERT INTO registros_generos (nombre)\
                                    VALUES(?)", (lista_generos))
            print("Se registro correctamente los nuevos generos en la base de datos")

        with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn:
            cursor_biblioteca = conn.cursor()
            ##Sobreescritura de la Tabla registros_libros
            cursor_biblioteca.execute("DROP TABLE IF EXISTS registros_libros")
            cursor_biblioteca.execute("CREATE TABLE IF NOT EXISTS registros_libros \
                                (clave INTEGER PRIMARY KEY,\
                                titulo TEXT NOT NULL, autor TEXT NOT NULL,\
                                genero TEXT NOT NULL, isbn INTEGER NOT NULL,\
                                añopub timestamp NOT NULL, fechaadq timestamp NOT NULL)")
            for id_libros, lista_libros in diccionario_libros.items():
                cursor_biblioteca.execute("INSERT INTO registros_libros (titulo,autor,genero, isbn, añopub, fechaadq)\
                                          VALUES(?,?,?,?,?,?)", lista_libros)
            print("Se registro correctamente los nuevos registros de libros en la base de datos")
        break
    except Error as e:
        print(e)
    except Exception:
        print("Ocurrio un Error inesperado ")
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    
print("*"*80)

#Guardar Diccionario_Libros
datos_a_grabar = dict()
archivo = open("catalogo_libreria.csv","w", newline="")
grabador = csv.writer(archivo)
grabador.writerows([(id,listado[0],listado[1],listado[2],
                     listado[3],listado[4],listado[5]) for id,listado 
                     in diccionario_libros.items()])
archivo.close()
print("Se registro correctamente los nuevos registros de libros en la memoria externa")


#Guardar Diccionario_Autores
datos_a_grabar = dict()
archivo = open("catalogo_autores.csv","w", newline="")
grabador = csv.writer(archivo)
grabador.writerows([(id,listado[0],listado[1]) for id,listado in diccionario_autores.items()])
archivo.close()
print("Se registro correctamente los nuevos registros de autores en la memoria externa")


#Guardar Diccionario_Autores
datos_a_grabar = dict()
archivo = open("catalogo_generos.csv","w", newline="")
grabador = csv.writer(archivo)
grabador.writerows([(id,listado[0]) for id,listado in diccionario_generos.items()])
archivo.close()
print("Se registro correctamente los nuevos registros de generos en la memoria externa")
