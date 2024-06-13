from modulos.mostrar_clientes import mostrar_clientes as mc

def anadir_cliente(clientes):
    ''' 
        Función que permite añadir un nuevo cliente a la lista "clientes".

        Entradas:
            - Nombre del cliente
                    
        Operaciones:
            - Primero: Verifica mediante un IF si hay clientes o no y printa el mensaje correspondiente.
                - El ID del cliente se genera automaticamente.
            - Segundo: Avisa al usuario sobre qué datos va a necesitar.
            - Tercero: Pide los datos y verifica que no se añadan datos vacios mediante el uso de bucles while y decisiones if not.

        Salidas:
            - Lista de clientes actualizada
    '''
    if clientes:
        print(f'Tenemos clientes en nuestra base de datos\n')
        mc(clientes)
    else:
        print(f'No hay clientes en nuestra base de datos\n')

    print(f'A continuación vas a introducir un nuevo cliente a nuestra base de datos.\n Necesitarás:\n \t-ID del cliente\n \t-Nombre del cliente')
    
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
   
    clientes.append({'codigo destino': '', 'nombre destino': '', 'precio destino': '', 'reserva': False, 'codigo destino': '', 'id cliente': id_cliente, 'nombre cliente': nombre_cliente })
    
    print(f'Nuevo cliente {nombre_cliente} con ID {id_cliente} añadido con éxito')

    return clientes