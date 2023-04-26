"""Hacer un programa que sume 5 precios de camisas (en dólares)
y que luego muestre el total de la venta en pesos."""

camisaDolar = []
totalVentas = 0
valorDolar = 4496.32

for i in range(0,4):
    camisaDolar.append(int(input(f"Ingrese el valor de la camisa {i+1} en dolares:")))

totalVentas=valorDolar*sum(camisaDolar)

print("El valor total de las camisa es pesos es",totalVentas)
