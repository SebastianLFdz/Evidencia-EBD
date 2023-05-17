from sqlite3 import Error
import sqlite3
from consultas_Y_reportes import consulta_Y_reporte 
from registro_libro import registro
from diccionario import diccionario
import csv
import sys

##Busqueda de CSV de Diccionario de Libros
try:   
    with open("registros_libreria.csv","r", newline="") as archivo:
        lector = csv.reader(archivo)
        for id, titulo, nombre, genero, isbn, año, fecha in lector:
            diccionario[int(id)] = ([titulo, nombre, genero, isbn, año, fecha])
except FileNotFoundError:
    pass
except Exception:
    print("Ocurrio un Error Inesperado al buscar el respaldo")

##Busqueda de CSV de Diccionario de Autores


##Busqueda de CSV de Diccionario de Generos


##BUsqueda de DB de la Biblioteca
try:
    with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn:
        cursor_autor = conn.cursor()
        cursor_autor.execute("CREATE TABLE IF NOT EXISTS registros_autores \
                                (clave INTEGER PRIMARY KEY,\
                                nombre TEXT NOT NULL, apellido TEXT NOT NULL)")
        cursor_autor.execute("CREATE TABLE IF NOT EXISTS registros_generos \
                                (clave INTEGER PRIMARY KEY,\
                                nombre TEXT NOT NULL)")
        cursor_autor.execute("CREATE TABLE IF NOT EXISTS registros_libros \
                                (clave INTEGER PRIMARY KEY,\
                                titulo TEXT NOT NULL, autor TEXT NOT NULL,\
                                genero TEXT NOT NULL, isbn INTEGER NOT NULL,\
                                añopub timestamp NOT NULL, fechaadq timestamp NOT NULL)")
except Error as e:
    print(e)
except Exception:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")




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
                2.- Consultar y reportes
                3.- Salir""")
        print("\nNOTA: Para indicar que opcion desea realizar introduzca el numero de la opcion deseada")
        try:
            opciones=int(input("\nIngrese la opcion que desee realizar: "))
            if opciones ==1:
                registro()
            elif opciones==2:
                consulta_Y_reporte()
            elif opciones ==3:
                print("Gracias por visitar la biblioteca J. FELIX GARCIA")
                break
        except ValueError: 
            print("Hay un pequeño error de sintaxis, introduciste una letra o un simbolo en lugar de un numero")
        except Exception:
            print("Error hay un error intentalo de nuevo")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
menu()

datos_a_grabar = dict()
archivo = open("catalogo_libreria.csv","w", newline="")
grabador = csv.writer(archivo)
grabador.writerows([(id,listado[0],listado[1],listado[2],listado[3],listado[4],listado[5]) for id,listado in diccionario.items()])
archivo.close()
