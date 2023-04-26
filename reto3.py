"""Elaborar un algoritmo que permita ingresar 20 números y muestre 
    todos los números menores e iguales a 25."""  

numeros = []
n = 20

for i in range(0,n):
    print(f"ingrese número ",i+1)
    numero = input()
    if int(numero) <= 25:
        numeros.append(numero)

print("los números menores i iguales a 25 son", numeros)
