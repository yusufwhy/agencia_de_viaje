# Tres partes: 1. menú principal y reserva ; 2. cliente relacionado; 3. destino relacionado
# Parte Hongyin - funciones con destinos relacionado
# Añadir un nuevo destino (Código destino, Nombre destino y Precio destino)
# def addDestinatoin(listaDestino):
# add ese código al inicio del principal: listaDestino = []
listaDestino = []
for i in range(4):
        codigoDestino = input('Introduzca el código del destino nuevo, for favor.\n')
        nombreDestino = input('Introduzca el nombre de ese destino nuevo, por favor.\n')
        while True:
            try:
                precioDestino = float(input('Introduzca el precio para ese destino nuevo, por favor.\n'))
                break
            except ValueError:
                print('El precio no puede ser otro formato fuera de ser numeros.')
# from modulos.screen import pause_screen, clear_screen (Domingo´s modulos)
        nuevoDestino = {
            'codigo' : codigoDestino,
            'nombre' : nombreDestino,
            'precio' : precioDestino, 
            }
        print(f'El nuevo destino {nombreDestino} con código {codigoDestino} se ha añadido con éxito y su precio será €{precioDestino}.')
        listaDestino.append(nuevoDestino)
print(listaDestino)
#def showDestination(listaDestino):
for j, destinos in enumerate(listaDestino):
     print(f'n\ Destino {j + 1}')
     for key, value in destinos.items():
          print(f'\t {key} \t {value}')
     
     