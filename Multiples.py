def multiplier():
    number=input("Insert a number ")
    print"the multiples of ", number, "are "
    for cont in range(11):
        print cont, "*", number,"= ", cont*number

    input("press enter to exit")

multiplier()
