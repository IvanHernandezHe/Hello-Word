#Dados tres numeros, decir cual es el intermedio.

print("Programa para conocer el numero más intermedio de los ingresados")

A=int(input("Ingresa el primer numero: "))
B=int(input("Ingresa el primer numero: "))
C=int(input("Ingresa el primer numero: "))
print("")

if A==B and A==C:
    print("Los tres números ingresados son iguales.",A,B,C)
    print("El valor intermedio es: ",A)
else:
    if A==B:
        print("El primer y segundo numeros ingresados son iguales.")
        print("El numero intermedio es:",A)
    else:
        if A==C:
            print("El primer y tercer numeros ingresados son iguales")		
            print("El numero intermedio es: ",A)
        else:   
            if B==C:
                print("El segundo y tercer numeros ingresados son iguales")
                print("El numero intermedio es: ",B)
            else:
                if A>B and A>C:
                    if B>C:
                        print("El segundo numero ingresado es el intermedio")
                        print("\nEl numero intermedio es: ",B)	
                    else:
                        print("El tercer numero ingresado es el intermedio")
                        print("El numero intermedio es: ",C)
                else:
                    if B>A and B>C:
                        if A>C:
                            print("El primer numero ingresado es el intermedio")
                            print("El numero intermedio es: ",A)
                        else:
                            print("El tercer numero ingresado es el intermedio")
                            print("El numero intermedio es: ",C)
                    else:
                        if A>B:
                            print("El primer numero ingresado es el intermedio")
                            print("El numero intermedio es: ",A)
                        else:
                            print("El segundo numero ingresado es el intermedio")
                            print("El numero intermedio es: ",B)
print("Fin del programa.")
								

								


							

								



							


			    







