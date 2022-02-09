tex = input("Ingresa el texto que deseas imprimir: ")
n = int(input("Ingresa las veces que deseas imprimir el texto: "))

i=0

''' metodo while

while i<n:
    print(i+1," .",tex)
    i=i+1
print("El programa ha finalizado")
'''

for _ in range(n):
    print(i+1," .",tex)
    i=i+1
print("El programa ha finalizado")

