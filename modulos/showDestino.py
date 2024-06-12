def showDestino(listaDestino):
# add ese código al inicio del principal: listaDestino = []
    for j, destinos in enumerate(listaDestino):
        print(f'\nDestino {j + 1}')
        for key, value in destinos.items():
            print(f'{key} \t {value}')