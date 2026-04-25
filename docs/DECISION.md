#Metodo elegido 
Para elaborar el trabajo solicitado, se utilizaron los 2 métodos de conexión, el primero fue el método de conexión mediante una misma red WI-FI,
en este caso, las dos computadoras se enlazaron a una misma red WI-FI.
Para el segundo caso las dos computadoras se conectaron a una misma red de hotspot de un dispositivo celular móvil, a este método se le llama hotspot. 

#Justificacion 
Se utilizo ambos métodos ya que esto mismo nos permitió ver y comparar la conectividad de este en diferentes situaciones y sobre todo su funcionamiento.
Comparando un poco, lo que pudimos observar son sus ventajas y desventajas de cada una de ellas.
Red WI-FI Direct 
Ventajas 
Algunas de las ventajas de esta red es que los datos se transmiten con una velocidad increíble y cuenta con una estabilidad muy buena de conexión etc.. 
Limitaciones  
Depende mucho de la calidad del router, si hay muchos dispositivos conectados a la misma red se vuelve muy lenta y va a tener muchas complicaciones. 
Una de las mas importantes es que si la red es publica, va a tener diferentes IP o también puede tener restricciones de seguridad la red. 
Hotspot 
Ventajas  
Una de sus grandes ventajas es que es portátil y permite realizar pruebas en diferentes lugares. 
A demás que es útil en entornos donde no se cuenta con WI-FI o donde no tengamos acceso a una red. 
Limitaciones 
Tiene un cierto límite de datos, consume mucha batería al momento de estar trabajando, 
su velocidad es muy lenta a comparación del WI-FI, también tiene un límite muy bajo de dispositivos para conectar. 


#Comandos usados 
Los comandos utilizados en el código nos permitieron la conexión entre el cliente y el servidor, para este punto utilizamos la consola de comandos (CMD), 
esta nos sirve para interpretar comandos en sistemas Windows NT, utilizado para administrar archivos, automatizar tareas y solucionar problemas mediante texto, 
y utiliza los comandos netsh wlan para configurar y activar la red. Primero, se define el nombre y la contraseña con netsh wlan set hostednetwork
mode=allow ssid=xd key=01234567890 y, luego se inicia la red con netsh wlan start hostednetwork. 


#Problemas encontrados 
Dentro de los problemas que se nos presentaron al momento de desarrollar el trabajo fue que equipo ocupa hardware adicional, la RIUV también fue un problema, 
también tuvimos que desconectar manualmente el internet, el socket continuaba abierto incluso cuando intentábamos cerrarlo. 
Las soluciones que le dimos a estos problemas fueron, buscar un nuevo lugar para poder trabajar, ya que con la RIUV como es una red pública nos arrojaba diferentes IP. 
Para lo del cierre del socket, se revisó el código hasta comprender el fallo y modificarlo.
