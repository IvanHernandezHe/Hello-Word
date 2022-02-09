
from Divisores_de_un_numero import Residuo


N = 0
i = 0
residuo = 0
divisores = 0
l=1

Numero = int(input("Ingresa numero para conocer divisores"))

N = Numero
i = (N*-1)

if N==0:
    print("Numero 0 no tiene divisores")
elif N==1:
    print("Estos son los divisores del numero ingresado, estan ordenados de menor a mayor.")	
    print("Se incluyen valores negativos y positivos.")
    print("------------------------------")
    print("-1")
    print("-----------------------------")
    print("1")
elif N==-1:
    print("Estos son los divisores del numero ingresado, estan ordenados de menor a mayor.")	
    print("Se incluyen valores negativos y positivos.")
    print("------------------------------")
    print("-1")
    print("-----------------------------")
    print("1")
else:
    print("Estos son los divisores del numero ingresado, estan ordenados de menor a mayor.")
    print("Se incluyen valores negativos y positivos.")
    print("------------------------------")
    
    #########

if(i<N):
    l=l
else:
    N = (N*-1)
    i = (i*-1)

if(i==0):
    l=l
    if i>N:
        i = i-1
    else:
        i = i+1

residuo = N%i

if residuo==0:
    print(i)
    divisores=divisores+1

if i<N:
    i=i+1
else:
    i=i-1


while(i!=N):

    if(i<N):
        l=l
    else:
        N = (N*-1)
        i = (i*-1)

    if(i==0):
        l=l

        if i>N:
            i = i-1
        else:
            i = i+1

    residuo = N%i

    if residuo==0:
        print(i)
        divisores=divisores+1

    if i<N:
        i=i+1
    else:
        i=i-1
print(i)

print("El numero ingresado tiene: ",divisores-1,"divisores")

print("Programa finalizado.")
