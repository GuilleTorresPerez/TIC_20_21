#Escribe un programa que genere una contraseña

def password():
    nombre=raw_input("Introduce el nombre: ")
    apellido=raw_input("Introduce el apellido: ")
    print nombre," ", apellido, " eres el impostor?"
    print "Tu nombre empieza por la letra ",nombre[0]
    print "Las tres letras iniciales son",nombre[:3]
    print "Voy a multiplicar tu nombre ok??? ",nombre*2,apellido*3

password()
