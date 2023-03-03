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
            continue 
        elif tipo_consulta=="2":
            continue
        elif tipo_consulta =="3":
            consulta_Y_reportes()
        else:
            print("Error la opcion ingresada no existe, intentelo de nuevo")
            continue
        break