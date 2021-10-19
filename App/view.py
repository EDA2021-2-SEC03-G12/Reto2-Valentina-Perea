"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#MENU

def printMenu():
    print("___________________________________________")
    print("    BIENVENIDO AL CATALOGO DE MoMA'S")
    print("___________________________________________")
    print("")
    print("1 ) Cargar información en el catálogo")
    print("2 ) Listar cronológicamente los artistas")
    print("3 ) Listar cronológicamente las adquisiciones")
    print("4 ) Clasificar las obras de un artista por técnica")
    print("5 ) Clasificar las obras por la nacionalidad de sus creadores")
    print("6 ) Transportar obras de un departamento ")
    print("7 ) Encontrar los artistas más prolíficos del museo ")
    print("0 ) Salir")
    print("")
    print("___________________________________________")

#CARGA DE DATOS [1]
def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

catalog = None

#REQ1 [2]

def crono_artistas(catalogo):
    f_i=int(input("Ingrese la fecha minima de busqueda: "))
    f_f=int(input("Ingrese la fecha maxima de busqueda: "))
    info=controller.crono_artistas(catalogo,f_i,f_f)
    return info

#REQ3 [4]

def artista_tecnica(catalogo):
    nombre=(input("Ingrese el nombre del artista que desea consultar: "))
    return controller.artista_tecnica(catalogo,nombre)

#REQ5 [6]
def transporteobras (catalog):
    dep=input("Ingrese el departamento que desee buscar: ")
    return controller.transporteobras(catalog,dep)

def medioAntiguo(catalog):
    num=int(input("Ingrese el numero de obras que quiere ver: "))
    medio=input("Ingrese el medio que desea consultar: ")
    antiguos=controller.medioAntiguo(catalog,num,medio)
    return antiguos

#MENU PRINCIPAL

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....") 
        catalog = initCatalog()
        loadData(catalog)
        print(" ")
        print('Artistas cargadas: ' + str(controller.ArtistsSize(catalog)))
        print(" ")
        print('Obras cargadas: ' + str(controller.ArtworksSize(catalog)))
        print(" ")

    elif int(inputs[0]) == 2:
        dic=crono_artistas(catalog)
        for key,val in dic.items():
            print(key,val)

    elif int(inputs[0]) == 4:
        dic=artista_tecnica(catalog)
        for key,val in dic.items():
            print(key,val)

    elif int(inputs[0]) == 6:
        dic=transporteobras(catalog)
        for key,val in dic.items():
            print(key,val)

    else:
        sys.exit(0)

sys.exit(0)
