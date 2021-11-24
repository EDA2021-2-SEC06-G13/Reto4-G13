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
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gr


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar puntos de interconexión aérea")
    print("3- Encontrar clústeres de tráfico aéreo")
    print("4- Encontrar la ruta más corta entre ciudades")
    print("5-  Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aeropuerto cerrado")

catalog = None

def initCatalog():
    
    return controller.initCatalog()

def loadData(catalog):
     return controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        loadData(catalog)
        total_aeropuerto= controller.totalAeropuertos(catalog)
        totalAeropuertos2=controller.totalAeropuertos2(catalog)
        total_rutasaereas= controller.total_rutas(catalog)
        total_rutasaereas2= controller.total_rutas2(catalog)
        print("El total de aeropuertos es "+ str(total_aeropuerto) + " en el grafo dirigido y del grafo no dirigido: " + str(totalAeropuertos2))
        print("El total de rutas aereas es "+ str(total_rutasaereas)+ " en el grafo dirigido y del grafo no dirigido: " + str(total_rutasaereas2))
        """sumatoria=0
        info=mp.valueSet(catalog["ciudades"])
        for i in range(1,lt.size(info)+1):
            cant_ciudad=lt.getElement(info,i)
            cantidad=lt.size(cant_ciudad)
            sumatoria+=cantidad
        print("El total de ciudades es: "+ str(sumatoria))
"""


    elif int(inputs[0]) == 2:
        r=controller.requerimiento_uno(catalog)
        print("El/Los aeropuerto(s) que sirven como punto de interconexion a mas rutas es/son ")
        i=1
        while i<=lt.size(r):
            aeropuerto=lt.getElement(r,i)
            print(aeropuerto)
            i+=1
        
        
    elif int(inputs[0]) == 3:
        ciudad_1=input("Ingrese el codigo IATA del aeropuerto 1")
        ciudad_2=input("Ingrese el codigo IATA del aeropuerto 2")
        r=controller.requerimiento_dos(catalog,ciudad_1,ciudad_2)
        

    else:
        sys.exit(0)
sys.exit(0)
