def mostrar_destinos(destinos):
    ''' 
        Función que muestra todos los destinos (Se muestra código, nombre y precio).
    '''
    if destinos:
        print('Lista de destinos en nuestra base de datos:\n')
        for destino in destinos:
            print(f"Código destino: {destino['codigo destino']} | Nombre del destino: {destino['nombre destino'].title()} | Precio de destino: {destino['precio destino']}€\n ")
    else:
        print('No hay destinos en nuestra base de datos.\n')