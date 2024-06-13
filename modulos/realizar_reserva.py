def realizar_reserva(clientes, destinos):
    ''' 
        Función que permite realizar una reserva a la lista "clientes".

        Entradas:
            - Código de destino
            - ID de cliente
      
        Salidas:
            - Lista de clientes actualizada
    '''
       if clientes and destinos:

        print(f'A continuación vas a realizar una reserva. \n Necesitarás:\n \t-Código de destino\n \t-ID de cliente')
        
        print(f'Lista de destinos:\n')
        for destino in destinos:
            print(f"Código destino: {destino['codigo destino'].title()} | Destino: {destino['nombre destino'].title()} \n")

        print(f'Lista de Clientes:\n')
        for cliente in clientes:
            print(f" ID cliente: {cliente['id cliente'].title()} | Cliente: {cliente['nombre cliente'].title()}\n")

        codigo_destino = input('Introduce el código del destino para hacer la reserva').lower()
        id_cliente = input('Introduce el ID del cliente del que quieres hacer la reserva').lower()
        
        lista_clientes = []

        for cliente in clientes:
                if id_cliente == cliente['id cliente']:
                    lista_clientes.append(cliente)
                else:
                    pass
        if lista_clientes:
             pass
        else:
             print('No nos consta este ID de cliente en nuestra base de datos\n')
             
        lista_destinos = []
        
        for destino in destinos:
                if codigo_destino == destino['codigo destino']:
                    lista_destinos.append(destino)
                else:
                    pass
        if lista_destinos:
             pass
        else:
             print('No nos consta este codigo de destino en nuestra base de datos\n')

        if lista_clientes and lista_destinos:
            cliente['reserva'] = True
            cliente['codigo destino'] = codigo_destino
            cliente['id cliente'] = id_cliente
            cliente['nombre destino']= destino['nombre destino']
            cliente['precio destino']= destino['precio destino']
        
        else:
            print('No has introducido un ID de cliente o un código de destino válidos\n')

    else:
        print('No se puede realizar una reserva porque no hay destinos o clientes\n')
        
    return clientes  
