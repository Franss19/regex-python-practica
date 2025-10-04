import re

# Patrón para detectar URLs comunes
patron = re.compile(
    r'((https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-z]{2,6}(/[a-zA-Z0-9._/-]*)?)'
)

# Pedir al usuario el texto
texto = input("Ingresa un texto que contenga URLs: ")

# Buscar URLs en el texto
urls = patron.findall(texto)

if urls:
    for i, url in enumerate(urls, start=1):
        url_completa = url[0]

        # Extraer protocolo
        protocolo = "https" if url[1].startswith("https") else "http" if url[1] else "No especificado"

        # Extraer dominio y
