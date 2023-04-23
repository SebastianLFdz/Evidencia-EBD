from diccionario import diccionario
from importar_excel import importar_excel

dicc = {}

def reporte_generos():
    tipo = 2
    generos = []
    claves = list(diccionario.keys())
    for clave in claves:
        generos.append(diccionario[clave][2])
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
        if genero_busqueda_mayusculas == diccionario[clave][2]:
            print(f"|{diccionario[clave][0]:^16}", end="")
            print(f"|{diccionario[clave][1]:^15}", end="")
            print(f"|{diccionario[clave][2]:^12}", end="")
            print(f"|{diccionario[clave][3]:^13}", end="")
            print(f"|{diccionario[clave][4]:^18}", end="")
            print(f"|{diccionario[clave][5]:^20}|")
            n+=1
            dicc[clave]=[diccionario[clave][0],
                         diccionario[clave][1],
                         diccionario[clave][2],
                         diccionario[clave][3],
                         diccionario[clave][4],
                         diccionario[clave][5]]
    if coincidencia != 0:
        while True:
            pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
            if pregunta_exportar == "S":
                pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n \
                                        1) CSV \n2) Excel\n-->"))
                if pregunta_seleccion == 1:
                    print("Aqui va el CSV")
                    
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

