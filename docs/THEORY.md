¿Qué es un socket? 
 Se trata del punto final de una conexión bidireccional
 que existe entre dos programas que se comunican por medio 
 de una red.
 Tienen una  extensa aplicación dentro de la vida cotidiana, 
 tal es el caso de la mensajería EN WhatssApp para que los mensajes 
 se envíen y reciban en tiempo real.

TCP VS UDP

 TCP-Transmission Control Protocol
 Se orienta a la conexión para ello se basa en el handshake que consta de 
 tres pasos:
 SYN (Sincronizar)
 El Cliente envía un paquete con la bandera SYN activada
 SYN-ACK ( Sincronizar- Acuse de la información) 
 El Servidor responde con un paquete SYN y ACK
 ACK (Acuse de la información)
 El Cliente envía el paquete final con la bandera ACK
 Este proceso añade latencia por lo que debes esperar a que estos 
 tres mensajes viajen de ida y vuelta antes de enviar el primer byte
 de información real.
 En los video juegos es útil el TCP para realizar el inicio de sesión y procesos de menú.
 
 UDP -User Datagram Protocol
 
 Este método no requiere conexión, envía datagramas directamente al 
 destino sin verrificación previa o de recepción.
 Su principal característica es la velocidad y la eficiencia
 En UDP se envían datos al instante, sin embargo es posible que durante 
 el envío se pierda el mensaje o dato.
 Es útil para videojuegos en línea que requieren sockets UDP para el movimiento de 
 personajes, disparo y uso de habilidades, donde se realizan acciones 
 en juegos como LOL y Fortnite

Puertos y direcciones IP
 La dirección IP permite la identificación del computador dentro de la red, es indispensable
 para conectar cliente-servidor.En programación de sockets hay dos términos clave:
 IP Local (0.0.0.0 o 127.0.0.1): Indica que el socket escucha en la propia máquina. 127.0.0.1 es el famoso localhost.
 IP Remota: La dirección del servidor o dispositivo al que te quieres conectar. 
 
 Los puertos se encargan de identificar servicios dentro de un dispositivo.

 Puertos Bien conocidos (Well-Known Ports)
 Tienen rangos de 0-1023
 Su uso es reservado para servicios universales y protocolos estándar del sistema
 Para su control requieren regularmente de permisos de administrador para ser usados 
 en aplicaciones
 Ejemplo de su uso:
 20/21: FTP (Transferencia de archivos).
 22: SSH (Acceso remoto seguro).
 25: SMTP (Envío de correos).
 53: DNS (Resolución de nombres).

 Puertos Dinámicos (Ephemeral Ports)
 Tiene un rango de 49152-65535
 Son puertos temporales que el sistema asigna automáticamente a las aplicaciones
 cliente cuando inician una conexión

NAT y problemas de conectividad entre redes distintas.
 NAT- Network Adress Translation
 Es un proceso que ayuda a múltiples dispositivos conectarse a una misma red de 
 internet mediantes una red local que comparte la misma dirección IP
 Dentro de los principales problemas de conectividad entre distintas redes son los siguientes;
 Invisibilidad del host: Negación de conexión a socket local de dispositivos externos
 Doble NAT: Dos routers en cadena operador y propio crean capas de traducción que rompen la 
 comunicación de videojuegos y VPNs
 Puertos dinámicos variables: cambios de los routers del puerto de origen rompiendo la conexión
 Latencia adicional: retraso en los envíos

Firewalls y permisos de puerto.
 Es el encargado de filtrar conexiones entrantes y salientes, su función dentro de los sockets 
 radica en decidir qué tráfico puede entrar o salir a través de los puertos específicos.
 Permisos de puerto según el nivel 
 1. ACLs (Access Control Lists) en Routers/Switches
 Son las "listas de invitados" de la red. Los administradores definen reglas basadas en:
 IP de origen/destino: 
 2. CGNAT (Carrier-Grade NAT)
 Definen qué IPs pueden hablar con qué puertos.
 Abre todos los puertos hacia una sola IP local (muy inseguro, solo para pruebas extremas).
 
Wi‑Fi Direct vs hotspot vs misma red: diferencias y limitaciones.
  Wi-Fi Direct: No tiene intermediario, velocidad alta, mínima latencia, su configuración es mediante discovery API, juegos multijugador locales
  Hotspot:El intermediario es el celular, su velocidad es media,  latencia media ¿, uso para transferir archivos de un dispositivo a otro
  Misma red: El intermediario es el router, velocidad media, latencia variable, uso en oficinas


Seguridad básica: TLS/SSL, recomendaciones para prueba, latencia media
 TLS/SSL: En este caso los datos se vuelven ilegibles para terceros.asegura que el mensaje no fue alterado en el camino.mediante certificados,
 el cliente confirma que el servidor es quien dice ser.
 Requiere un Handshake adicional (más mensajes de ida y vuelta antes de enviar datos).
 Recomendaciones para prueba:Certificados Self-Signed (Autofirmados) se pueden generar con OPPENSSL
 Si pruebas en la misma máquina, no necesitas TLS para la funcionalidad lógica, pero es mejor implementarlo desde el inicio para detectar errores de permisos.
 Latencia media:La latencia (o ping) es el tiempo que tarda un paquete en ir y volver. 
 En sockets, esto varía según la tecnología
 Red Local (Ethernet/Wi-Fi): < 1ms a 5ms.
 Fibra Óptica (Misma ciudad/país): 10ms a 30ms.
 Conexiones Transatlánticas: 100ms a 200ms.
 4G / 5G: 30ms a 80ms (muy variable según la cobertura).