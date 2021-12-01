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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from App.controller import elegir_ciudad_2
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
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
                'components': None,
                'paths': None
                }

    catalog['aeropuerto'] = mp.newMap(numelements= 300 ,maptype='PROBING',
                                     comparefunction=cmpaeropuerto)
    catalog["ciudades"]= mp.newMap(numelements= 300 ,maptype='PROBING',
                                     comparefunction=cmpaeropuerto)
    catalog['ida'] = gr.newGraph(datastructure="ADJ_LIST",directed=True,size=10,comparefunction=cmpaeropuerto)
    catalog['idayvuelta'] = gr.newGraph(datastructure="ADJ_LIST",directed=False,size=10,comparefunction=cmpaeropuerto)
    catalog["ciudad"]= mp.newMap(numelements= 300 ,maptype='PROBING',
                                     comparefunction=cmpaeropuerto)
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

def alfabetica(uno,dos):
    if uno["City"]<dos["City"]:
        return True


def addAeropuerto(catalog,aeropuerto):
    presente = mp.contains(catalog["aeropuerto"], aeropuerto["City"])
    if not presente:
        lista=lt.newList()
        lt.addFirst(lista, aeropuerto)
        mp.put(catalog["aeropuerto"],aeropuerto["City"],lista)
        
    else:
        nombre=aeropuerto["City"]
        entry = mp.get(catalog["aeropuerto"], nombre)
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


def addArco(catalog,aero):
    vertice_a=aero["Departure"]
    vertice_b=aero["Destination"]
    peso=aero["distance_km"]
    gr.addEdge(catalog["ida"],vertice_a,vertice_b,float(peso))
    if gr.getEdge(catalog["ida"],vertice_b,vertice_a)!=None:
        if not gr.containsVertex(catalog["idayvuelta"], vertice_b):
            gr.insertVertex(catalog["idayvuelta"], vertice_b)
        if not gr.containsVertex(catalog["idayvuelta"], vertice_a):
            gr.insertVertex(catalog["idayvuelta"], vertice_a)    
        gr.addEdge(catalog["idayvuelta"],vertice_a,vertice_b)


    


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


def requerimiento_1(catalog):
    lista_aeropuertos=lt.newList()
    lista_vertices=gr.vertices(catalog["ida"])
    mayor=0
    i=1
    while i<=lt.size(lista_vertices):
        vertice=lt.getElement(lista_vertices,i)
        entradas=gr.degree(catalog["ida"],vertice)
        salidas=gr.outdegree(catalog["ida"],vertice)
        total=entradas+salidas

        if total>mayor:
            mayor=total
            lista_aeropuertos=lt.newList()
            lt.addLast(lista_aeropuertos,vertice)
        elif total==mayor:
            lt.addLast(lista_aeropuertos,vertice)

        i+=1
    return lista_aeropuertos

#Requerimiento 3

def minimumCostPaths(catalog, ciudad_origen):
    """
    Calcula los caminos de costo mínimo desde la estacion initialStation
    a todos los demas vertices del grafo
    """
    catalog['paths'] = djk.Dijkstra(catalog['ida'], ciudad_origen)
    return catalog


def minimumCostPath(catalog, ciudad_destino):
    """
    Retorna el camino de costo minimo entre la estacion de inicio
    y la estacion destino
    Se debe ejecutar primero la funcion minimumCostPaths
    """
    path = djk.pathTo(catalog['paths'], ciudad_destino)
    return path
    
def elegir_ciudad_origen(catalog, ciudad_origen):
    lista_origen=mp.get(catalog["aeropuerto"],ciudad_origen)
    lista_origen=me.getValue(lista_origen)
    return lista_origen

def elegir_ciudad_destino(catalog, ciudad_destino):
    lista_destino=mp.get(catalog["aeropuerto"],ciudad_destino)
    lista_destino=me.getValue(lista_destino)
    return lista_destino

def requerimiento_3(catalog, ciudad_origen, ciudad_destino):
    lista_origen=lt.newList()
    lista_final=lt.newList()
    aerpuerto_ciudad_1=elegir_ciudad_origen(catalog, ciudad_origen)
    camino=None
    aeropuerto_ciudad_2=elegir_ciudad_destino(catalog,ciudad_destino) 
    lista_aeropuerto=mp.keySet(catalog["aeropuerto"])
    for i in range(1,lt.size(aerpuerto_ciudad_1)+1):
        aeropuerto=lt.getElement(aerpuerto_ciudad_1,i)
        print(aeropuerto)
        ida=djk.Dijkstra(catalog["ida"],aeropuerto["IATA"])
        for j in range(1,lt.size(aeropuerto_ciudad_2)+1):

            aeropuerto_2=lt.getElement(aeropuerto_ciudad_2,j)
            print(aeropuerto_2)
            camino=djk.pathTo(ida,aeropuerto_2["IATA"])
        
    return camino


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
