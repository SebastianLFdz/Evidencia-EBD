from diccionario import diccionario
import datetime


def registro():
    print("+"+"-"*60+"+")
    fecha_actual = datetime.datetime.now().date()

    def ingresar_datos():

        lista_datos = []
        while True:
            id_libro=max(diccionario, default=0)+1
            while True:
                _titulo=input("Ingresa el titulo del libro que deseas registrar:\n-->")
                if _titulo.isdigit():
                    print("El dato es un entero")
                elif _titulo=="":
                    print("No se admiten valores nulos")
                else:
                    titulo = _titulo.upper()
                    break
            print("+"+"-"*60+"+")


            while True:
                _autor=input(f"Ingresa el autor del libro {titulo}:\n-->")
                if _autor.isdigit():
                    print("El dato es un valor entero")
                elif _autor=="":
                    print("No se admiten valores nulos")
                else:    
                    autor = _autor.upper()
                    break
            print("+"+"-"*60+"+")

            while True:
                _genero=input(f"Ingresa el genero del libro {titulo}:\n-->")
                if _genero.isdigit():
                    print("El  dato es un valor entero")
                elif _genero =="":
                    print("No se admiten valores nulos")
                else:
                    genero = _genero.upper()
                    break

            print("+"+"-"*60+"+")
            while True:
                isbn=input(f"Ingresa la clave ISBN del libro {titulo}:\n-->")
                if len(isbn) == 13:
                    try:
                        isbn=int(isbn)
                    except ValueError :
                        print("Hay un pequeño error de sintaxis, introduciste ua letra o un simbolo en lugar de un numero")

                    else:
                        break
                else:
                    print("El ISBN debe tener 13 caracteres, Vuelva a Ingresarlos")
                
            while True:
                print("+"+"-"*60+"+")
                try:
                    fecha_publicacion=input(f"Ingresa la fecha de publicacion del libro {titulo} (dd/mm/yyyy):\n-->")
                    fecha_publicacion_procesada = datetime.datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
                except ValueError: 
                    print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                else:
                    publicacion = fecha_publicacion_procesada > fecha_actual
                    if publicacion == True:
                        print(f"La Fecha {fecha_publicacion_procesada}, no es valida, vuelva a ingresarla")
                    else:
                        while True:
                            print("+"+"-"*60+"+")
                            try:
                                fecha_adquisicion=input(f"Ingresa la fecha de adquisicion del libro {titulo} (dd/mm/yyyy):\n-->")
                                fecha_adquisicion_procesada = datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
                            except ValueError: 
                                print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                            else:
                                adquisicion = fecha_adquisicion_procesada > fecha_actual
                                if adquisicion == True:
                                    print(f"La Fecha {fecha_adquisicion_procesada}, no es valida, vuelva a ingresarla")
                                else:
                                    break
                        comparacion = fecha_adquisicion_procesada < fecha_publicacion_procesada
                        if comparacion == True:
                            print(f"La Fecha de Adquisicion no puede ser mayor a la Fecha de Publicacion")
                        else:
                            break
            año_publicacion = fecha_publicacion_procesada.year 
            string_adquisicion = str(fecha_adquisicion_procesada)

            while True:
                lista_datos = [titulo,autor,genero, isbn, año_publicacion, string_adquisicion]
                
                print(f"+{'-'*122}+")
                print(f"|{'ID Clave':^8}|{'Titulo':^15}|{'Autor':^15}|{'Genero':^15}|{'ISBN':^20}|{'Año de publicacion':^20}|{'Fecha de adquisicion':^23}|")
                print(f"+{'='*8:^8}|{'='*15:^15}|{'='*15:^15}|{'='*15:^15}|{'='*20:^20}|{'='*20:^20}|{'='*23:^23}+")
                print(f"|{id_libro:^8}|{lista_datos[0]:^15}|{lista_datos[1]:^15}|{lista_datos[2]:^15}|{lista_datos[3]:^20}|{lista_datos[4]:^20}|{lista_datos[5]:^23}|")
                print(f"+{'-'*122}+")
                validacion = input(f"¿Todos los datos introducidos estan correctos?\n (S/N): ")
                if validacion.upper() == "S":
                    diccionario[id_libro]=[titulo,autor,genero, isbn, año_publicacion, string_adquisicion]
                    break
                elif validacion.upper() == "N":
                    print("+"+"-"*60+"+")
                    print(f"¿Cual dato quiere modificar?")
                    print(f"1)Titulo\t2)Autor\t\t\t3)Genero\n4)ISBN\t\t5)Fecha de Publicacion\t6)Fecha de Adquisicion")
                    dato_modificar = int(input("--> "))
                    print("+"+"-"*60+"+")
                    if dato_modificar == 1:
                        while True:
                            _titulo=input("Ingresa el titulo del libro que deseas registrar:\n-->")
                            if _titulo.isdigit():
                                print("El dato es un entero")
                            elif _titulo=="":
                                print("No se admiten valores nulos")
                            else:
                                titulo = _titulo.upper()
                                break
                    elif dato_modificar == 2:
                        while True:
                            _autor=input(f"Ingresa el nuevo autor del libro {titulo}:  ")
                            if _autor.isdigit():
                                print("El dato es un entero")
                            elif _titulo=="":
                                print("No se admiten valores nulos")
                            else:
                                autor= _autor.upper()
                    elif dato_modificar == 3:
                        while True:
                            _genero=input(f"Ingresa el nuevo genero del libro {titulo}:  ")
                            if _genero.isdigit():
                                print("El dato es un entero")
                            elif _titulo=="":
                                print("No se admiten valores nulos")
                            else:
                                genero = _genero.upper()
                    
                    elif dato_modificar == 4:
                        isbn=input(f"Ingresa la nuev clave ISBN {titulo}: ")
                        if len(isbn) == 13:
                            try:
                                isbn=int(isbn)
                            except ValueError :
                                print("Hay un pequeño error de sintaxis, introduciste ua letra o un simbolo en lugar de un numero")
                            else:
                                break
                        else:
                            print("El ISBN debe tener 13 caracteres, Vuelva a Ingresarlos")
                    elif dato_modificar == 5:
                        while True:
                            try:
                                fecha_publicacion=input(f"Ingresa el nueva fecha de publicacion del libro {titulo} (dd/mm/yyyy): ")
                                fecha_publicacion_procesada = datetime.datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
                            except ValueError:
                                print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                            
                            else:
                                if fecha_publicacion_procesada < fecha_actual:
                                    año_publicacion = fecha_publicacion_procesada.year 
                                    break
                                else:
                                    print(f"La Fecha {fecha_publicacion_procesada}, no es valida, vuelva a ingresarla")
                    elif dato_modificar == 6:
                        while True:
                            try:
                                fecha_adquisicion=input(f"Ingresa la nueva fecha de adquisicion del libro {titulo}: ")
                                fecha_adquisicion_procesada = datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
                            except ValueError:
                                print("Hay un pequeño error de sintaxis, ingresa un dato de tipo fecha con el formato indicado. ")
                            else:
                                if fecha_adquisicion_procesada < fecha_actual:
                                    if fecha_adquisicion_procesada > fecha_publicacion_procesada:
                                        string_adquisicion = str(fecha_adquisicion_procesada)
                                        break
                                    else:
                                        print(f"La Fecha de Adquisicion no puede ser mayor a la Fecha de Publicacion")
                                else:
                                    print(f"La Fecha {fecha_adquisicion_procesada}, no es valida, vuelva a ingresarla")
                    else:
                        print("Valor erroneo, Vuelva a Intentarlo")
                else:
                    print("Respuesta No Aceptada, Vuelva a Ingresarla")
            if validacion.upper() == "S":
                break 
    ingresar_datos()

