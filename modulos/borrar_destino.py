from modulos.mostrar_destino import mostrar_destinos as md

def borrar_destino(destinos):
    ''' 
        Función que permite borrar un destino a la lista "destinos".

        Entradas:
            - Código del destino
            - Nombre del destino


        Salidas:
            - Lista de destinos actualizada
    '''

    if destinos:
        print(f'Tenemos destinos en nuestra base de datos.\n')
        md(destinos)
        
        print(f'A continuación vas a borrar un destino de nuestra base de datos.\n Necesitarás:\n \t-Código de destino\n \t-Nombre del destino\n')
        
        while True:
            codigo = input('Introduce el código asociado al destino').lower()

            if not codigo:
                print(f'\nNo has introducido un código de destino')
            else:
                break
                
        while True:
            destinoPedido = input('Introduce el destino').lower()
            
            if not destinoPedido:
                print(f'\nNo has introducido un destino.')
            else:
                break

        for destino in destinos:
            if codigo == destino['codigo destino'] and destinoPedido == destino['nombre destino']:
                destinos.remove(destino)
 
    else:
        print('No hay destinos en nuestra base de datos')


    return destinos