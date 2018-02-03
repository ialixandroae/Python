import json,arcpy,urllib2,pprint

# adresa =

adresa = arcpy.GetParameterAsText(0)

class geocodareAdrese(object):
    restURL = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?SingleLine="
    replacementSpace = "%20"
    def __init__(self,a):
        self.a = a
        self.c = geocodareAdrese.restURL + self.a + "&outFields=*&f=pjson"

        self.cale = self.c.replace(" ",geocodareAdrese.replacementSpace)
        self.raspuns = urllib2.urlopen(self.cale)
        self.jsonAdrese = self.raspuns.read()
        arcpy.AddMessage(self.jsonAdrese)

obiect = geocodareAdrese(adresa)









