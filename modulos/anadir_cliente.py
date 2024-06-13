from modulos.mostrar_clientes import mostrar_clientes as mc

def anadir_cliente(clientes):
    ''' 
        Función que permite añadir un nuevo cliente a la lista "clientes".

        Entradas:
            - Nombre del cliente
        
        Salidas:
            - Lista de clientes actualizada
    '''
    index = len(clientes)
    while True:
        if clientes:
            print(f'Tenemos clientes en nuestra base de datos\n')
            mc(clientes)
        else:
            print(f'No hay clientes en la base de datos\n')
        print(f'A continuación vas a introducir un nuevo cliente a nuestra base de datos.\n Se recomendará introducir ambos el nombre y el apellido del cliente\n')
        
        while True:
            nombre_cliente = input('Introduce el nombre del cliente').lower()
            if not nombre_cliente:
                print(f'\nNo has introducido un nombre de cliente')
            elif not nombre_cliente.isdigit():
                index += 1
                id_cliente = str(index) + ''.join([word[0] for word in nombre_cliente.split()])
                break
            else:
                print('El nombre del cliente no puede ser de números sólo.')
        clientes.append({'codigo destino': '', 'nombre destino': '', 'precio destino': '', 'reserva': False, 'codigo destino': '', 'id cliente': id_cliente, 'nombre cliente': nombre_cliente })
        print(f'El nuevo cliente {nombre_cliente} con ID {id_cliente} se ha añadido con éxito.')
        
        epilogue = input('Para seguir introduciendo clientes presiona enter. Si no, puedes presionar * para volverte al menu principal. \n')
        if epilogue == '*':
            break
        else:
            continue

    return clientes