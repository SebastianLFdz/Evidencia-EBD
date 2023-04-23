from reporte_genero import reporte_generos
from diccionario import diccionario
import datetime
from importar_excel import importar_excel

dicc = {}

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
            tipo = 0
            print("Los ejemplares disponibles en este momento son: \n")

            print(f'+{"-" *107}+')
            print(f"|{'ID':^8}|{'Título':^15}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
            print(f'+{"-"*107}+')
            for id_libro, datos in diccionario.items():
                print(f'|{id_libro:^8}|{datos[0]:^15}|{datos[1]:^15}|{datos[2]:^12}|{datos[3]:^13}|{datos[4]:^18}|{datos[5]:^20}|')
                print(f'+{"-"*107}+')
                dicc[id_libro]=[datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]]
            while True:
                pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
                if pregunta_exportar == "S":
                    pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n \
                                            1) CSV \n2) Excel\n-->"))
                    if pregunta_seleccion == 1:
                        print("Aqui va el CSV")
                        break
                    elif pregunta_seleccion == 2:
                        importar_excel(dicc,tipo)
                        break
                    else:
                        print("Respuesta Invalida, Vuelva a Intentar")
                elif pregunta_exportar == "N":
                    print("No se exporto ningun archivo")
                else:
                    print("Respuesta Invalida, Vuelva a Intentar")
            

        elif metodo == "2":
            tipo = 1
            autores = []
            claves = list(diccionario.keys())

            for clave in claves:
                autores.append(diccionario[clave][1])

            conjunto_autores = set(autores)

            print("|"+"-"*21+"|")
            print("| Autores Disponibles |")
            print("|"+"-"*21+"|")

            for autores_iteracion in conjunto_autores:
                print(f"|{autores_iteracion:^21}|")

            print("|"+"-"*21+"|")
            autor_busqueda = input("Ingrese el nombre del autor que desee consultar: ").upper()

            autores = list(diccionario.items())
            print(f'+{"-"*107}+')
            print(f"|{'ID':^8}|{'Título':^15}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
            print(f'+{"-"*107}+')
            n=0
            for id_libro, datos in autores:
                if autor_busqueda == diccionario[id_libro][1]:
                    print(f'|{id_libro:^8}|{datos[0]:^15}|{datos[1]:^15}|{datos[2]:^12}|{datos[3]:^13}|{datos[4]:^18}|{datos[5]:^20}|')
                    print(f'+{"-"*107}+')
                    dicc[id_libro]=[datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]]
                    n+=1
            if n == 0:
                print("| no se encontro el autor unu|")
            while True:
                pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
                if pregunta_exportar == "S":
                    pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n \
                                            1) CSV \n2) Excel\n-->"))
                    if pregunta_seleccion == 1:
                        print("Aqui va el CSV")
                        break
                    elif pregunta_seleccion == 2:
                        importar_excel(dicc,tipo)
                        break
                    else:
                        print("Respuesta Invalida, Vuelva a Intentar")
                elif pregunta_exportar == "N":
                    print("No se exporto ningun archivo")
                else:
                    print("Respuesta Invalida, Vuelva a Intentar")
        elif metodo == "3":
            reporte_generos()
        elif metodo == "4":
            tipo = 3       
            anio = list(diccionario.items())
            anio_busqueda= input("ingrese el año de publicacion del libro a desear: ")
            try:

                anio_datetime = datetime.datetime.strptime(anio_busqueda, "%Y").year

                print(f'+{"-"*98}+')
                print(f"|{'Título':^15}|{'Autor':^15}|{'Género':^12}|{'ISBN':^13}|{'Año de publicación':^18}|{'Fecha de adquisición':^20}|")
                print(f'+{"-"*98}+')
                coincidenica = 0
                for clave, datos in anio:
                    if anio_datetime == diccionario[clave][4]:        
                        print(f'|{datos[0]:^15}|{datos[1]:^15}|{datos[2]:^12}|{datos[3]:^13}|{datos[4]:^18}|{datos[5]:^20}|')
                        print(f'+{"-"*98}+')
                        dicc[clave]=[datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]]
                        coincidencia += 1
                if coincidenica == 0:
                    print("no hay libros en el año")

                while True:
                    pregunta_exportar = input("¿Quieres exportar tu reporte?\n(S o N)\n-->").upper()
                    if pregunta_exportar == "S":
                        pregunta_seleccion = int(input("¿De cual manera lo quiere exportar?\n \
                                                1) CSV \n2) Excel\n-->"))
                        if pregunta_seleccion == 1:
                            print("Aqui va el CSV")
                            break
                        elif pregunta_seleccion == 2:
                            importar_excel(dicc,tipo)
                            break
                        else:
                            print("Respuesta Invalida, Vuelva a Intentar")
                    elif pregunta_exportar == "N":
                        print("No se exporto ningun archivo")
                    else:
                        print("Respuesta Invalida, Vuelva a Intentar")
            except ValueError:
                print(f"El valor proporcionado ({anio_busqueda}) no es compatible con la operación solicitada")
                
        elif metodo == "5":
            break
        else:
            print("La opción ingresada no es válida, intenta de nuevo: ")
            continue
    


