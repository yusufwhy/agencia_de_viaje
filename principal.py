#imports
import os
from pakages.gestion_reservas.add_reserva import reservar, cancelar_Reserva
from pakages.gestion_costumers.cliente import 
from pakages.gestion_destino.destino import 
from pakages.gestion_mostrar.mostrar import 
def clearP():
    os.system('cls')

def pausaP():
    print('enter para seguir')
    input()


def principal():

    print('\n\tBienvenido  a nuestra agencia de viajes:\n\t Por favor haga una seleccion del menu:')
    
    flagMen = True
    while flagMen:
        print(""" \n\t Menu:\n
                \t\t1-Añadir un nuevo destino
                \t\t2-Añadir un nuevo cliente
                \t\t3-Realizar una reserva
                \t\t4-Cancelar una reserva
                \t\t5-Mostrar todos los destinos
                \t\t6-Mostrar todos los clientes
                \t\t7-Mostrar todas las reservas
                \t\t8-Salir""")

        try:
            sel = int(input('Introduzca una seleccion del menu:'))
        except ValueError:
            clearP()
            print('\nPor favor haga la seleccion de forma numerica\n\t\t Tipo---> 1 (para seleccionar Añadir un nuevo destino) ')
        else:
            if 8 <= sel < 1: 
                match sel:
                    case 1:
                        clearP()
                        print('\n\t\tSelecciono Añadir un nuevo destino')
                        
                    case 2:
                        clearP()
                        print('\n\t\tSelecciono Añadir un nuevo cliente ')
                        
                    case 3:
                        clearP()
                        print('\n\t\tSelecciono Realizar una reserva ')
                        reservar(agencia)
                        
                    case 4:
                        clearP()
                        print('\n\t\tSelecciono Cancelar una reserva ')
                        cancelar_Reserva(agencia)
                    case 5:
                        clearP()
                        print('\n\t\tSelecciono  Mostrar todos los destinos ')
                        
                    case 6:
                        clearP()
                        print('\n\t\tSelecciono  Mostrar todos los clientes ')
                        
                    case 7:
                        clearP()
                        print('\n\t\tSelecciono  Mostrar todos los reservas ')
                        
                    case 8:
                        clearP()
                        print('\n\t\tSelecciono  Salir del Programa ')
                        flagMen = False
                    case _:
                        clearP()
                        print('\n\t\tAlgo salio muy mal saliendo del Programa...')
                        break
            else:
                clearP()
                print('\n\t\tLa seleccion debe estar en el menu es decir entre el 1 y el 8')