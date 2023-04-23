    #Importaciones
import datetime
import openpyxl
from openpyxl.styles import Font
import openpyxl.worksheet.dimensions 

def importar_excel(diccionario,tipo):
    #Asignacion de Variables
    biblioteca = openpyxl.Workbook()
    numero = 2
    negritas = Font(bold = True)
    #dia = datetime.datetime.date()

    #Asignacio de Negritas y Nombres
    primera = biblioteca["Sheet"]
    primera.title = " dia "

    primera["A1"].value = "ID Libro"
    primera["A1"].font = negritas

    primera["B1"].value = "Titulo"
    primera["B1"].font = negritas

    primera["C1"].value = "Autor"
    primera["C1"].font = negritas

    primera["D1"].value = "Genero"
    primera["D1"].font = negritas

    primera["E1"].value = "ISBN"
    primera["E1"].font = negritas

    primera["F1"].value = "Fecha Publicacion"
    primera["F1"].font = negritas

    primera["G1"].value = "Fecha Adquisicion"
    primera["G1"].font = negritas

    #Ancho de Columnas
    primera.column_dimensions["A"].width = len(primera["A1"].value)
    primera.column_dimensions["B"].width = len(primera["B1"].value)
    primera.column_dimensions["C"].width = len(primera["C1"].value)
    primera.column_dimensions["D"].width = len(primera["D1"].value)
    primera.column_dimensions["E"].width = len(primera["E1"].value)
    primera.column_dimensions["F"].width = len(primera["F1"].value)
    primera.column_dimensions["G"].width = len(primera["G1"].value)


    #Ingreso de Datos
    print(diccionario)
    lista_dicc = list(diccionario.keys())
    for fila in lista_dicc:
        primera.cell(row=numero, column=1).value = fila
        primera.cell(row=numero, column=2).value = diccionario[fila][0]
        primera.cell(row=numero, column=3).value = diccionario[fila][1]
        primera.cell(row=numero, column=4).value = diccionario[fila][2]
        primera.cell(row=numero, column=5).value = diccionario[fila][3]
        primera.cell(row=numero, column=6).value = diccionario[fila][4]
        primera.cell(row=numero, column=7).value = diccionario[fila][5]
        numero += 1
    


    if tipo == 0:
        typo = "Catalogo Completo"
    elif tipo == 1:
        typo = "Por Autor"
    elif tipo == 2:
        typo = "Por Genero"
    elif tipo == 3:
        typo = "Por Año de Publicacion"

    #Guardar Archivo
    biblioteca.save(f"Reporte de Libros {typo} .xlsx")