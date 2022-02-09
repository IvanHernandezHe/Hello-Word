'''Escribir un programa que acepte dos números reales de un usuario y un código de selección.
Si el código es 1, entonces el programa suma los números introducidos y se visualiza el resultado; 
si el código de selección es 2 los números deben ser multiplicados; si el códigos eleccionado es 3, 
el primernumero debe dividirse por el segundo (con lógicaespecial para divisiónsobre 0) y visualizarse el resultado.'''

print('Programa que al ingresar dos números, se da la opción de: sumar,multiplicar o divir.\n')

A = int(input('Ingresa un número: '))
B = int(input('Ingresa un segundo número: '))
print()

print('Ingresa que operación deseas realizar con los números ingresados.\n')
print('Opción 1. SUMA')
print('Opción 2. MULTIPLICACIÓN')
print('Opción 3. DIVISIÓN\n')

r = int(input("\nIngresa la opción a seleccionar: "))


while (r<1 or r>3):         #Validación de caracter valido

    print("\nIngresa un caracter valido para continuar el programa, los valores permitidos son: '1 , 2 o 3'")
    r = int(input('Ingresa la opción a seleccionar: \n'))

if r ==1:
    print('Has seleccionado la opción 1. (suma)\n')
    print(A,"+",B,"=",A+B)

elif r==2:
    print('Has seleccionado la opción 2. (Mutiplicación)\n')
    print(A,'*',B,'=',A*B)

elif r==3:
    print('Has seleccionado la opción 3. (División)\n')

    if B==0:
        print("El numero 0 no puede ser divido entre otro numero\n")

    else:
        print(A,"/",B,"=",A/B)     

print("\nFin del programa.")