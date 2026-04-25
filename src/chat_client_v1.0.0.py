# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:13:37 2026

@author: bakaa
"""

import socket

# Configuración del servidor
host = '192.168.100.18'  # Dirección IP o nombre de host
port = 8080         # Puerto del servidor

# 1. Crear el socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Conectar al servidor
client.connect((host, port))

# 3. Enviar datos
mensaje = "que tal "
client.send(mensaje.encode())

# 4. Recibir respuesta
respuesta = client.recv(1024)
print("Respuesta:", respuesta.decode())

# 5. Cerrar conexión
client.close()
