from diccionario import diccionario_autores
from importar_excel import importar_excel
import os
import csv

dicc = {}

def reporte_generos():
    tipo = 2
    generos = []
    claves = list(diccionario_autores.keys())
    for clave in claves:
        generos.append(diccionario_autores[clave][2])
    conjunto_generos = set(generos)

    print("|"+"-"*21+"|")
    print("| Generos Disponibles |")
    print("|"+"-"*21+"|")

    for genero_for in conjunto_generos:
        print(f"|{genero_for:^21}|")

    print("|"+"-"*21+"|")
    print("\n¿Que Genero quieres buscar?")
    genero_busqueda_mayusculas = str(input("--> ")).upper()

    print(" ")
    print(f'+{"-"*99}+')
    print(f"|{'Título':^16}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
    print(f'+{"-"*99}+')

    coincidencia=0
    for clave in claves:
        if genero_busqueda_mayusculas == diccionario_autores[clave][2]:
            print(f"|{diccionario_autores[clave][0]:^16}", end="")
            print(f"|{diccionario_autores[clave][1]:^15}", end="")
            print(f"|{diccionario_autores[clave][2]:^12}", end="")
            print(f"|{diccionario_autores[clave][3]:^13}", end="")
            print(f"|{diccionario_autores[clave][4]:^18}", end="")
            print(f"|{diccionario_autores[clave][5]:^20}|")
            coincidencia+=1
            dicc[clave]=[diccionario_autores[clave][0],
                         diccionario_autores[clave][1],
                         diccionario_autores[clave][2],
                         diccionario_autores[clave][3],
                         diccionario_autores[clave][4],
                         diccionario_autores[clave][5]]
    print(f'+{"-"*99}+')
    if coincidencia != 0:
        while True:
            pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
            if pregunta_exportar == "S":
                pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n1) CSV \n2) Excel\n-->"))
                if pregunta_seleccion == 1:
                    with open("reporte_genero.csv", "w", newline="") as archivo:
                        grabador = csv.writer(archivo)
                        grabador.writerow(("clave", "titulo", "autor", "genero", "isbn", "año_publi"))
                        grabador.writerows([(clave, info[0], info[1], info[2], info[3], info[4], info[5])for clave, info in dicc.items()])
                        print("El Archivo fue creado exitosamente")
                        print("Gracias por visitar la biblioteca J. FELIX GARCIA")
                        break
                elif pregunta_seleccion == 2:
                    importar_excel(dicc,tipo)
                    break
                else:
                    print("Respuesta Invalida, Vuelva a Intentar")
            elif pregunta_exportar == "N":
                print("No se exporto ningun archivo")
            else:
                print("Respuesta Invalida, Vuelva a Intentar")

    if coincidencia == 0:
        print("No se encontro el libro por genero")
    print(f'+{"-"*99}+')