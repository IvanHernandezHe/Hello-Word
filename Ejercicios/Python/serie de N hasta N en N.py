#Serie de N numero en N numero hasta N numero imprimiendo en ciclo while

N = int(input("Ingresa desde el numero a comenzar la serie: "))
Sf = int(input("Ingresa el numero hasta donde terminara la serie: "))
incre = int(input("Ingresa el incremento de la serie: "))



while N<=Sf:
    print(N)
    N=N+incre
print("La serie ha terminado")

