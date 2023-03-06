from diccionario import diccionario
import datetime

def registro():
    fecha_actual = datetime.datetime.now().date()

    def ingresar_datos():

        lista_datos = []
        while True:
            id_libro=max(diccionario, default=0)+1
            _titulo=input("Ingresa el titulo del libro que deseas registrar:  ")
            titulo = _titulo.upper()
            _autor=input(f"Ingresa el autor del libro {titulo}:  ")
            autor = _autor.upper()
            _genero=input(f"Ingresa el genero del libro {titulo}:  ")
            genero = _genero.upper()
            while True:
                isbn=input(f"Ingresa la clave ISBN del libro {titulo}: ")
                if len(isbn) == 13:
                    break
                else:
                    print("¬El ISBN debe tener 13 caracteres, Vuelva a Ingresarlos")
            while True:
                fecha_publicacion=input(f"Ingresa el año de publicacion del libro {titulo} (dd/mmyyyy): ")
                fecha_publicacion_procesada = datetime.datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
                publicacion = fecha_publicacion_procesada > fecha_actual
                if publicacion == True:
                    print(f"La Fecha {fecha_publicacion_procesada}, no es valida, vuelva a ingresarla")
                else:
                    while True:
                        fecha_adquisicion=input(f"Ingresa la fecha de adquisicion del libro {titulo} (dd/mm/yyyy): ")
                        fecha_adquisicion_procesada = datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
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
                print(lista_datos)
                validacion = input(f"¿Todos los datos introducidos estan correctos?\n (S/N): ")
                if validacion.upper() == "S":
                    diccionario[id_libro]=[titulo,autor,genero, año_publicacion,isbn,string_adquisicion]
                    break
                elif validacion.upper() == "N":
                    print(f"¿Cual dato quiere modificar?")
                    print(f"1)Titulo\t2)Autor\t\t\t3)Genero\n4)ISBN\t\t5)Fecha de Publicacion\t6)Fecha de Adquisicion")
                    dato_modificar = int(input("--> "))
                    if dato_modificar == 1:
                        _titulo=input("Ingresa el titulo del libro que deseas registrar:  ")
                        titulo = _titulo.upper()
                    elif dato_modificar == 2:
                        _autor=input(f"Ingresa el nuevo autor del libro {titulo}:  ")
                        autor= _autor.upper()
                    elif dato_modificar == 3:
                        _genero=input(f"Ingresa el nuevo genero del libro {titulo}:  ")
                        genero = _genero.upper()
                    elif dato_modificar == 4:
                        isbn=input(f"Ingresa la nuev clave ISBN {titulo}: ")
                    elif dato_modificar == 5:
                        while True:
                            fecha_publicacion=input(f"Ingresa el nueva fecha de publicacion del libro {titulo} (dd/mm/yyyy): ")
                            fecha_publicacion_procesada = datetime.datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
                            if fecha_publicacion_procesada < fecha_actual:
                                año_publicacion = fecha_publicacion_procesada.year 
                                break
                            else:
                                print(f"La Fecha {fecha_publicacion_procesada}, no es valida, vuelva a ingresarla")
                    elif dato_modificar == 6:
                        while True:
                            fecha_adquisicion=input(f"Ingresa la nueva fecha de adquisicion del libro {titulo}: ")
                            fecha_adquisicion_procesada = datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
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
