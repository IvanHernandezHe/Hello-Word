#Divisores de un número

N = int(input("Ingresa un numero para conocer sus divisores."))
Residuo = 0.0

print("Estos son los divisores del numero ingresao ordenados de mayor a menor.")

if N == 0:
    print("---------------")
    print("El numero ingresado (0) no tiene divisores. bueno almenos eso se cree.")
else:
    print("---------------")    
    print("Se incluyen valores positivos y negativos.")
    print("---------------")

    i = N*-1

    while i==N:


        if i<=N:
            print(" ")
        else:
            N = N*-1
            i = i*-1

        if i==0:
            print("---------------")
            if i>N:
                i = i-1
            else:
                i = i+1
        else:
             print(" ")
        
        Residuo = N%i    

        if Residuo==0:
            print(i)

        if i==N:
            print("------")
            print("Programa finalizado.")
        else:
            if i<N:
                i=i+1
            else: 
                i=i-1
                
