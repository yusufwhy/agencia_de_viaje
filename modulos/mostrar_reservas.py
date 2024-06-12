def mostrar_reservas(clientes, destinos):
    ''' 
        Función que muestra todas las reservas (Se muestra Cliente y Reserva).
    ''' 
    contador = 0

    if clientes and destinos:
        print('Reservas:')

        for cliente in clientes:
            if cliente['reserva'] == True:
                print(f"ID cliente: {cliente['id cliente']} | Nombre cliente: {cliente['nombre cliente'].title()} | Código destino: {cliente['codigo destino']} | Nombre destino: {cliente['nombre destino'].title()}| Nombre destino: {cliente['precio destino']}\n")
                         
        
        else:
            contador +=1
            if contador == len(clientes):
                print('No hay reservas realizadas por nuestros clientes.')
            else:
                pass
    else:
        print('No se puede mostrar la lista de reservas porque no hay destinos o clientes en la base de datos')