def seccion_autores():
    import sqlite3
    import sys
    from sqlite3 import Error

    try:
        with sqlite3.connect("JFelix_Garcia_Biblioteca.db") as conn: #1- Puente
            cursos_autor = conn.cursor()
            print("Registro de autor")
            nombre_autor = ("Ingrese el nombre del autor: ")
            apellido_autor = ("Ingrese el apellido del autor:")
            lista_autores = [nombre_autor,apellido_autor]
            desicion = ("Desea agregar otro registro? S/N: ")
            conn.execute("INSERT INTO registros_autores VALUES(?,?,?)", lista_autores)
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
seccion_autores()
