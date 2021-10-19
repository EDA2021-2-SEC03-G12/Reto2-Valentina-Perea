"""
 * Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Reto No.2 - MoMAs
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from DISClib.DataStructures.singlelinkedlist import newList
import config as cf
import time
import re
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as s
assert cf

# Construccion de modelos

def newCatalog():

    catalog = {}

    catalog['Artistas'] = mp.newMap(15225,
                                   maptype='PROBING',
                                   loadfactor=4.0)

    catalog['Obras'] = mp.newMap(150682,
                                   maptype='PROBING',
                                   loadfactor=4.0)

    catalog['Obras Artista'] = mp.newMap(15225,maptype='CHAINING',loadfactor=0.4)

    catalog["Nacionalidad Artistas"] = mp.newMap(15225,maptype='CHAINING',loadfactor=0.4)

    catalog["Fecha Artistas"]=mp.newMap(maptype='CHAINING',loadfactor=0.4)

    catalog["Por Departamento"]=mp.newMap(maptype='CHAINING',loadfactor=0.4)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    
    artistas=catalog["Nacionalidad Artistas"]
    artistas_fecha=catalog["Fecha Artistas"]
    mp.put(catalog['Artistas'], artist["DisplayName"], artist)
    add_map_bynationality(artistas,artist)
    add_map_bydate(artistas_fecha,artist)

def addArtwork (catalog, artwork):

    obras=catalog['Obras Artista']
    obras2=catalog["Por Departamento"]

    mp.put(catalog['Obras'], int(artwork["ObjectID"]), artwork)
    add_map_byauthorID(obras,artwork)
    add_map_bydep(obras2,artwork)

def add_map_byauthorID (obras,artwork):

    dic={"TITULO ": artwork["Title"],
    "FECHA ":  artwork["Date"],
    "TECNICA ": artwork["Medium"],
    "DIMENSIONES ": artwork["Dimensions"]}

    element=artwork["ConstituentID"].strip('[]')
    element=element.split(",")

    for authorID in element:
        authorID=authorID.strip()
        b=mp.contains(obras, authorID)

        if b:
            a=mp.get(obras,authorID)
            a=me.getValue(a)
            lt.addLast(a,dic)
            
        else:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista,dic)
            mp.put(obras,authorID,lista)

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
    "Fallecimento":artist["EndDate"],
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

def add_map_bydep(obras,artwork):

    dic={"TITULO ": artwork["Title"],
    "ARTISTA ": artwork["ConstituentID"],
    "CLASIFICACION ":artwork["Classification"],
    "FECHA ": artwork["Date"],
    "TECNICA ": artwork["Medium"],
    "DIMENSIONES ": artwork["Dimensions"],
    "MEDIDAS ": [artwork['Circumference (cm)'],artwork['Depth (cm)'],artwork['Diameter (cm)'],
    artwork['Height (cm)'],artwork['Length (cm)'],artwork['Weight (kg)'],artwork['Width (cm)'],
    artwork['Seat Height (cm)']],
    "PESO": artwork['Weight (kg)']}

    b=mp.contains(obras,artwork["Department"])

    if b:
        a=mp.get(obras,artwork["Department"])
        a=me.getValue(a)
        lt.addLast(a,dic)
        
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,dic)
        mp.put(obras, artwork["Department"],lista)


# Funciones para creacion de datos
def sort_by_num(a,b):
    if a!=0:
        a=int(a)
    if b!=0:
        b=int(a)
    
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
                
                for element in lt.iterator(valor):
                    dic["PRIMEROS ARTISTAS"].append(element)
                    tam-=1
                    if tam==0:
                        not_full=False
                        break

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
                tam-=1
                if tam==0:
                    not_full=False
                    break 
            pos-=1
    return dic

# Req 3

def artista_tecnica(catalog,nombre):

    exists=mp.contains(catalog["Artistas"],nombre)
    value=""

    a={"TOTALOBRAS":"NO HAY OBRAS","TOTALTECNICAS":0,
            "TECNICATOP":"","OBRAS POR LA TECNICA":0}
    dic=mp.newMap()

    if exists:
        value=mp.get(catalog["Artistas"],nombre)
        value=me.getValue(value)
        value=value["ConstituentID"]
        value=value.strip()

    exists=mp.contains(catalog["Obras Artista"],value)

    if exists:
        value=mp.get(catalog["Obras Artista"],value)
        value=me.getValue(value)
        a["TOTALOBRAS"]=lt.size(value)

        for obra in lt.iterator(value):
            exists=mp.contains(dic,obra["TECNICA "])

            if exists:
                
                b=mp.get(dic,obra["TECNICA "])
                b=me.getValue(b)
                lt.addLast(b,obra)     

            else:  

                lista=lt.newList("ARRAY_LIST")
                lt.addLast(lista,obra)
                mp.put(dic, obra["TECNICA "], lista)
    
        value=0
        key=obra["TECNICA "]
        llaves=mp.keySet(dic)
        for medio in lt.iterator(llaves):
            val=mp.get(dic,medio)
            val=me.getValue(val)
            longitud=lt.size(val)
            if longitud>=value:
                value=longitud
                key=medio
        a["TOTALTECNICAS"]=lt.size(dic)
        a["TECNICATOP"]=key
        a["OBRAS POR LA TECNICA"]=me.getValue(mp.get(dic,key))

    return a

#Req 5

def transporteobras(catalog,depmuseo):

    obrasdep=lt.newList()
    sumattl=0
    pesottl=0

    if mp.contains(catalog["Por Departamento"],depmuseo):

        info=mp.get(catalog["Por Departamento"],depmuseo)
        info=me.getValue(info)

        for obra in lt.iterator(info):
                calculos=sumasdeobras(obra)
                obra["COSTO"]=calculos
                sumattl+=calculos
                pesopieza=obra["PESO"].strip()
                if pesopieza!="":
                    pesottl+=float(pesopieza)
    
    obrasantiguas5=s.sort(info,cmpfunction=compareold)
    obrasantiguas5=lt.subList(obrasantiguas5,1,5)

    obrascostosas=s.sort(info,cmpfunction=compareprice)
    obrascostosas=lt.subList(obrascostosas,1,5) 

    return {"TOTAL OBRAS":lt.size(info),"ESTIMADO USD": sumattl,"PESO ESTIMADO":pesottl,
    "OBRAS ANTIGUAS":obrasantiguas5, "OBRAS COSTOSAS": obrascostosas}

def sumasdeobras(obra):
    d=obra["DIMENSIONES "]
    a=48.00
    if d!= "":
        d=d.replace('x',"*")
        d=d.replace('×',"*")
        num=[float(s) for s in re.findall(r'-?\d+\.?\d*', d)]
        if len(num)==8:
            cm=num[6:8]
            a=centimeter(cm)
        elif len(num)==16:
            cm=num[6:8]
            pcm=centimeter(cm)
            cm1=num[14:16]
            pcm1=centimeter(cm1)
            a=max(pcm,pcm1)
        elif len(num)==4:
            cm=num[2:4]
            a=centimeter(cm)
        elif len(num)==6:
            cm=num[4:6]
            a=centimeter(cm)
        elif len(num)==14:
            cm=num[7:9]
            cm1=num[12:14]
            pcm=centimeter(cm)
            pcm1=centimeter(cm1)
            a=max(pcm,pcm1)
        elif len(num)==12:
            cm3=num[9:12]
            a=centimeter(cm3)
        elif len(num)==9:
            cm3=num[6:9]
            a=centimeter(cm3)
                
    return a

def centimeter(cm:list):
    costo=72.00/((cm[0]*cm[1])/100)
    return costo

def centimetercubic(cm:list):
    costo=72.00/((cm[0]*cm[1]*cm[2])/100)
    return costo

def compareprice(PRICE1,PRICE2):
    return PRICE1["COSTO"]<PRICE2["COSTO"]

def compareold(obra1,obra2):
    a=obra1["FECHA "]
    b=obra2["FECHA "]
    val=2020
    val1=2020

    if a!="":
        if (len(a)==11) or ("c" in a):
            val=(a[-4:])
        elif "-" in a:
            val=(a[:5])
        
    if b!="":
        if (len(b)==11) or ("c" in b):
            val1=(b[-4:])
        elif "-" in b:
            val1=(val[:5])
        
    return int(val)>int(val1)