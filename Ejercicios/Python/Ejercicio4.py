#El sistema de calificación americano se suele calcular de acuerdo con el siguiente cuadro:
#Utilizando esta información escribir un algoritmo que acepte una calificación numérica del
#estudiante(0-100), convierta esta calificacióna su equivalente en letra y visualicela calificación correspondiente en letra.

#Mayor o igual a 90                         A
#Menor a 90 pero mayor o igual a 80         B
#Menor de 80 pero mayor o igual a 70        C
#Menor de 70 pero mayor o igual a 69        D
# Menor de 69                               F

print("Programa para convertir la notación decimal de calificaciones de numero a letra.\n")

C = str(input('Ingresa el puntaje de la calificación obtenida, para cambiarla al sistema americano de calificaciones: '))

validacion = str.isdigit(C) 

while (validacion != True) or (C<0 or C>100) :     
    C = str(input('Ingresa el puntaje de la calificación obtenida, debe ingresar un numero del 0 al 100: '))
    validacion = str.isdigit(C) 
    
print(validacion)
print("\nFin del programa.")
