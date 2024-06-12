from modulos.mostrar_clientes import mostrar_clientes as mc

def borrar_cliente(clientes):
    ''' 
        Función que permite borrar un cliente de la lista "clientes".

        Entradas:
            - ID del cliente
            - Nombre del cliente
        
        Salidas:
            - Lista de clientes actualizada
    '''
    if clientes:
        print(f'Tenemos clientes en nuestra base de datos\n')
        mc(clientes)
        
        print(f'A continuación vas a introducir borrar un cliente de nuestra base de datos.\n Necesitarás:\n \t-ID del cliente\n \t-Nombre del cliente')
        
        while True:
            id_cliente = input('Introduce el ID asociado al cliente').lower()

            if not id_cliente:
                print(f'\nNo has introducido un ID de cliente')
            else:
                break
        while True:
            nombre_cliente = input('Introduce el nombre del cliente').lower()

            if not nombre_cliente:
                print(f'\nNo has introducido un nombre de cliente')
            else:
                break

        for cliente in clientes:
                if nombre_cliente == cliente['nombre cliente'] and id_cliente == cliente['id cliente']:
                        clientes.remove(cliente)

    else:
        print(f'No hay clientes en nuestra base de datos\n')


    return clientes