"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import time
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    t1=loadArtists(catalog)
    t2=loadArtworks(catalog)
    print("("+str(t1+t2)+")")
    
def loadArtists(catalog):

    start_time = time.process_time() 
    booksfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000  
    return elapsed_time_mseg     

def loadArtworks(catalog):

    start_time = time.process_time() 
    tagsfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg  
        
# Funciones de ordenamiento



# Funciones de consulta sobre el catálogo

def medioAntiguo(catalog,num,medio):
    return model.medioAntiguo(catalog,num,medio)

def ArtistsSize(catalog):
    return model.ArtistsSize(catalog)

def ArtworksSize(catalog):
    return model.ArtworksSize(catalog)

#Req 1

def crono_artistas(catalog,f_i,f_f):
    catalogo=catalog["Fecha Artistas"]
    return model.crono_artistas(catalogo,f_i,f_f)

#Req 3

def artista_tecnica(catalog,nombre):
    return model.artista_tecnica(catalog,nombre)

#Req 5

def transporteobras(catalog,depmuseo):
    return model.transporteobras(catalog,depmuseo)
