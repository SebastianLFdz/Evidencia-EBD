from reporte_genero import reporte_generos
from diccionario import diccionario

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
            reporte_generos()
        elif metodo == "4":
                anio_busqueda= input("ingrese el año de publicacion del libro a desear: ")
    anio_datetime = datetime.datetime.strptime(anio_busqueda, "%Y").year
    clave_anio = list(diccionario.keys())
    for clave in clave_anio:
        if anio_datetime == diccionario[clave][3]:
            print("-" * 100)
            print("|\t\tTitulo\t\t|\tAutor\t|\tGenero\t|\tAño Publicacion\t|\t\tISBN\t\t|\tFecha de Adquisicion\t|")
            print("-" * 100)
            print(f"{diccionario[clave][0]:<21}", end="")
            print(f"{diccionario[clave][1]:<13}", end="")
            print(f"{diccionario[clave][2]:<13}", end="")
            print(f"{diccionario[clave][3]:<21}", end="")
            print(f"{diccionario[clave][4]:<21}", end="")
            print(f"{diccionario[clave][5]:<15}")
            
        elif metodo == "5":
            break
        else:
            print("La opción ingresada no es válida, intenta de nuevo: ")
            continue
