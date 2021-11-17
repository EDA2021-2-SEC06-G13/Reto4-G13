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
    catalog = {'aeropuerto': None}

    catalog['aeropuerto'] = gr.newGraph(datastructure="ADJ_LIST",directed=False,size=10,comparefunction=cmpaero)
    catalog['ida-vuelta'] = gr.newGraph(datastructure="ADJ_LIST",directed=False,size=10,comparefunction=cmpaero)

    return catalog


def cmpaero(city_1,city_2):  
    if city_1 == city_2:         
        return 0     
    else:         
        return 1     


def addVertice(catalog,aeropuerto):
    gr.insertVertex(catalog["aeropuerto"],aeropuerto["IATA"])

def addArco(catalog,aero):
    vertice_a=aero["Departure"]
    vertice_b=aero["Destination"]
    peso=aero["distance_km"]
    gr.addEdge(catalog["aeropuerto"],vertice_a,vertice_b,float(peso))

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
