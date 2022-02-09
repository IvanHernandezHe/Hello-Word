'''Un ángulo se considera agudo si es menor de 90 grados, obtuso si es mayor de 90 grados y recto si es igual a 90 grados. 
Utilizando esta información, escribir un algoritmo que acepte un ángulo en grados y visualice el tipo de
ángulo correspondiente a los grados introducidos.'''

print("Programa para determinar el angulo de un triangulo.")

a = int(input("Ingresa el aungulo del triangulo este debe ser mayor a 0° y menor de 180°: "))

while (a<0 or a>180):       #validación de grados ingresados
    a = int(input("Ingresa el aungulo del triangulo este debe ser mayor a 0° y menor de 180°: "))
    
print()
if a==0:
    print('el angulo ingresado es llano')
elif a<90:
    print("El angulo ingresado es agudo.")
elif a==90:
    print("El angulo ingresado es recto.")
elif (a<180 and a>90):
    print("El angulo ingresado es obtuso.")
else:
    print("El angulo ingresado es llano.")

print("Fin del programa.")