from modulos.mostrar_destino import mostrar_destinos as md

def anadir_destino(destinos):
    ''' 
        Función que permite añadir un destino a la lista "destinos".

        Entradas:
            - Código del destino
            - Nombre del destino
            - Precio del destino

        Salidas:
            - Lista de destinos actualizada
    '''

    if destinos:
        print(f'Tenemos destinos en nuestra base de datos.\n')
        md(destinos)
    else:
        print('No hay destinos en nuestra base de datos')

    print(f'A continuación vas a introducir un nuevo destino a nuestra base de datos.\n Necesitarás:\n \t-Código de destino\n \t-Nombre del destino\n \t-Precio del destino (€)')
    
    while True:
        codigo = input('Introduce el código asociado al destino').lower()

        if not codigo:
            print(f'\nNo has introducido un código de destino')
        else:
            break
            
    while True:
        destino = input('Introduce el destino').lower()
        
        if not destino:
            print(f'\nNo has introducido un destino.')
        else:
            break

    while True:
        try:
            precio= float(input(f'Introduce (en €) el precio de ir al destino {destino.title()}: '))
            break
        
        except ValueError:
            print('Has de introducir el precio (en €) como un número.')

    destinos.append({'codigo destino': codigo, 'nombre destino': destino, 'precio destino': precio})
    
    # Falta evitar repeticiones de destinos ya hechos.

    return destinos