from consulta_D_titulo import Consulta_de_titulo

def consulta_Y_reporte():
    while True:    
        print("""  
    +-----------------------------------------+
    |          Consultas y reportes.          |
    +=========================================+
    | Consulta por Título           |    1    |
    +-----------------------------------------+
    | Reportes                      |    2    |   
    +-----------------------------------------+
    | Volver al menú principal      |    3    |   
    +-----------------------------------------+""")
        opcion_menu_consultas = input("Ingresa la opción que desees --> ")
        if opcion_menu_consultas == "1":
            Consulta_de_titulo()
        elif opcion_menu_consultas == "2":
            continue
        elif opcion_menu_consultas =="3":
            break
        else:
            print("La opción ingresada no existe, intente de nuevo. ")
            continue


