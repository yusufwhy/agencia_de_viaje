def mostrar_clientes(clientes):
    ''' 
        Función que muestra todos los clientes (Se muestra ID cliente y nombre cliente).
    ''' 
    if clientes:
        print('Lista de clientes en nuestra base de datos:')
        for cliente in clientes:
            print(f"ID cliente: {cliente['id cliente']} | Nombre cliente: {cliente['nombre cliente'].title()}\n")
    
    else:
        print('No hay clientes en nuestra base de datos.')