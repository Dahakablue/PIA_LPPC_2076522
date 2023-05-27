Escaneo de equipos activos en la subred

Este script realiza un escaneo de equipos activos en la subred. A continuación se describe brevemente lo que sucede en cada parte del script:

Determina el gateway utilizando el comando Get-NetRoute y almacena el valor en la variable $subred.
Muestra el gateway detectado en la salida.
Determina el rango de subred utilizando manipulaciones de cadenas en la variable $subred y lo almacena en la variable $rango.
Verifica si el rango de subred termina en punto y agrega un punto si es necesario.
Crea un array con los números del 1 al 254 y lo almacena en la variable $rango_ip.
Muestra información sobre la subred actual en la salida.
Itera sobre cada número en el rango de IP y genera una dirección IP.
Realiza una prueba de conexión con cada dirección IP utilizando el comando Test-Connection.
Si la conexión es exitosa, muestra un mensaje indicando que el host responde.
