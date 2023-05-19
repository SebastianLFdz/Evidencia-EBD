from reporte_genero import reporte_generos
from diccionario import diccionario_libros
import datetime
from importar_excel import importar_excel
import os
import csv

dicc = {}

def Reportes():
    while True:
        print("""  
            +-----------------------------------------+
            |            Método de reporte            |
            +=========================================+
            | Catálogo completo             |    1    |
            +-----------------------------------------+
            | Reporte por autor             |    2    |   
            +-----------------------------------------+
            | Reporte por género            |    3    |
            +-----------------------------------------+
            | Por año de publicación        |    4    |   
            +-----------------------------------------+
            | Volver al menú anterior       |    5    |   
            +-----------------------------------------+\n""")

        metodo = input("Ingresa la opción que desees --> ")

        if metodo == "1":
            tipo = 0
            print("Los ejemplares disponibles en este momento son: \n")

            print(f'+{"-" *107}+')
            print(f"|{'ID':^8}|{'Título':^15}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
            print(f'+{"-"*107}+')
            for id_libro, datos in diccionario_libros.items():
                print(f'|{id_libro:^8}|{datos[0]:^15}|{datos[1]:^15}|{datos[2]:^12}|{datos[3]:^13}|{datos[4]:^18}|{datos[5]:^20}|')
                print(f'+{"-"*107}+')
                dicc[id_libro]=[datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]]
            while True:
                pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
                if pregunta_exportar == "S":
                    pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n1) CSV \n2) Excel\n-->"))

                    if pregunta_seleccion == 1:
                        with open("catalogo_libreria.csv", "w", newline="") as archivo:
                            grabador = csv.writer(archivo)
                            grabador.writerow(("clave", "titulo", "autor", "genero", "isbn", "año_publi"))
                            grabador.writerows([(clave, info[0], info[1], info[2], info[3], info[4], info[5]) for clave, info in dicc.items()])
                            nombre_file_catalogo = "catalogo_libreria.csv"
                            ruta_libreria = os.path.abspath(nombre_file_catalogo)
                            print(f"El archivo {nombre_file_catalogo} fué creado exitosamente, localizado en {ruta_libreria}.")
                            print("Gracias por visitar la biblioteca J. FELIX GARCIA")
                            break
                    elif pregunta_seleccion == 2:
                        importar_excel(dicc,tipo)
                        break
                    else:
                        print("Respuesta Invalida, Vuelva a Intentar")
                elif pregunta_exportar == "N":
                    print("No se exporto ningun archivo")
                    break
                else:
                    print("Respuesta Invalida, Vuelva a Intentar")

        elif metodo == "2":
            tipo = 1
            autores = []
            claves = list(diccionario_libros.keys())

            for clave in claves:
                autores.append(diccionario_libros[clave][1])

            conjunto_autores = set(autores)

            print("|"+"-"*21+"|")
            print("| Autores Disponibles |")
            print("|"+"-"*21+"|")

            for autores_iteracion in conjunto_autores:
                print(f"|{autores_iteracion:^21}|")

            print("|"+"-"*21+"|")
            autor_busqueda = input("Ingrese el nombre del autor que desee consultar: ").upper()

            autores = list(diccionario_libros.items())
            print(f'+{"-"*107}+')
            print(f"|{'ID':^8}|{'Título':^15}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
            print(f'+{"-"*107}+')
            n=0
            for id_libro, datos in autores:
                if autor_busqueda == diccionario_libros[id_libro][1]:
                    print(f'|{id_libro:^8}|{datos[0]:^15}|{datos[1]:^15}|{datos[2]:^12}|{datos[3]:^13}|{datos[4]:^18}|{datos[5]:^20}|')
                    print(f'+{"-"*107}+')
                    dicc[id_libro]=[datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]]
                    n+=1
            while True:
                pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
                if pregunta_exportar == "S":
                    pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n1) CSV \n2) Excel\n-->"))
                    if pregunta_seleccion == 1:
                        with open("autor_libreria.csv","w", newline="") as archivo:
                            grabador = csv.writer(archivo)
                            grabador.writerow(("clave", "titulo", "autor", "genero", "isbn", "año_publi"))
                            grabador.writerows([(clave, info[0], info[1], info[2], info[3], info[4], info[5])for clave, info in dicc.items()])
                            nombre_file_autor = "autor_libreria.csv"
                            ruta_autor = os.path.abspath(nombre_file_autor)
                            print(f"El archivo {nombre_file_autor} fué creado exitosamente, localizado en {ruta_autor}.")
                            print("Gracias por visitar la biblioteca J. FELIX GARCIA")
                            break
                    elif pregunta_seleccion == 2:
                        importar_excel(dicc,tipo)
                        break
                    else:
                        print("Respuesta Invalida, Vuelva a Intentar")
                elif pregunta_exportar == "N":
                    print("No se exportó nada.")
                    break
            if n == 0:
                print("| no se encontro el autor unu|")  
                continue
        elif metodo == "3":
            reporte_generos()
        elif metodo == "4":
            tipo = 3       
            anio = list(diccionario_libros.items())
            anio_busqueda= input("ingrese el año de publicacion del libro a desear: ")
            try:

                anio_datetime = datetime.datetime.strptime(anio_busqueda, "%Y").year

                print(f'+{"-"*98}+')
                print(f"|{'Título':^15}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
                print(f'+{"-"*98}+')
                coincidencia = 0
                for clave, datos in anio:
                    if anio_datetime == diccionario_libros[clave][4]:        
                        print(f'|{datos[0]:^15}|{datos[1]:^15}|{datos[2]:^12}|{datos[3]:^13}|{datos[4]:^18}|{datos[5]:^20}|')
                        print(f'+{"-"*98}+')
                        dicc[clave]=[datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]]
                        coincidencia += 1
                if coincidencia != 0:
                    while True:
                        pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
                        if pregunta_exportar == "S":
                            pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n1) CSV \n2) Excel\n-->"))
                            if pregunta_seleccion == 1:
                                with open("anio_publicacion_libreria.csv", "w", newline="") as archivo:
                                    grabador = csv.writer(archivo)
                                    grabador.writerow(("clave", "titulo", "autor", "genero", "isbn", "año_publi"))
                                    grabador.writerows([(clave, info[0], info[1], info[2], info[3], info[4], info[5]) for clave, info in dicc.items()])
                                    nombre_file_anio = "anio_publicacion_libreria.csv"
                                    ruta_anio = os.path.abspath(nombre_file_anio)
                                    print(f"El archivo {nombre_file_anio} fué creado exitosamente, localizado en {ruta_anio}.")
                                    print("Gracias por visitar la biblioteca J. FELIX GARCIA")
                                    break
                            elif pregunta_seleccion == 2:
                                importar_excel(dicc,tipo)
                                break
                            else:
                                print("Respuesta Invalida, Vuelva a Intentar")
                        elif pregunta_exportar == "N":
                            print("No se exporto ningun archivo")
                            break
                        else:
                            print("Respuesta Invalida, Vuelva a Intentar")
                elif coincidencia == 0:
                    print("No Existen Registros")
            except ValueError:
                print(f"El valor proporcionado ({anio_busqueda}) no es compatible con la operación solicitada")    
        elif metodo == "5":
            break
        else:
            print("La opción ingresada no es válida, intenta de nuevo: ")
            continue
    


