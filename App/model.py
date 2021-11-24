﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
from DISClib.ADT import graph as gr
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog():
    catalog = {'aeropuerto': None,
                'ida':None,
                'idayvuelta':None,
                'lista_rutas':None}

    catalog['aeropuerto'] = om.newMap('RBT',
                                     comparefunction=cmpaeropuerto)
    catalog["ciudades"]= mp.newMap(numelements= 300 ,maptype='PROBING',
                                     comparefunction=cmpaeropuerto)
    catalog['ida'] = gr.newGraph(datastructure="ADJ_LIST",directed=True,size=10,comparefunction=cmpaeropuerto)
    catalog['idayvuelta'] = gr.newGraph(datastructure="ADJ_LIST",directed=False,size=10,comparefunction=cmpaeropuerto)
    catalog['lista_rutas'] = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=None, key=None, filename=None, delimiter=",")
    return catalog


def cmpaero(city_1,city_2):  
    if city_1 == city_2:         
        return 0    
    elif city_1 > city_2:
        return 1 
    else:         
        return -1 

def cmpaeropuerto(llave,entry):
    llave_1=me.getKey(entry)
    if llave == llave_1:         
        return 0    
    elif llave > llave_1:
        return 1 
    else:         
        return -1


def addAeropuerto(catalog,aeropuerto):
    presente = om.contains(catalog["aeropuerto"], aeropuerto["IATA"])
    if not presente:
        lista=lt.newList()
        lt.addFirst(lista, aeropuerto)
        om.put(catalog["aeropuerto"],aeropuerto["IATA"],lista)
        
    else:
        nombre=aeropuerto["IATA"]
        entry = om.get(catalog["aeropuerto"], nombre)
        lista=me.getValue(entry)
        lt.addLast(lista, aeropuerto)

def addCiudad(catalog,ciudad):
    presente = mp.contains(catalog["ciudades"], ciudad["city"])
    if not presente:
        lista=lt.newList()
        lt.addFirst(lista, ciudad)
        mp.put(catalog["ciudades"],ciudad["city"],lista)
        
    else:
        nombre=ciudad["city"]
        entry = mp.get(catalog["ciudades"], nombre)
        lista=me.getValue(entry)
        lt.addLast(lista, ciudad)

def addVertice (catalog, vertice):
    if not gr.containsVertex(catalog["ida"], vertice["IATA"]):
        gr.insertVertex(catalog["ida"], vertice["IATA"])

def addInfo (catalog, ruta):
    origen=ruta["Departure"]
    destino= ruta["Destination"]
    addVertice(catalog["ida"],origen)
    addVertice(catalog["ida"],destino)
    addArco(catalog["ida"],ruta)
    lt.addLast(catalog["lista_rutas"], ruta)


def addArco(catalog,aero):
    vertice_a=aero["Departure"]
    vertice_b=aero["Destination"]
    peso=aero["distance_km"]
    gr.addEdge(catalog["ida"],vertice_a,vertice_b,float(peso))
    

def addGraph(catalog):
    lista_ruta=catalog["lista_rutas"]
    for ruta_1 in lt.iterator(lista_ruta):
        origen_1= ruta_1["Departure"]
        destino_1= ruta_1["Destination"]
        for ruta_2 in lt.iterator(lista_ruta):
            origen_2= ruta_2["Departure"]
            destino_2= ruta_2["Destination"] 
            if origen_1==destino_2 and origen_2 == destino_1:
                
                addVertice(catalog["idayvuelta"], origen_1)
                addVertice(catalog["idayvuelta"], origen_2)
                addArco(catalog["idayvuelta"],ruta_1)

def totalAeropuertos(catalog):
    return gr.numVertices(catalog["ida"])

def totalAeropuertos_2(catalog):
    return gr.numVertices(catalog["idayvuelta"])

def total_rutas_aereas(catalog):
    return gr.numEdges(catalog["ida"])


def total_rutas_aereas_2(catalog):
    return gr.numEdges(catalog["idayvuelta"])

def total_ciudades(catalog):
    lista=mp.valueSet(catalog["ciudades"])
    return lt.size(lista)




# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
