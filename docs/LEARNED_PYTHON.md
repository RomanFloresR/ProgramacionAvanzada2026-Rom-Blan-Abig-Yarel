

PARA SERVIDOR
Sockets y funciones clave: socket(), bind(), listen(), accept(), sendall(), recv(), `close() para comunicación TCP cliente-servidor.
Gestión de conexión: obtención automática de IP con socket.gethostname() y socket.gethostbyname().
Control de sesión: uso de time.time() para medir duración de la conexión.
Comunicación interactiva:input() para enviar mensajes desde el servidor al cliente.
Comandos especiales:

 `"Cerrar Cliente"` para finalizar conexión del cliente
 `"Cerrar Servidor"` para cerrar el servidor manualmente
  Manejo de cierre: función Cerrar_Servidor() que cierra connection.close()` y sock.close() liberando el puerto.
  Bucle principal:while True para escuchar múltiples intentos hasta cierre manual.
  Recepción de datos:recv(1024) con decodificación, decode() para mensajes del cliente.
  Envío de datos:sendall(mensaje.encode()), para respuesta del servidor.
  **Detección de desconexión:** validación if data: y condición else para romper el ciclo.
  Buenas prácticas implementadas:
 Separación de lógica en función `Cerrar_Servidor()`
 Mensajes de estado (`Esperando conexión`, `Conexión desde...`)
 Liberación del socket al cerrar
 Control de duración de conexión
 Manejo de cierre mediante comandos

 CLIENTE 
 Sockets y funciones clave: socket(), connect(), send(), recv(), close()para comunicación cliente-servidor TCP.
Configuración de conexión: variables host y port para definir IP y puerto del servidor.
Conexión al servidor: client.connect((host, port)) para establecer la sesión.
Comunicación interactiva: input() para enviar múltiples mensajes al servidor.
Envío de datos: client.send(mensaje.encode()) para transmitir mensajes al servidor.
Recepción de datos:recv(1024) con decode() para mostrar respuesta del servidor.
Bucle principal:while True permite comunicación continua cliente-servidor.

Comandos especiales

Cerrar Cliente cierra la conexión desde el cliente
Cerrar Servidot detecta que el servidor terminó la conexión

Control de cierre del cliente:

 envío del mensaje Cerrar Cliente
client.close() para liberar el socket
break para salir del ciclo

Detección de cierre del servidor:

 comparación`if a == "Cerrar Servidor
 mensaje `+El servidor cerro
 cierre del socket del cliente

Manejo de mensajes

variable respuesta almacena datos recibidos
variable a guarda el texto decodificado para validaciones




