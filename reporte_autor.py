from reporte_genero import reporte_generos
from diccionario import diccionario
import datetime
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
            print("Los ejemplares disponibles en este momento son: \n")

            print(f'+{"-" *102}+')
            print(f"|{'ID':^8}|{'Título':^15}|{'Autor':^10}|{'Género':^12}|{'Año de publicación':^18}|{'ISBN':^13}|{'Fecha de adquisición':^20}|")
            for id_libro, datos in diccionario.items():
                print(f'+{"-" *102}+')
                print(f'|{id_libro:^8}|{datos[0]:^15}|{datos[1]:^10}|{datos[2]:^12}|{datos[3]:^18}|{datos[4]:^13}|{datos[5]:^20}|')
                print(f'+{"-"*102}+')

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
            
            anio = list(diccionario.items())
            anio_busqueda= input("ingrese el año de publicacion del libro a desear: ")
            anio_datetime = datetime.datetime.strptime(anio_busqueda, "%Y").year
            
            print(f'+{"-"*98}+')
            print(f"|{'Título':^15}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
            print(f'+{"-"*98}+')
            
            for clave, datos in anio:
                if anio_datetime == diccionario[clave][4]:        
                    print(f'|{datos[0]:^15}|{datos[1]:^15}|{datos[2]:^12}|{datos[3]:^13}|{datos[4]:^18}|{datos[5]:^20}|')
                    print(f'+{"-"*98}+')
            
        elif metodo == "5":
            break
        else:
            print("La opción ingresada no es válida, intenta de nuevo: ")
            continue
