import os
from funciones import *

ruta_csv = input("Ingrese la ruta del archivo csv que quiera leer: ")
ruta_csv_nueva = ("Primer Parcial\\movies_genero.csv")
ruta_txt = ("Primer Parcial\\movies_ordenadas.txt")

lista_dict_transformada = []
lista_ordenada = []
flag_lista_csv = False
flag_peliculas_ordenadas = False

def menu_opciones():
    os.system("cls")
    print("""
1- Cargar datos del archivo
2- Imprimir datos de las peliculas
3- Asignar tiempos
4- Crear archivo peliculas por genero
5- Ordenar peliculas
6- Guardar peliculas en nuevo archivo de texto
7- Salir""")
    
    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            while opcion < 1 or opcion > 7:
                opcion = int(input("ERROR, ingrese un numero que este dentro de las opciones: "))

            return opcion
        
        except ValueError:
            print("ERROR, eso no es un numero")
            os.system("pause")
            os.system("cls")


def elegir_opcion(opcion: int, lista_dict_transformada: list, lista_ordenada: list):
    salir = None
    match opcion:
        case 1:
            os.system("cls")
            lista_csv= leer_csv(ruta_csv)
            lista_dict_transformada = transformar_lista_a_dict(ruta_csv, lista_csv, "id_peli", "titulo", "genero", "duracion")
        case 2:
            os.system("cls")
            imprimir_lista(lista_dict_transformada)
        case 3:
            os.system("cls")
            asignar_tiempos(lista_dict_transformada, ruta_csv)
        case 4:
            os.system("cls")
            filtrar_por_tipo(ruta_csv_nueva, lista_dict_transformada, "genero")
        case 5:
            os.system("cls")
            lista_ordenada = mostrar_duraciones_ordenadas(lista_dict_transformada, "genero", "duracion")
        case 6:
            os.system("cls")
            guardar_peliculas(ruta_txt, lista_ordenada)
        case 7:
            os.system("cls")
            salir = input("Seguro que desea salir? s/n: ")
            pass
    return salir, lista_dict_transformada, lista_ordenada

while True:
    opcion = menu_opciones()

    try:
        open(ruta_csv, encoding='utf-8')

    except FileNotFoundError:
        print("ERROR, el archivo csv no existe")
        break

    if opcion == 7 or (opcion == 1 and not flag_lista_csv):
        flag_lista_csv = True

    if opcion == 5 and not flag_peliculas_ordenadas:
        flag_peliculas_ordenadas = True

    elif not flag_peliculas_ordenadas and opcion == 6:
        os.system("cls")
        print("Las peliculas no estan ordenadas, primero hay que ordenarlas")
        os.system("pause")
        continue

    elif not flag_lista_csv:
        os.system("cls")
        print("ERROR, La lista no está creada. Por favor, cree la lista antes de continuar")
        os.system("pause")
        continue

    opcion_salir, lista_dict_transformada, lista_ordenada = elegir_opcion(opcion, lista_dict_transformada, lista_ordenada)

    if opcion_salir == 's':
        os.system("cls")
        break
    os.system("pause")