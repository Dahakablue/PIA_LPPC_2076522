Escáner de puertos
*Este código permite escanear un rango de puertos en un host específico y muestra los puertos abiertos encontrados. Es útil para realizar análisis de seguridad de red y descubrir qué puertos están accesibles en un sistema.

Se importan los módulos necesarios: sys para obtener los argumentos de la línea de comandos y socket para realizar operaciones de red.
Se obtiene el nombre del host y los números de puerto inicial y final a partir de los argumentos de la línea de comandos.
Se resuelve la dirección IP del host utilizando gethostbyname().
Se crea una lista vacía llamada opened_ports para almacenar los puertos abiertos encontrados.
Se itera a través de todos los puertos en el rango especificado (start_port a end_port).
Se crea un objeto de socket utilizando socket(AF_INET, SOCK_STREAM).
Se establece un tiempo de espera de 10 segundos para el socket utilizando settimeout(10).
Se utiliza connect_ex() en el socket para intentar establecer una conexión con el host y el puerto actual. El resultado de la conexión se almacena en la variable results.
Si results es igual a 0, significa que el puerto está abierto y se agrega a la lista opened_ports.
Después de recorrer todos los puertos, se imprime la lista de puertos abiertos encontrados.
