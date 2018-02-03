#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Experto en Desarrollo GIS 2017/2018
# Analisis espacial con Python
# Python avanzado
#
# Ejercicios complementarios
# Autor: Ionut Alixandroae
# Fecha: 30/01/2018

"""
Importacion de modulos requeridos
"""
import requests, arcpy, csv

def peticionesArcGISServer(serviceURl):
    """
    Funcion para hacer peticiones a servicios de ArcGIS Server.
    La funcion imprime data de servicio como JSON si despues
    el numero total de entidades
    :param serviceURl: URl de servicio ArcGIS Server
    :return: No devuelve nada
    """
    params = {"where": "1=1", "f":"pjson"}
    data = requests.get(serviceURl + "/query", params)
    count = 0
    for feature in data.json()["features"]:
        count += 1

    print data.json()
    print "Numero total de entidades: {0}".format(count)
    

def printAreaAndTotalArea(featureClassPath):
    """
    Funcion para trabajar con geometria.
    La funcion imprime el area para cada entidad y
    despues imprime area total
    :param featureClassPath: Path de la FeatureClass
    :return: No devuelve nada
    """
    with arcpy.da.SearchCursor(featureClassPath, ["SHAPE@AREA"]) as cursor:
        totalArea = 0
        featureId = 0
        for row in cursor:
            totalArea += row[0]
            featureId += 1
            print "Entidad {0} tiene una area de {1} metros cuadrados".format(featureId, row[0])
        print "Area total por {0} entidades : {1} metros cuadrados".format(featureId, totalArea)


def checkMxd(mapDocumentPath, reportPath):
    """
    Funcion para chequear las capas de un Mxd y escribe un raport en format .txt.
    La funcion cheque cuales capas son en Mxd, nombres de capas, workspace por las capas
    y si existe paths que aparezcan rotos
    :param mapDocumentPath:
    :param reportPath: Path para crear un rapor en format .txt
    :return: 2 listas, prima con los workspaces, y segunda con paths que aparezcan rotos
    """
    mxd = arcpy.mapping.MapDocument(mapDocumentPath)
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    brokenPathsList = []
    workspacesList = []
    with open(reportPath + "\Report.txt", "a+") as txt_file:
        txt_file.write("Capas en Mxd: " + mapDocumentPath)
        for layer in arcpy.mapping.ListLayers(df):
            print layer.name
            txt_file.write("\n\t" + layer.name + "\n")

        txt_file.write("\n\nWorkspaces en Mxd: " + mapDocumentPath)
        for layer in arcpy.mapping.ListLayers(df):
            print layer.dataSource
            txt_file.write("\n\t" + layer.dataSource + "\n")
            workspacesList.append(layer.dataSource)

        txt_file.write("\n\nCapas con paths que aparezcan rotos: ")
        for layer in arcpy.mapping.ListLayers(df):
            if layer.isBroken == True:
                print layer.isBroken
                txt_file.write("\n\t" + layer.name + "\n")
                brokenPathsList.append(layer.name)

        print "0"
        txt_file.write("\n0")
    return workspacesList, brokenPathsList

def addDataFromCSV(featureClassPath, csvPath):
    """
    Funcion que consume un CSV para insertar datos en un Feature Class ya disponible en un GDB.
    La funcion comproba si la esquema de CSV es como la esquema de Feature Class sin campos como
    OBJECTID o SHAPE, para poder insertar datos.
    :param featureClassPath: Path de la Feature Class que sera actualizado
    :param csvPath: Path de la CSV con los datos de insertar
    :return: No devuelve nada
    """
    csvColumnNames = []
    featureClasssAttrNames = []
    with open(csvPath, "r") as csv:
        names = csv.next()[:-1].split(",")
        for name in names:
            csvColumnNames.append(name)
    fcFields = arcpy.ListFields(featureClassPath)
    for fieldName in fcFields:
        if fieldName.name != "OBJECTID" and fieldName.name != "SHAPE":
            featureClasssAttrNames.append(fieldName.name.encode("utf-8"))

    if (set(featureClasssAttrNames).issubset(csvColumnNames)) == True:
        insertCursorList = featureClasssAttrNames
        insertCursorList.append("SHAPE@X")
        insertCursorList.append("SHAPE@Y")
        with open(csvPath, "r") as _csv:
            _csv.readline()
            with arcpy.da.InsertCursor(featureClassPath,insertCursorList) as insertCursor:
                for row in _csv:
                    insertCursor.insertRow(row[:-1].split(","))

    else:
        print "La schema de CSV no es la misma con la schema de Feature Class"





if __name__ == "__main__":
    peticionesArcGISServer("https://services8.arcgis.com/DMKut3xZ61BEViT4/ArcGIS/rest/services/LocatieZimbri/FeatureServer/0")
    printAreaAndTotalArea("C:\Users\ialix\Desktop\Introduccion a Arcpy\GDB.gdb\Edificios")
    checkMxd("C:\Users\ialix\Desktop\Introduccion a Arcpy\Untitled.mxd","C:\Users\ialix\Desktop")
    addDataFromCSV("C:\Users\ialix\Desktop\Introduccion a Arcpy\GDB.gdb\PointsWGS84","C:\Users\ialix\Desktop\Introduccion a Arcpy\Coords.csv")