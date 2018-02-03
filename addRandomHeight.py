import arcpy
import random

def addHeight(suprafata, inaltime):
    if suprafata <= 500:
        inaltime = random.choice([3,6])
    elif suprafata > 500 and suprafata <= 1500:
        inaltime = random.choice([9,15])
    elif suprafata > 1500 and suprafata <= 4000:
        inaltime = random.choice([18,21,24,27,30])
    elif suprafata > 4000 and suprafata <= 8000:
        inaltime = random.choice([33,37,41,44])
    elif suprafata > 8000 and suprafata <= 18000:
        inaltime = random.choice([42,45,48])
    elif suprafata > 18000 and suprafata <= 35000:
        inaltime = random.choice([51,55,60])
    elif suprafata > 35000 and suprafata <= 60000:
        inaltime = random.choice([63,66,69,72,75])
    else:
        inaltime = random.choice([78,81,85,90])
    return inaltime

locatie = "input_location"
featureClass = "CladiriWGS"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = locatie
# campuri = arcpy.ListFields(featureClass)
# for camp in campuri:
#     print camp.name
with arcpy.da.UpdateCursor(featureClass,["Suprafata_m2", "Height"]) as cursor:
    for row in cursor:
        row[1] = addHeight(row[0], row[1])
        cursor.updateRow(row)




