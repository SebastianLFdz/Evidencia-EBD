from diccionario import diccionario

def reporte_generos():
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
    print(f"\n¿Que Genero quieres buscar?")
    genero_busqueda_minusculas = str(input("--> "))
    genero_busqueda_mayusculas = genero_busqueda_minusculas.upper()

    print(" ")
    print("-"*86+"+")
    print(f"     Titulo\t|  Autor   |  Genero  |     ISBN      | Año Lanzado | Fecha Adquirida |")
    print("-"*86+"|")

    for clave in claves:
        if genero_busqueda_mayusculas == diccionario[clave][2]:
            print(f"{diccionario[clave][0]:^16}", end="")
            print(f"|{diccionario[clave][1]:^10}", end="")
            print(f"|{diccionario[clave][2]:^10}", end="")
            print(f"|{diccionario[clave][3]:^15}", end="")
            print(f"|{diccionario[clave][4]:^13}", end="")
            print(f"|{diccionario[clave][5]:^17}|")

    print("-"*86+"+")

