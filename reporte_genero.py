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
    print(f'+{"-"*99}+')
    print(f"|{'Título':^16}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
    print(f'+{"-"*99}+')

    n=0
    for clave in claves:
        if genero_busqueda_mayusculas == diccionario[clave][2]:
            print(f"|{diccionario[clave][0]:^16}", end="")
            print(f"|{diccionario[clave][1]:^15}", end="")
            print(f"|{diccionario[clave][2]:^12}", end="")
            print(f"|{diccionario[clave][3]:^13}", end="")
            print(f"|{diccionario[clave][4]:^18}", end="")
            print(f"|{diccionario[clave][5]:^20}|")
            n+=1

    if n == 0:
        print("No se encontro el libro por genero")
    print(f'+{"-"*99}+')

