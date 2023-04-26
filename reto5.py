"""Hacer un programa que registre el consumo realizado por los clientes de un restaurante, 
si el consumo de cada cliente excede 50.000 se hará un descuento del 20%.
Se debe mostrar el pago de cada cliente y el total de todos los pagos.""" 

pagoCliente = 0
pagosCliente = []
totalPagos = 0
r = "S"

while r == "S":
    pagoCliente=int(input("Ingrese el total del consumo del cliente:"))
    if pagoCliente > 50000:
        pagosCliente.append(pagoCliente*0.8)
    else:
        pagosCliente.append(pagoCliente)
    r = input("¿Nuevo cliente por registrar? ")

totalPagos = sum(pagosCliente)
print("El pago de cada cliente fue:", pagosCliente)
print(f"El total de todos los pagos es de {totalPagos} pesos")

