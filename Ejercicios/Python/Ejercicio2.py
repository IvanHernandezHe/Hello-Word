#Realizar el algoritmo para obtener la suma de los números pares hasta 1000 inclusive.

print("Programa que imprime la suma de numeros pares de 0 hasta el 1000\n")

i=0 #iterador
p=0 #variable para contabilizar pares
s=0 #variable para acumular suma de pares

while i < 1000/2:
    p=p+2 # variable par es igual a variable par + 2 
    s+=p  # variable que almacena la suma de los pares
    i+=1  # iterador en incremento de 1

print("La suma de los numeros pares de 0 hasta 1000 es: ",s)
print("Fin del programa.")