#Porgama para convertir cadena de 8 numeros en forma binal a decimal
print("Progama para convertir cadena de 8 numeros en forma binal a decimal")

for j in range(9):

    print("Se convertiran las cadenas binarias 9 veces")
    print(f"Ingresa la cadena numero {j+1}")

    acumulador = 0
    i=0

    while i < 8:

        n = int(input(f'\nIngresa el {i+1} numero (de izquierda a derecha)'))

        while n<0 or n>1:
            if n<0 or n>1:
                n = int(input("Ingresa un valor binario, 0 o 1"))
            else:
                n=n

        if i == 0:
            n=n*128
        elif i == 1:
            n=n*64
        elif i == 2:
            n=n*32
        elif i == 3:
            n=n*16
        elif i == 4:
            n=n*8
        elif i == 5:
            n=n*4
        elif i == 6:
            n=n*2
        else:
            n=n*1

        acumulador = acumulador+n

        i=i+1

    print("\nEl numero decimal es: ",acumulador)
    print("El caracter ascci es: ",chr(acumulador))
    print(f"Fin de la cadena numero {j+1}")
    
print("Fin del programa")