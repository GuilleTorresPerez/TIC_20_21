#Juego de adivinar un numero
import random

def juego():
    cantidad=input("Inserte la cantidad de numeros ")
    numero = random.randint(1,cantidad)
    
    print"Adivina el numero que he pensado desde el 1 hasta el",cantidad
    intento=input("elige el numero ")

    while intento!=numero:
        if intento>numero:
            print"Demasiado grande tonto"
            intento=input("escoge otro numero ")
        elif intento<numero:
            print"Demasiado pequeno tonto"
            intento=input("escoge otro numero ")

    print"Enhorabuena has acertado eres listisimo"
            
    
    

juego()
    
