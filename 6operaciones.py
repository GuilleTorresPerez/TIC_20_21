def operaciones():
    primerNumero=input("Inserte el primer n�mero")
    segundoNumero=input("Inserte el segundo n�mero")
    print"Para sumar -> S"
    print"Para restar ->R"
    print"Para multiplicar ->M"
    print"Para dividir ->D"

    operacion=raw_input("Inserte la operacion")
    if operacion=="S":
        resultado=primerNumero+segundoNumero
    elif operacion=="R":
        resultado=primerNumero-segundoNumero
    elif operacion=="M":
        resultado=primerNumero*segundoNumero
    elif operacion=="D":
        resultado=primerNumero/segundoNumero

    print resultado

operaciones()
