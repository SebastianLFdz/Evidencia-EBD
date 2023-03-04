import tabulate
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
            encabezados = ["ID", "Título", "Autor", "Género", "Año de publicación", "ISBN", "Fecha de adquisición"]

            print("Los ejemplares disponibles en este momento son: \n")
            tabla = [[id_libro] + datos for id_libro, datos in diccionario.items()]
            print(tabulate.tabulate(tabla, headers=encabezados))

        elif metodo == "2":

            encabezados = ["ID", "Título", "Autor", "Género", "Año de publicación", "ISBN", "Fecha de adquisición"]

            autor_busqueda = input("Ingrese el nombre del autor que desee consultar: ")
            libros_autor = []

            for id_libro, datos in diccionario.items():
                if autor_busqueda in datos[1]:
                    libros_autor.append([id_libro] + datos)
            if libros_autor:
                print(f"Los libros escritos por {autor_busqueda} son: \n")
                print(tabulate.tabulate(libros_autor, headers=encabezados))
            else:
                print(f"No se encontraron libros escritos por {autor_busqueda}.")
        elif metodo == "3":
            continue
        elif metodo == "4":
            continue
        elif metodo == "5":
            break
        else:
            print("La opción ingresada no es válida, intenta de nuevo: ")
            continue
