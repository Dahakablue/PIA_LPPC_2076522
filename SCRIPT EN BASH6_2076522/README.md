Superscan.sh

Este script muestra un menú principal en la terminal con diferentes opciones. El usuario puede ingresar un número del 1 al 4 para seleccionar una opción. Dependiendo de la opción seleccionada, se ejecutará un script correspondiente al número elegido. Las opciones disponibles son:

Net Discover: Ejecuta el script netdiscover.sh ubicado en el escritorio.
Port scan: Ejecuta el script portscanv1.sh ubicado en el escritorio.
Welcome: Ejecuta el script welcome.sh ubicado en el escritorio.
Exit: Muestra el mensaje "Adios!" y finaliza el script.
portscanv1.sh

Este script realiza un escaneo de puertos en una dirección IP específica. Se define una variable direccion_ip que contiene la dirección IP objetivo y una variable puertos que contiene una lista de puertos separados por comas.

Luego, utiliza un bucle for para iterar sobre cada puerto en la lista puertos. Para cada puerto, se intenta establecer una conexión utilizando el comando timeout y redirigiendo la salida a /dev/null. Si la conexión se establece correctamente, se imprime un mensaje indicando que el puerto está abierto. Si la conexión no se puede establecer, se imprime un mensaje indicando que el puerto está cerrado.

number.sh

Este script solicita al usuario que proporcione tres números y luego los muestra en la salida. Utiliza el comando read para leer los valores ingresados por el usuario y los almacena en las variables n1, n2 y n3. Luego, muestra los valores ingresados en la salida utilizando el comando echo.

netdiscover.sh

Este script realiza un escaneo básico de red. Primero, verifica si el comando ifconfig está disponible. Si está disponible, utiliza ifconfig para obtener la dirección IP y la subred del sistema. Si el comando ifconfig no está disponible, utiliza el comando ip para obtener la dirección IP y la subred.

Luego, utiliza un bucle for para iterar sobre todas las direcciones IP posibles dentro de la subred. Para cada dirección IP, realiza un ping y verifica si recibe una respuesta. Si recibe una respuesta, imprime un mensaje indicando que el host responde.
