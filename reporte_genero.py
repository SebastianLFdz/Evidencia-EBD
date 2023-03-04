def reporte_generos():
    diccionario = {
        1:["Fuego Abrasador","Sebas","MIEDO",1234567890123,"2004","26/08/2006"],
        2:["Hielo Intenso","Sebas","ROMANCE",1234567890213,"2005","12/10/2008"],
        3:["Zacatecas","Omar","MIEDO",1234567890312,"2014","16/04/2016"],
        4:["Muevo Leon","Mauricio","MIEDO",1234567890132,"2010","07/12/2016"],
        5:["Tierra Desolada","Sebas","ROMANCE",1234567890231,"2011","01/04/2020"],
        }
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
    print("-"*86+"|")
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

    print("-"*86+"|")

