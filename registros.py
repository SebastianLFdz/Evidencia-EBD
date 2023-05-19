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
            while True:
                try:
                    nombre_autor = str(input("Ingrese el nombre del autor: ").upper())
                    if nombre_autor == '':
                        print('El dato no se de omitir, intente de nuevo.')
                    else:
                        break
                except TypeError:
                    print("El nombre es del tipo incorrecto, intente de nuevo.")
            
            while True:
                try:
                    apellido_autor = str(input("Ingrese el apellido del autor: ").upper())
                    if nombre_autor == '':
                        print('El dato no se de omitir, intente de nuevo.')
                    else:
                        break
                except TypeError:
                    print('El apellido es del tipo incorrecto, intente de nuevo.')
                        

            for tuplita in diccionario_autores.items():
                if nombre_autor == tuplita[1][0] and apellido_autor == tuplita[1][1]:
                    print("El autor ya existe")
                    numero_validacion += 1
            if numero_validacion == 0:
                diccionario_autores[id_autor] = [nombre_autor,apellido_autor]
                print("Se registro correctamente el nuevo autor en la memoria interna")
            elif numero_validacion > 0:
                continue

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

def registros_generos():
    try:
        while True:
            numero_validacion = 0
            print("Registro de genero")
            id_genero=max(diccionario_generos,default=0)+1
            while True:
                try:
                    nuevo_genero = str(input("ingresa el nuevo genero a registrar: ").upper())
                    if nuevo_genero == '':
                        print('El dato no se de omitir, intente de nuevo.')
                    else:
                        break
                except TypeError:
                    print('El dato es del tipo incorrecto, intente de nuevo.')
            for nombre in diccionario_generos.values():
                if nuevo_genero == nombre[0]:
                    print("El genero ya existe")
                    numero_validacion += 1
            if numero_validacion == 0:
                diccionario_generos[id_genero] = [nuevo_genero]
                print("Se registro correctamente el nuevo autor en la memoria interna")
            elif numero_validacion > 0:
                continue
            

            while True:
                try:
                    decision=input('Deseas agregar otro genero? (S/N) --> ').upper()
                    if decision =="S":
                        break
                    elif decision=="N":
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