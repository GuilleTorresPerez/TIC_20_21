# -*- coding: cp1252 -*-
def sumaGaus():
    finalNumber=input ("Inserte el número por favor")
    sumaAcumulada=0

    for cont in range(1,finalNumber+1):
       if(cont%2==0):
           sumaAcumulada = sumaAcumulada+cont

    print "La suma de los números hasta ",finalNumber
    print "= ", sumaAcumulada

sumaGaus()
