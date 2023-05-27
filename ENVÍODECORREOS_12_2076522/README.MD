*Envío de correos*
1. Se importan las librerías necesarias para el envío de correos y adjuntos: `EmailMessage` de `email.message` y `smtplib`.
2. Se definen las variables `remitente` y `destinatario` para especificar la dirección de correo del remitente y destinatario respectivamente.
3. Se define el contenido del mensaje en la variable `mensaje`. Se utiliza una estructura HTML básica para formatear el contenido del mensaje.
4. Se crea un objeto `EmailMessage` para representar el correo electrónico.
5. Se asigna el remitente, destinatario y asunto al objeto `EmailMessage`.
6. Se establece el contenido del mensaje utilizando el contenido definido en la variable `mensaje`, se especifica que el tipo de contenido es HTML.
7. Se utiliza el método `open` para abrir el archivo `LPCfcfm_cool.png` que se desea adjuntar al correo electrónico.
8. Se agrega el archivo adjunto al objeto `EmailMessage` utilizando el método `add_attachment`. Se especifica el nombre del archivo adjunto, el tipo principal (maintype) y el subtipo (subtype).
9. Se configuran los parámetros del servidor SMTP (`smtp.gmail.com` en el puerto `587`).
10. Se inicia una conexión segura utilizando `starttls`.
11. Se realiza la autenticación con el servidor SMTP utilizando el remitente y la contraseña.
12. Se envía el correo electrónico utilizando el método `sendmail` de SMTP, pasando el remitente, destinatario y el correo electrónico convertido a una cadena utilizando `as_string()`.
13. Finalmente, se cierra la conexión con el servidor SMTP utilizando `quit()`.

Este código muestra cómo enviar un correo electrónico utilizando Python, incluyendo la capacidad de adjuntar archivos al mensaje.
