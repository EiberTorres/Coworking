#IMPORTACIONES
from ast import Try
import datetime 
from datetime import time, timedelta


#AGREGAR AL CLIENTE
clientes={}
def agregar_cliente():
    print("***********AÑADIR CLIENTE***********")
    print('/'*30)
    global clientes
    while True:
        nombre_cliente=input("Ingresa el nombre del cliente (deja en blanco para terminar):\n")
        if nombre_cliente=="":
            break
        else:
            descripcion=input("Ingrese la empresa a la que pertenece \n")
            if clientes.keys():
                nueva_llave=(max(list(clientes.keys()))+1)
            else:
                nueva_llave=1
            clientes[nueva_llave]=(nombre_cliente,descripcion)
    for id_cliente,datos_cliente in list(clientes.items()):
        print(f"ID CLIENTE: {id_cliente}\t NOMBRE CLIENTE: {datos_cliente[0]:^10} EMPRESA:\t{datos_cliente[1]:^10}")

#AGREGAR SALA
salas={}
def Agregar_salas():
    print("REGISTRO DE UNA NUEVA SALA")
    print('*'*30)
    global salas,datos_sala
    while True:
        nombre_sala=input("Ingresa el nombre de la sala(Deja en blanco para finalizar)\n")
        if nombre_sala=="":
            break
        else:
            cupo_sala=input("Ingresa el cupo de la sala: \n")
            if salas.keys():
                nueva_llave=(max(list(salas.keys()))+1)
            else:
                nueva_llave=1
            salas[nueva_llave]=(nombre_sala,cupo_sala)
    for id_sala,datos_sala in list(salas.items()):
        print(f"ID SALA: {id_sala}\t NOMBRE: {datos_sala[0]:^10}\t CUPO SALA: {datos_sala[1]:^10}")

#REGISTRAR RESERVACION
Reservaciones={}
def Reservar_sala():
    print("RESERVACION DE UNA SALA")
    print('*'*30)
    global Reservaciones,fecha_procesada
    ingresa_id_cliente=int(input("Ingresa el id de cliente \n"))
    if ingresa_id_cliente in clientes:
        registrar_sala=int(input("Ingresa el id de la sala \n"))
        if registrar_sala in salas:
            reservacion_evento=input("Ingrese el nombre del evento \n")
            if reservacion_evento=="":
                print("Error \n")
            else:
                reservacion_turno=int(input("Ingresa el turno: "))
                if reservacion_turno>3 or reservacion_turno==0:
                    print("Error en la reservacion del turno")
                else:
                    fecha_evento=input("Ingresa la fecha del evento: \n")
                    fecha_procesada= datetime.datetime.strptime(fecha_evento, "%d/%m/%Y").date()
                    fecha_actual = datetime.date.today()
                    fecha_permitida= fecha_actual+timedelta(days=2)
                    if (fecha_procesada<fecha_permitida):
                        print("Fecha no disponible \n")
                    else:
                        if Reservaciones.keys():
                            nueva_llave=(max(list(Reservaciones.keys()))+1)
                        else:
                            nueva_llave=1
                        Reservaciones[nueva_llave]=(fecha_procesada,reservacion_evento,registrar_sala,reservacion_turno)
                    for id_reservacion,datos_reservacion in list(Reservaciones.items()):
                        print(f"Folio: {id_reservacion}\t  Fecha: {datos_reservacion[0]}\t Evento:{datos_reservacion[1]}\t Sala:{datos_reservacion[2]}\t Turno: {datos_reservacion[3]}\t ")
#CONSULTAR LAS RESERVACIONES DE UNA SALA EXISTENTE
def consultas():
    for id_reservacion,datos_reservacion in list(Reservaciones.items()):
        print(f"Folio: {id_reservacion}\t  Fecha: {datos_reservacion[0]}\t Evento:{datos_reservacion[1]}\t Sala:{datos_reservacion[2]}\t Turno: {datos_reservacion[3]}\t ")


#CAMBIAR NOMBRE DEL EVENTO
def cambiar_nombre():
    while True:
        clave_buscar = int(input("Ingrese la clave del evento: \n"))
        if clave_buscar in Reservaciones:
            for clave,datos in list(Reservaciones.items()):
                actualizar=input("Ingresa el nuevo nombre del evento: \n")
                if clave_buscar==clave:
                    datos[1]=actualizar
        else:
            print("no existe la reservacion")


while True:
    print("******* MENÚ PRINCIPAL *******")
    print("\t[a] Registrar la reservación de una sala")
    print("\t[b] Editar el nombre de una reservación ya hecha")
    print("\t[c] Consultar las reservaciones existentes de una fecha específica")
    print("\t[d] Registro nuevo cliente")
    print("\t[e] Registro de una nueva sala")
    print("\t[f] Salir")
    try:
        opcion=input("\n¿Qué desea hacer? ")

        if opcion=="a":
            Reservar_sala()

        if opcion=="b":
            cambiar_nombre()
        if opcion=="c":
            consultas()
        if opcion=="d":
            agregar_cliente()
    
        if opcion=="e":
            Agregar_salas()

        if opcion=="f":
            print("Saliendo del programa...")
            break
    except:
        print("Ingresa una opción valída")