Ncad = int(input("Cuantas cadenas binarias de 8 digitos deseas convertir a caracter: "))

for j in range(Ncad):

    cadena = str(input(f"Ingresa la cadena numero {j+1} de caracteres de codigo Binario: "))

    while len(cadena)<8 or len(cadena)>8:
        cadena = str(input("Ingresa la cadena de caracteres de codigo Binario (DEBE SER DE 8 DIGITOS): "))

    caracter=[len(cadena)]
    
    #list(int(cadena))

    acumulador=0

    conver=list(map(int,cadena))

    for i in range(len(cadena)):

        #print (f"Letra: {i}")
        #\t Codigo ascci: ",ord(i)
        #Nascci=ord(i)
        #print('este es el iterador: ',i)
        #print('este es el numero a convertir a decimal',conver[i])
        #print('Este es el acumulador')

        n=conver[i]

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

        #caracter[i]=caracter.appendchr(acumulador)
        
    #print(chr(acumulador))
    #print(acumulador)
    #print(list(conver))
    
    #caracter.append(chr(acumulador))

    #caracter[i] = chr(acumulador)

    #print(chr(acumulador))

print('Este es el resultado de los caracteres ingresados')    

'''i=0
for i in range(Ncad):
     
    print(caracter[i])'''

print(list(caracter))
print("fin") 