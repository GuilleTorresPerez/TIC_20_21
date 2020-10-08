#Introduce un nombre y un apellido
#Genera una contraseña a partir de 3 letras del nombre
#y 3 letras del apellido

def miContrasena():
    nombre=raw_input("Introduzca su nombre ")
    apellido=raw_input("Introduzca su apellido ")

    contrasenaNombre = nombre[-3:]+apellido[-3:]
    print "La contrasena es ", contrasenaNombre

miContrasena()
    
    
