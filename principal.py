#principal
"""PythonAC1 - Projecte Agència de Viatges
Vamos a crear un programa para una agencia de viajes que permita gestionar destinos, clientes y reservas. Este programa tendrá como mínimo las siguientes funcionalidades:
Añadir un nuevo destino (Código destino, Nombre destino y Precio destino).
Añadir un nuevo cliente (ID cliente y Nombre cliente.
Realizar una reserva (Pasaremos un código de destino y un ID de cliente).
Cancelar una reserva (Pasaremos un código de destino y un ID de cliente).
Mostrar todos los destinos (Mostraremos código, nombre y precio).
Mostrar todos los clientes (Mostraremos ID y nombre).
Mostrar todas las reservas (Mostraremos Cliente y Reserva).
Nuestro programa tiene que cumplir:
Los parámetros entre paréntesis son orientativos y pueden ayudar a la funcionalidad del programa, podemos decidir otros.
Las entradas y salidas de datos tienen que ser amigables con el usuario. O sea, darle un formato adecuado.
Debemos controlar que las entradas de datos cumplan ciertos parámetros y crear las excepciones necesarias.
Como mínimo deberíamos de tener dos módulos.
Todas las funciones tienen que tener su correspondiente documentación (docstring), con su funcionamiento, parámetros de entrada y parámetros de salida.
Uso de Git y GitHub para el control de versiones. Debéis añadirme como colaborador al repositorio de GitHub, donde también se realizará la entrega.
Formato de entrega: Enlace al repositorio de GitHub (1 por grupo).
Componentes de los grupos:
Grupo 1: Domingo, Hongyin y Enrique.
Grupo 2: Daniel, Alex y Jesús.
Grupo 3: Francisco, Volodymyr y María.
Grupo 4: Carlos, Albert y Caleb.
Fecha de entrega: 13 jun"""

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
            print('Por favor haga la seleccion de forma numerica\n Tipo---> 1 (para seleccionar Añadir un nuevo destino) ')
        else:
            if 8 <= sel < 1: 
                match sel:
                    case 1:
                        print('Selecciono Añadir un nuevo destino')
                        nDestino()
                    case 2:
                        print('Selecciono Añadir un nuevo cliente ')
                        nCliente()
                    case 3:
                        print('Selecciono Realizar una reserva ')
                        nReservas()
                    case 4:
                        print('Selecciono Cancelar una reserva ')
                        cReservas()
                    case 5:
                        print('Selecciono  Mostrar todos los destinos ')
                        mDestinos()
                    case 6:
                        print('Selecciono  Mostrar todos los clientes ')
                        mClientes()
                    case 7:
                        print('Selecciono  Mostrar todos los reservas ')
                        mReservas()
                    case 8:
                        print('Selecciono  Salir del Programa ')
                        flagMen = False
                    case _:
                        print('Algo salio muy mal saliendo del Programa...')
                        break
            else:
                print('La seleccion debe estar en el menu es decir entre el 1 y el 8')
