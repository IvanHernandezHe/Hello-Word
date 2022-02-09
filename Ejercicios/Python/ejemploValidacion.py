car = int(input("Elige 1 o 2 para validar un caracter:\n\n"))

while (car<1 or car>2):
    if car==1:
        print("has seleccionado la opicion 1")
        
    elif car==2:
        print("Has seleccionado la opion 2")
        
    else:
        car = int(input("Ingresa un caracter valido, 1 o 2: "))
print("fin del juego")
