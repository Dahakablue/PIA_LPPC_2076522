#Serrano ALAN
#2076522
#Importar modulos
import requests
#Obtener la informacion HTML de la URL
URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
#Imprimir el texto de la peticion GET
print(page.text)
