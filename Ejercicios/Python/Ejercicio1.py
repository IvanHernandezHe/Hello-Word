print("Programa para conocer el numero más grande ingresado.\nConsiderando que los numeros ingresados son diferentes.")

A=int(input("Ingresa el primer numero: "))
B=int(input("Ingresa el primer numero: "))
C=int(input("Ingresa el primer numero: "))

if A>B and A>C:
    print("\nEl numero mayor es A: ",A)
elif B>C and B>A:
    print("\nEl numero mayor es B: ",B)
else:
    print("\nEl numero mayor es C: ",C)
print("Fin del programa.")