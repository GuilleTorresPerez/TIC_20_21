# -*- coding: cp1252 -*-
def sumaGaus():
    finalNumber=100
    sumaAcumulada=0

    for cont in range(1,finalNumber+1):
        sumaAcumulada = sumaAcumulada+cont

    print "La suma de los números hasta ",finalNumber
    print "= ", sumaAcumulada

sumaGaus()
