# La función se diseña para añadir clientes
listaCliente = []
idCliente = 0
while True:
    nombreCliente = input('Introduzca el nombre del cliente aquí')
    if not nombreCliente.isdigit():
        idCliente += 1
    break
else:
    print('El nombre del cliente no puede ser formato de números')

# listaCliente.append()
# print(f'El nombre de cliente no puede ser de formato de número.')


    
