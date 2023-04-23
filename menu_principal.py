from consultas_Y_reportes import consulta_Y_reporte 
from registro_libro import registro

def menu():
    print("""
                     __,                     ,__
                  __/==+\ J. FELIX GARCIA /+==\__
                    "  "`  ===============  '"  "
                                 ,   ,
                                /////|
                               ///// |
                              /////  |
                             /////   |
                            |~~~|    |
                            |===|    |
                            | P |    |
                            | Y |    |
                            | T |    |
                            | H |   /
                            | O |  /
                            | N | /
                            |===|/
                            '---'
            BIENVENIDO A LA BIBLIOTECA J. FELIX GARCIA
                           EL MENU
                1.- Registrar un nuevo ejemplar
                2.- Consultar y reportes
                3.- Salir""")
    print("\nNOTA: Para indicar que opcion desea realizar introduzca el numero de la opcion deseada")
    while True:
        try:
            opciones=int(input("\nIngrese la opcion que desee realizar: "))
            if opciones ==1:
                registro()
            elif opciones==2:
                consulta_Y_reporte()
            elif opciones ==3:
                break
            else:
                print("\nERROR la opcion elegida no existe.\n\nPor favor indique un numero disponible en el menú")
                continue
        except ValueError: 
            print("Hay un pequeño error de sintaxis, introduciste ua letra o un simbolo en lugar de un numero")
        except Exception:
            print("Error hay un error intentalo de nuevo")

        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
menu()
