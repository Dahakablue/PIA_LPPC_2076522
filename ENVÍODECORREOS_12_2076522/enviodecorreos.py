#Serrano Lara Alan David
#2076522
#Importando librerias necesarias para el envío y los adjuntos en los mails
from email.message import EmailMessage
import smtplib
remitente = "pruebapia2023@gmail.com"
destinatario = "david.serrano.gallo@gmail.com "
mensaje = """<head><strong>Practica 12</strong><head/></br>
</br><body>Ejercicio de la Practica 12 para envío de correos. 
</br></br><strong>Alumno: </strong>Serrano Alan
</br></br><strong>Matricula: </strong>2076522</body>"""
#Metodo para llenar la información del remitente, destinatario y asunto del mail
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Prueba de envío (script python) 1756734"
email.set_content(mensaje, subtype="html")
#Metodo open para abrir el archivo que queremos adjuntar
with open("C:\Users\Alan Lara\OneDrive\Escritorio\evidencias\LPCfcfm_cool.png", "rb") as f:
    email.add_attachment(
        f.read(),
        filename="fcfm_cool.png",
        maintype="fcfm_cool.png",
        subtype="png"
    )
   #Parametros SMTP para indicar el servidor y el puerto para realizar el envío
smtp = smtplib.SMTP("smtp.gmail.com", port=587)
#smtp = SMTP("smtp.gmail.com", port=587)
smtp.starttls()
smtp.login(remitente, "")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()
