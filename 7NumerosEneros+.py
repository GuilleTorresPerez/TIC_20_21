'''S Suma
R Resta
M Multiplica
D Divide'''
def menu():
    print"Introduce dos n�meros enteros"
    numero1=input("numero 1= ")
    interruptora=1
    while(interruptora==1):
        numero2=input("numero 2= ")
        print"***************************************"
        print"*                 MENU                *"
        print"***************************************"
        print"1.Suma"
        print"2.Resta"
        print"3.Multiplicacion"
        print"4.Division"
        opcion=input("Teclee la opcion deseada: ")
        if(opcion==1):
            resultado=numero1+numero2
            interruptora=0
        if(opcion==2):
            resultado=numero1-numero2
            interruptora=0
        if(opcion==3):
            resultado=numero1*numero2
            interruptora=0
        if(opcion==4):
            if(numero2!=0):
                resultado=numero1/numero2
                interruptora=0
            else:
                interruptora=1
                print"Has intentado dividir entre 0"
                print"Introduce un nuevo numero"

    print"El resultado es ",resultado

menu()
