#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

DMS = '''asdljdkjfbkjvb40° 26' 46" N sdfkjdfjvbdjfvhb79° 58' 56" Wskjdckjdfvbjhfbv'''
DDM = "40° 26.767' N 79° 58.933' W"
DD = "40.446° N 79.982° W"
geonameLatLong = "45.333333 29.666667,45.468983 28.207403"
geonameDMS = "45:20:00N 29:40:00E,45:28:08N 28:12:27E"

# patternDD = "(\d+\.\d+[°|\s]?\s*[NSEW]?)"
# patternDDM = "(\d+[°|\s]?\s*\d+\.\d+\s?[]\x27[]\s+[NSEW]?)"
# patternDMS = "(\d+[°|\s]?\s+\d+[']?\s+\d+[\"]?\s+[NSWE]?)"
# patternDD2 = "(\d+\.\d+)"
# patterngeonamesDMS = "\d+\:\d+\:\d+[NSWE]?"

class regexCoordinates(object):
    def __init__(self):
        self.patternDD = "(\d+\.\d+[°|\s]?\s*[NSEW]?)"
        self.patternDDM = "(\d+[°|\s]?\s*\d+\.\d+\s?[]\x27[]\s+[NSEW]?)"
        self.patternDMS = "(\d+[°|\s]?\s+\d+[']?\s+\d+[\"]?\s+[NSWE]?)"
        self.patterngeonamesLatLong = "(\d+\.\d+)"
        self.patterngeonamesDMS = "\d+\:\d+\:\d+[NSWE]?"
        self.listaCoordonate = []

    def coordDMS(self,string):
        self.string = string.decode('utf-8')
        self.coordonate = re.findall(self.patternDMS,self.string)
        for i in self.coordonate:
            self.listaCoordonate.append(i)
        for i in self.listaCoordonate:
            print i.encode(encoding="utf-8")

    def coordDDM(self,string):
        self.string = string.decode('utf-8')
        self.coordonate = re.findall(self.patternDDM,self.string)
        for i in self.coordonate:
            self.listaCoordonate.append(i)
        for i in self.listaCoordonate:
            print i.encode(encoding="utf-8")

    def coordDD(self,string):
        self.string = string.decode('utf-8')
        self.coordonate = re.findall(self.patternDD, self.string)
        for i in self.coordonate:
            self.listaCoordonate.append(i)
        for i in self.listaCoordonate:
            print i.encode(encoding="utf-8")

    def geonamesLatLong(self,string):
        self.string = string.decode('utf-8')
        self.coordonate = re.findall(self.patterngeonamesLatLong,self.string)
        for i in self.coordonate:
            self.listaCoordonate.append(i)
        for i in self.listaCoordonate:
            print i.encode(encoding="utf-8")

    def geonamesDMS(self,string):
        self.string = string.decode('utf-8')
        self.coordonate = re.findall(self.patterngeonamesDMS,self.string)
        for i in self.coordonate:
            self.listaCoordonate.append(i)
        for i in self.listaCoordonate:
            print i.encode(encoding="utf-8")

if __name__ == "__main__":
    xy = regexCoordinates()
    xy.geonamesDMS(geonameDMS)



