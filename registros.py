import sqlite3
import sys
from sqlite3 import Error
from diccionario import diccionario_autores
from diccionario import diccionario_generos


def registros_autores():
    try:
        while True:
            numero_validacion = 0
            print("Registro de autor")
            id_autor = max(diccionario_autores, default=0)+1
            nombre_autor = input("Ingrese el nombre del autor: ").upper()
            apellido_autor = input("Ingrese el apellido del autor: ").upper()
            lista_autores = [nombre_autor,apellido_autor]

            for tuplita in diccionario_autores.items():
                if nombre_autor == tuplita[1][0] and apellido_autor == tuplita[1][1]:
                    print("El autor ya existe")
                    numero_validacion += 1
            if numero_validacion == 0:
                lista_autores = [id_autor,nombre_autor,apellido_autor]
                diccionario_autores[id_autor] = [nombre_autor,apellido_autor]
                print("Se registro correctamente el nuevo autor en la memoria interna")

            with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn:
                cursos_autor = conn.cursor()
                cursos_autor.execute("INSERT INTO registros_autores (nombre,apellido)\
                                     VALUES(?,?)", lista_autores)
                print("Se registro correctamente el nuevo autor en la base de datos")

            try:
                while True:
                    decision = input("Desea agregar otro registro? S/N: ").upper()
                    if decision == "N":
                        break
                    elif decision == "S":
                        break
                    else:
                        print("Valor No Aceptable, Vuelva a Ingresarlo")
            except Exception:
                print("Error Inesperado, Volvamos a intentarlo")
            if decision == "N":
                break
            elif decision == 'S':
                continue
    except Error as e:
        print (e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()

def registros_generos():
    try:
        while True:
            id_genero=max(diccionario_generos,default=0)+1
            nuevo_genero=input("ingresa el nuevo genero a registrar: ").upper()
            if nuevo_genero == '':
                print('El dato no se de omitir, intente de nuevo.')
            elif nuevo_genero.isdigit():
                print('El dato es del tipo incorrecto, intente de nuevo.')
            diccionario_generos[id_genero]= [nuevo_genero]
            ##SQL
            with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn:
                cursos_autor = conn.cursor()
                cursos_autor.execute("INSERT INTO registros_generos (nombre)\
                                     VALUES(nuevo_genero)")
                print("Se registro correctamente el nuevo autor en la base de datos")

            while True:
                try:
                    decision=input('Deseas agregar otro genero? (S/N) --> ').upper()
                    if decision =="S":
                        break
                    elif decision=="N":
                        print("Se completo el registro deseado")
                        break
                    else:
                        print("La respuesta no es valida. ")
                except Exception:
                    print("Error Inesperado, Volvamos a intentarlo")
            if decision == "N":
                break
            elif decision == 'S':
                continue

    except ValueError:
        print("El tipo de error es invalido, intentalo de nuevo!!")
    except Exception:
        print("Hay un error, intentalo de nuevo ")