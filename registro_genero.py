#from menu_principal import menu
def registro_genero():

    diccionario_genero={

    }
    while True:
        
        id_genero=max(diccionario_genero,default=0)+1
        try:
            ingresar_genero=input("ingresa el genero que deseas registrar --> ").upper()
        except ValueError:
            print("El tipo de error es invalido, intentalo de nuevo!!")
        except Exception:
            print("Hay un error, intentalo de nuevo ")
        else:
            diccionario_genero[id_genero]= ingresar_genero
            print(diccionario_genero)
            otro_genero=input('Deseas agregar otro genero? (S/N) --> ').upper()
            if otro_genero =="S":
                continue
            elif otro_genero=="N":
                print("fin")
                break
            else:
                print("La respuesta no es valida. ")
