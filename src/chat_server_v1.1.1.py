# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:12:31 2026

@author: Maria del Carmen

Notas de Versión
- V1.1.0    
* Se implento un metodo para enviar mensajes al cliente
* Se implmento una busqueda de dirección IP automatica
- V1.1.1    
* Se implemnto un metodo para cerrar servidor a traves de un comando
* Se agrego un timer para tiempo de conexión
* Se agrego una comprobación para la terminación de conexión del cliente
* Se agrego soc.close() a Cerrar_Servidor() para dejar el socket libre
"""

import socket
import time

def Cerrar_Servidor():                         #Función para cerrar servidor y dar duración
    print("Cerrando conexión")                 #de la conexión
    end=time.time()
    print("Tiempo de Conexión: ",end-start)
    connection.close()
    sock.close()

#0 Conseguir dirección IP
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Nombre de PC:", hostname)
print("Dirección IP:", IPAddr)

#1 Crear el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2 Vincular el socket al puerto
server_address = (str(IPAddr), 8080)
print(f'Iniciando servidor en {server_address[0]} puerto {server_address[1]}')
sock.bind(server_address)

#3 Escuchar conexiones entrantes
sock.listen(1)
start=time.time()

while True:
    # Esperar conexión
    print('Esperando conexión...')
    connection, client_address = sock.accept()
    try:
        print(f'Conexión desde {client_address}')
        # Recibir datos
        while True:
            data = connection.recv(1024)
            print(f'Cliente: {data.decode()}')
            if data.decode()=='Cerrar Cliente':             #Si el cliente termina la conexion terminar instancia 
                print("El cliente ha cerrado la conexión")
                break 
            if data:                                        #Si se recibe mensaje, enviar respuesta
                mensaje=input(str('Servidor: '))
                connection.sendall(mensaje.encode())
                if mensaje=='Cerrar Servidor':
                    break
            else:
                break
    finally:
        # Cerrar conexión
        Cerrar_Servidor()
        break
