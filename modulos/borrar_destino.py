from modulos.mostrar_destino import mostrar_destinos as md

def borrar_destino(destinos):
    ''' 
        Función que permite borrar un destino a la lista "destinos".

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
        
        print(f'A continuación vas a borrar un destino de nuestra base de datos.\n Necesitarás:\n \t-Código de destino\n \t-Nombre del destino\n \t-Precio del destino (€)')
        
        while True:
            codigo = input('Introduce el código asociado al destino\n').lower()

            if not codigo:
                print(f'No has introducido un código de destino\n')
            else:
                break
                
        while True:
            destino = input('Introduce el destino\n').lower()
            
            if not destino:
                print(f'No has introducido un destino.\n')
            else:
                break

        while True:
            try:
                precio= float(input(f'Introduce (en €) el precio de ir al destino {destino.title()}: '))
                break
            
            except ValueError:
                print('Has de introducir el precio (en €) como un número.\n')

        for destino in destinos:
            if codigo == destino['codigo destino'] and destino == destino['nombre destino'] and precio == destino['precio destino']:
                destinos.remove(destino)
 
    else:
        print('No hay destinos en nuestra base de datos\n')


    return destinos