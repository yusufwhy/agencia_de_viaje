from modulos.mostrar_clientes import mostrar_clientes as mc

def anadir_cliente(clientes):
    ''' 
        Función que permite añadir un nuevo cliente a la lista "clientes".

        Entradas:
            - ID del cliente
            - Nombre del cliente
        
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
 
     # Falta evitar repeticiones de clientes ya hechos.
    return clientes