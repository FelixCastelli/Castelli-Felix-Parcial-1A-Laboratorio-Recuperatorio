import random
import re
import os


def leer_csv(ruta: str):
    lista_retorno = []
    lista_aux = []
    with open(ruta, encoding='utf-8') as file:

        for i in file:
            i = i.replace("\n", "")
            lista_aux = i.split(',')
            lista_retorno.append(lista_aux)
        lista_retorno.pop(0)
        return lista_retorno


def transformar_lista_a_dict(ruta: str, lista: list, key: str, key2: str, key3: str, key4: str):
    lista = list(map(lambda peli: {key: peli[0], key2: peli[1], key3: peli[2], key4: random.randint(100, 240)}, leer_csv(ruta)))
    print("==================================")
    print("La lista se guardó correctamente")
    print("==================================")
    return lista


def imprimir_lista(lista: list):
    for pelicula in lista:
        print(f"""
ID: {pelicula["id_peli"]}
Titulo: {pelicula["titulo"]}
Genero: {pelicula["genero"]}
Duracion: {pelicula["duracion"]}
""")
        print("--------------------------------")


def asignar_tiempos(lista: list, ruta: str):
    with open(ruta, 'w', encoding='utf-8') as file:
        for peli in lista:
            lista_nuevos_datos = f"{peli['id_peli']},{peli['titulo']},{peli['genero']},{peli['duracion']}\n"
            file.write(lista_nuevos_datos)
        
        for peli in lista:
            print(f"""
Titulo: {peli["titulo"]}
Duracion: {peli["duracion"]}
""")
            print("-----------------------")


def filtrar_por_tipo(ruta: str, lista: list, key: str):
    peliculas_encontradas = []

    while True:
        genero = input("Ingrese el genero que quiere buscar: ").capitalize()

        for peli in lista:
            if re.search(genero, peli[key]): 
                peliculas_encontradas.append(peli)

        if not peliculas_encontradas or genero == "":
            os.system("cls")
            print(f"No se encontraron peliculas del genero {genero}")
            break

        with open(ruta, 'w', encoding='utf-8') as file:
            for peli in lista:
                if peli[key] == genero:
                    peli_completa = f"{peli['id_peli'], peli['titulo'], peli['genero'], peli['duracion']}"
                    peli_completa = peli_completa.replace("'", '').replace("(", '').replace(")", '')
                    file.write(f"{peli_completa}\n")
            print(f"Archivo de peliculas del genero {genero} creado con exito")
            break


def mostrar_duraciones_ordenadas(lista: list, key: str, key2: str):
    tam = len(lista)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][key] > lista[j][key]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

            if lista[i][key] == lista[j][key]:
                if lista[i][key2] < lista[j][key2]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    print("==============================================================================================")
    print("Peliculas ordenadas por genero (A-Z), (peliculas de mismo genero estan ordenadas por duracion): ")
    print("==============================================================================================")

    for peli in lista:
        print(f"""
ID: {peli["id_peli"]}
Titulo: {peli["titulo"]}
Genero: {peli[key]}
Duracion: {peli[key2]}
""")
        print("---------------------------------------------------------------------------------------")
    return lista


def guardar_peliculas(ruta: str, lista: str):
    file = open(ruta, 'a', encoding='utf-8')

    for peli in lista:
        file.write(f"""
ID: {peli['id_peli']}
Titulo: {peli['titulo']}
Genero: {peli['genero']}
Duracion: {peli['duracion']}
""")
        file.write("-----------------------------\n")

    print("=========================================")
    print("El archivo de texto fue creado con exito")
    print("=========================================")