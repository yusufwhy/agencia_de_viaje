''' Primer proyecto por grupos:


Vamos a crear un programa para una agencia de viajes que permita gestionar destinos, clientes y reservas. Este programa tendrá como mínimo las siguientes funcionalidades:
- Añadir un nuevo destino (Código destino, Nombre destino y Precio destino).
- Añadir un nuevo cliente (ID cliente y Nombre cliente).
- Realizar una reserva (Pasaremos un código de destino y un ID de cliente).
- Cancelar una reserva (Pasaremos un código de destino y un ID de cliente).
- Mostrar todos los destinos (Mostraremos código, nombre y precio).
- Mostrar todos los clientes (Mostraremos ID y nombre).
- Mostrar todas las reservas (Mostraremos Cliente y Reserva).

Nuestro programa tiene que cumplir:
- Los parámetros entre paréntesis son orientativos y pueden ayudar a la funcionalidad del programa, podemos decidir otros.
- Las entradas y salidas de datos tienen que ser amigables con el usuario. O sea, darle un formato adecuado.
- Debemos controlar que las entradas de datos cumplan ciertos parámetros y crear las excepciones necesarias.
- Como mínimo deberíamos de tener dos módulos.
- Todas las funciones tienen que tener su correspondiente documentación (docstring), con su funcionamiento, parámetros de entrada y parámetros de salida.
- Uso de Git y GitHub para el control de versiones. Debéis añadirme como colaborador al repositorio de GitHub, donde también se realizará la entrega.
- Formato de entrega: Enlace al repositorio de GitHub (1 por grupo).

Componentes de los grupos:
Grupo 1: Domingo, Hongyin y Enrique.
''' 


#Funciones

from modulos.screen import clear_screen, pause_screen

from modulos.anadir_destino import anadir_destino
from modulos.borrar_destino import borrar_destino
from modulos.anadir_cliente import anadir_cliente
from modulos.borrar_cliente import borrar_cliente
from modulos.realizar_reserva import realizar_reserva
from modulos.cancelar_reserva import cancelar_reserva
from modulos.mostrar_destino import mostrar_destinos
from modulos.mostrar_clientes import mostrar_clientes
from modulos.mostrar_reservas import mostrar_reservas


# Principal

def menu_principal(destinos, clientes):


    while True:
        clear_screen()

        print('¿Qué operación quieres realizar?')
        print(f' 1) Añadir un nuevo destino\n 2) Borrar un destino\n 3) Añadir un nuevo cliente\n 4) Borrar un cliente\n 5) Realizar una reserva\n 6) Cancelar una reserva\n 7) Mostrar todos los destinos\n 8) Mostrar todos los clientes\n 9) Mostrar todos las reservas\n 10) Salir del programa')
        opcion = input()

        match(opcion):
            case '1':
                anadir_destino(destinos)
                pause_screen()
            case '2':
                borrar_destino(destinos)
                pause_screen()
            case '3':
                anadir_cliente(clientes)
                pause_screen()
            case '4':
                borrar_cliente(clientes)
                pause_screen
            case '5':
                realizar_reserva(clientes, destinos)
                pause_screen()
            case '6':
                cancelar_reserva(clientes, destinos)
                pause_screen()
            case '7':
                mostrar_destinos(destinos)
                pause_screen()
            case '8':
                mostrar_clientes(clientes)
                pause_screen()
            case '9':
                mostrar_reservas(clientes, destinos)
                pause_screen()
            case '10':
                print('Has seleccionado salir. Adios.')
                break
            case _:
                print('Opción no contemplada')
                pause_screen()

if __name__ == '__main__':
    destinos = []
    clientes = []
    menu_principal(destinos, clientes)



