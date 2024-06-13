def cancelar_reserva(clientes, destinos):
    ''' 
        Función que permite cancelar una reserva a la lista "clientes".

        Entradas:
            - Código de destino
            - ID de cliente
      
        Salidas:
            - Lista de clientes actualizada
    '''
    while True:
        if clientes and destinos:
        
            print(f'A continuación vas a cancelar una nueva reserva. \n Necesitarás:\n \t-Código de destino\n \t-ID de cliente')
            
            for cliente in clientes:
                if cliente['reserva'] == True:

                    for cliente in clientes:
                        print(f"Código destino: {cliente['codigo destino']} | Destino: {cliente['nombre destino'].title()} | ID cliente: {cliente['id cliente']} | Cliente: {cliente['nombre cliente'].title()}")

                    codigo_destino = input('Introduce el código del destino donde vas cancelar la reserva').lower()
                    id_cliente = input('Introduce el ID del cliente para cancelar su reserva').lower()

                    for cliente in clientes:
                        if codigo_destino == cliente['codigo destino'] and id_cliente == cliente['id cliente']:
                            cliente['reserva'] = False
                            cliente['codigo destino'] = ''
                            cliente['id cliente'] = ''
                    
                        for destino in destinos:
                            if codigo_destino == destino['codigo destino']:
                                cliente['nombre destino'] = ''
                                cliente['precio destino'] = ''
                    
                    print('Reserva anulada')

                else:
                    print('No tenemos reservas en nuestra base de datos')
        else:
            print('No se puede cancelar una reserva porque no hay destinos o clientes')
                
        print(f'La reserva del cliente con ID {id_cliente} en el destino con código {codigo_destino} se ha cancelado con éxito.')
        epilogue = input('Para seguir cancelando reservas presiona enter. Si no, puedes presionar * para volverte al menu principal. \n')
        if epilogue == '*':
            break
        else:
            continue

    return clientes 