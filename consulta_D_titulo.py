from diccionario import diccionario
def Consulta_de_titulo():
    while True:
        print("""  
    +-----------------------------------------+
    |            Tipos de Consultas           |
    +=========================================+
    | Consulta por Título           |    1    |
    +-----------------------------------------+
    | Por ISBN                      |    2    |   
    +-----------------------------------------+
    | Volver al menú de             |         |
    | consultas y reportes          |    3    |   
    +-----------------------------------------+""")
        tipo_consulta=input("Que tipo de consulta deseas realizar? --> ")
        if tipo_consulta=="1":
            titulos = list(diccionario.values())
            lista1=[]
            print(f"+{'-'*20}+")
            print(f"|{'Titulos disponibles':^20}|")
            for titulo in titulos:
                if titulo[0] in lista1:
                    continue
                else:
                    lista1.append(titulo[0])
                    print(f"|{'='*20:^20}|")
                    print(f"|{''.join(titulo[0]):^20}|")
            print(f"+{'='*20}+")
            nombre_titulo=input("ingresa el titulo del libro que deseas vizualizar --> ").upper()
            print(f"+{'-'*117}+")
                        #id            titulo           autor           genero         año de publicacion       fecha de adquisisuin
            print(f"|{'ID Clave':^8}|{'Titulo':^15}|{'Autor':^15}|{'Genero':^15}|{'Año de publicacion':^20}|{'ISBN':^15}|{'Fecha de adquisicion':^23}|")
            print(f"+{'='*8:^8}|{'='*15:^15}|{'='*15:^15}|{'='*15:^15}|{'='*20:^20}|{'='*15:^15}|{'='*23:^23}+")
            for llaves, valores in diccionario.items():
                if nombre_titulo in diccionario[llaves][0]:
                    if diccionario[llaves][0] == nombre_titulo:
                        print(f"|{llaves:^8}|{valores[0]:^15}|{valores[1]:^15}|{valores[2]:^15}|{valores[3]:^20}|{valores[4]:^15}|{valores[5]:^23}|")
                        print(f"+{'-'*117}+")

        elif tipo_consulta=="2":
            isbn=input("ingresa el ISBN del libro que deseas vizualizar --> ").upper()
            print(f"+{'-'*117}+")
                        #id            titulo           autor           genero         año de publicacion       fecha de adquisisuin
            print(f"|{'ID Clave':^8}|{'Titulo':^15}|{'Autor':^15}|{'Genero':^15}|{'Año de publicacion':^20}|{'ISBN':^15}|{'Fecha de adquisicion':^23}|")
            print(f"+{'='*8:^8}|{'='*15:^15}|{'='*15:^15}|{'='*15:^15}|{'='*20:^20}|{'='*15:^15}|{'='*23:^23}+")
            for llaves, valores in diccionario.items():
                if isbn in diccionario[llaves][4]:
                    if diccionario[llaves][4] == isbn:
                        print(f"|{llaves:^8}|{valores[0]:^15}|{valores[1]:^15}|{valores[2]:^15}|{valores[3]:^20}|{valores[4]:^15}|{valores[5]:^23}|")
                        print(f"+{'-'*117}+")

        elif tipo_consulta =="3":
            break
        else:
            print("Error la opcion ingresada no existe, intentelo de nuevo")
            continue
                