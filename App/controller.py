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
import model
import csv

def initCatalog():
   
    catalog = model.newCatalog()
    return catalog

def loadData(catalog):
    loadAero(catalog)
    loadRoutes(catalog)
    loadCity(catalog)
    loadAeropuerto(catalog)
    loadIata(catalog)

def loadAero(catalog):
    ufosfile = cf.data_dir + 'Skylines/airports_full.csv'
    input_file = csv.DictReader(open(ufosfile, encoding='utf-8'))
    for aero in input_file:
        model.addVertice(catalog, aero)

def loadRoutes(catalog):
    ufosfile = cf.data_dir + 'Skylines/routes_full.csv'
    input_file = csv.DictReader(open(ufosfile, encoding='utf-8'))
    for aero in input_file:
        model.addArco(catalog, aero)

def loadCity(catalog):
    ufosfile = cf.data_dir + 'Skylines/worldcities.csv'
    input_file = csv.DictReader(open(ufosfile, encoding='utf-8'))
    for aero in input_file:
        model.addCiudad(catalog, aero)

def loadAeropuerto(catalog):
    ufosfile = cf.data_dir + 'Skylines/airports_full.csv'
    input_file = csv.DictReader(open(ufosfile, encoding='utf-8'))
    for aero in input_file:
        model.addAeropuerto(catalog, aero)

def loadIata(catalog):
    ufosfile = cf.data_dir + 'Skylines/airports_full.csv'
    input_file = csv.DictReader(open(ufosfile, encoding='utf-8'))
    for aero in input_file:
        model.addIATA(catalog, aero)

def totalAeropuertos(catalog):
    return model.totalAeropuertos(catalog)

def totalAeropuertos2(catalog):
    return model.totalAeropuertos_2(catalog)

def total_rutas(catalog):
    return model.total_rutas_aereas(catalog)

def total_rutas2(catalog):
    return model.total_rutas_aereas_2(catalog)

def total_ciudades(catalog):
    return model.total_ciudades(catalog)

def requerimiento_uno(catalog):
    return model.requerimiento_1(catalog)

def requerimiento_dos(catalog,ciudad_1,ciudad_2):
    return model.requerimiento_2(catalog,ciudad_1,ciudad_2)

def elegir_ciudad_1(catalog, ciudad_origen):
    return model.elegir_ciudad_origen(catalog, ciudad_origen)

def elegir_ciudad_2(catalog, ciudad_destino):
    return model.elegir_ciudad_destino(catalog,ciudad_destino)
    
def requerimiento_3(catalog,ciudad_origen,ciudad_destino):
    return model.requerimiento_3(catalog,ciudad_origen,ciudad_destino)

def requerimiento_4(catalog,origen,cant_millas):
    return model.requerimiento_4(catalog,origen,cant_millas)
    
def requerimiento_5(catalog,codigo):
    return model.requerimiento_5(catalog,codigo)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
