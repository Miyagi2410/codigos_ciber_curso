import requests
from bs4 import BeautifulSoup, Comment
import re

#la URL del sitio 
url = "http://127.0.0.1:8000/victima.html"
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, "html.parser")

# extrae los enlaces y los muestra
enlaces = []
for a in soup.find_all("a", href=True):
    enlaces.append(a["href"])
print("Enlaces encontrados:")
print("\n".join(enlaces))

# extrae los comentarios y los muestra 
comentarios = [comentario for comentario in soup.find_all(string=lambda texto: isinstance(texto, Comment))]
print("\nComentarios encontrados:")
print("\n".join(comentarios))

# extrae los correos y los muestra
patron_correo = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
correos_encontrados = patron_correo.findall(soup.text)

print("\nCorreos electronicos encontrados:")
print("\n".join(correos_encontrados))
