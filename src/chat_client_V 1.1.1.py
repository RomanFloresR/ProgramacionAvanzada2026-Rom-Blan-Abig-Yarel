# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:13:37 2026

@author: bakaa

notas de version:
    1.1.0
    se permite enviar multiples mensajes 
    1.1.1
    Notifica cuando el servidor cierra
    Se notifica al servidor cuando el cliente cierra
"""

import socket

# Configuración del servidor
host = '192.168.137.1'  # Dirección IP o nombre de host
port = 8080             # Puerto del servidor

# 1. Crear el socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Conectar al servidor
client.connect((host, port))

# 3. Enviar datos
while True:
    mensaje = input(str(": "))
    client.send(mensaje.encode())

# 4. Recibir respuesta
    respuesta = client.recv(1024)
    print("Servidor:", respuesta.decode())
    a=respuesta.decode()

# 5. Cerrar Conexion
    if mensaje=='Cerrar Cliente':
        client.send(mensaje.encode())
        print("conexion terminada")
        client.close()
        break
    
#. 6. servidor cerrado 
    if a=="Cerrar Servidor":
        print("El servidor cerro")
        client.close()
        break
