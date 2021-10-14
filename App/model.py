"""
 * Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Reto No.2 - MoMAs
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

# Construccion de modelos

def newCatalog():

    catalog = {}

    catalog['Artistas'] = mp.newMap(76,
                                   maptype='PROBING',
                                   loadfactor=4.0)

    catalog['Obras'] = mp.newMap(294,
                                   maptype='PROBING',
                                   loadfactor=4.0)

    catalog['Medios Obras'] = mp.newMap(maptype='CHAINING',loadfactor=0.80)

    catalog["Nacionalidad Artistas"] = mp.newMap(maptype='CHAINING',loadfactor=0.80)

    catalog["Fecha Artistas"]=mp.newMap(maptype='CHAINING',loadfactor=0.80)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    
    artistas=catalog["Nacionalidad Artistas"]
    artistas_fecha=catalog["Fecha Artistas"]
    mp.put(catalog['Artistas'], int(artist["ConstituentID"]), artist)
    add_map_bynationality(artistas,artist)
    add_map_bydate(artistas_fecha,artist)

def addArtwork (catalog, artwork):

    obras=catalog['Medios Obras']

    mp.put(catalog['Obras'], int(artwork["ObjectID"]), artwork)
    add_map_bymedium(obras,artwork)

def add_map_bymedium (obras,artwork):

    b=mp.contains(obras, artwork["Medium"])

    if b:
        if artwork["Medium"]!="":
            a=mp.get(obras,artwork["Medium"])
            a=me.getValue(a)
            lt.addLast(a,artwork)
        
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,artwork)
        mp.put(obras, artwork["Medium"],lista)

def add_map_bynationality (obras,artist):

    b=mp.contains(obras, artist["Nationality"])

    if b:
        if artist["Nationality"]!="":
            a=mp.get(obras,artist["Nationality"])
            a=me.getValue(a)
            lt.addLast(a,artist)
        
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,artist)
        mp.put(obras, artist["Nationality"],lista)

def add_map_bydate(obras,artist):
    b=mp.contains(obras, artist["BeginDate"])

    artista={"Nombre":artist["DisplayName"],
    "Nacimiento":artist["BeginDate"],
    "Falleciiento":artist["EndDate"],
    "Nacionalidad":artist["Nationality"],
    "Genero":artist["Gender"]}
    

    if b:
        a=mp.get(obras,artist["BeginDate"])
        a=me.getValue(a)
        lt.addLast(a,artista)
        
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,artista)
        mp.put(obras, artist["BeginDate"],lista)

# Funciones para creacion de datos

# Funciones de consulta

def medioAntiguo(catalogo,num,medio):
    print(medio)#Exhibition catalogue with one loose editioned print
    medium = mp.get(catalogo["Medios Obras"], medio)
    oldartwork = lt.newList("ARRAY_LIST")
    print(medium)
    if medium:
        lt.addLast(oldartwork, me.getValue(medium))

        
    return oldartwork

def ArtistsSize(catalog):
    return mp.size(catalog['Artistas'])

def ArtworksSize(catalog):
    return mp.size(catalog['Obras'])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# Req 1

def crono_artistas(catalog,anio_i,anio_f):
    tam=3
    not_full=True
    FIRST=[]
    LAST=[]
    f1=[]
    dic={"PRIMEROS ARTISTAS": FIRST,
        "ULTIMOS ARTISTAS":LAST,
        "TOTAL DE ARTISTAS":0}

    for i in range(anio_i,anio_f+1):
        exists=mp.contains(catalog,str(i))
        if exists:
            f1+=[str(i)]
            if len(f1)>3:
                f1.pop(0)
            dupla=mp.get(catalog,str(i))
            valor=me.getValue(dupla)
            tamanio=lt.size(valor)
            dic["TOTAL DE ARTISTAS"]+=tamanio

            if not_full:
                if tam>0:
                    for element in lt.iterator(valor):
                        dic["PRIMEROS ARTISTAS"].append(element)
                    tam-=tamanio
                else:
                    not_full=False

    dic=get_last_3(dic,catalog,f1)

    return dic
    
def get_last_3(dic,catalog,f1):
    not_full=True
    tam=3
    pos=len(f1)-1
    while not_full:
        if tam>0:        
            dupla=mp.get(catalog,f1[pos])
            valor2=me.getValue(dupla)
            for element in lt.iterator(valor2):
                dic["ULTIMOS ARTISTAS"].append(element)
            tam-=lt.size(valor2)
            pos-=1
        else:
            not_full=False
    return dic

# Req 2

