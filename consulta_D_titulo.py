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
            nombre_titulo=input("ingresa el nombre del titulo que deseas vizualizar --> ").upper()
            print(f"+{'-'*96}+")
            print(f"|{'ID Clave':^8}|{'Autor':^15}|{'Genero':^15}|{'Año de publicacion':^18}|{'ISBN':^15}|{'Fecha de adquisicion':^20}|")
            print(f"+{'='*8:^8}|{'='*15:^15}|{'='*15:^15}|{'='*18:^18}|{'='*15:^15}|{'='*20:^20}+")
            diccionario_items=diccionario.items()
            for llaves, valores in diccionario_items:
                if nombre_titulo in diccionario[llaves][0]:
                    if diccionario[llaves][0] == nombre_titulo:
                        #id |  titulo  | autor | genero  |  año de  publicadcion  |  ISBN | fecha de adquisision
                        print(f"|{llaves:^8}|{valores[1]:^15}|{valores[2]:^15}|{valores[3]:^18}|{valores[4]:^15}|{valores[5]:^20}|")
                        print(f"+{'-'*96}+")
            if not nombre_titulo in diccionario[llaves][0]:
                print("El titulo no hay en existencia")
        elif tipo_consulta=="2":
            isbn=input("ingresa el ISBN del libro que deseas vizualizar --> ").upper()
            print(f"+{'-'*101}+")
                        #id            titulo           autor           genero         año de publicacion       fecha de adquisisuin
            print(f"|{'ID Clave':^8}|{'Titulo':^15}|{'Autor':^15}|{'Genero':^15}|{'Año de publicacion':^20}|{'Fecha de adquisicion':^23}|")
            print(f"+{'='*8:^8}|{'='*15:^15}|{'='*15:^15}|{'='*15:^15}|{'='*20:^20}|{'='*23:^23}+")
            for llaves, valores in diccionario.items():
                if isbn in diccionario[llaves][4]:
                    if diccionario[llaves][4] == isbn:
                        print(f"|{llaves:^8}|{valores[0]:^15}|{valores[1]:^15}|{valores[2]:^15}|{valores[3]:^20}|{valores[5]:^23}|")
                        print(f"+{'-'*101}+")
            if not isbn in diccionario[llaves][4]:
                print("\tEl titulo no hay en existencia")
        elif tipo_consulta =="3":
            break
        else:
            print("Error la opcion ingresada no existe, intentelo de nuevo")
            continue
                