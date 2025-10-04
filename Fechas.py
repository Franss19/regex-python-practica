import re
from datetime import datetime

# Diccionario de meses en español
meses = {
    "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
    "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
    "septiembre": "09", "setiembre": "09", "octubre": "10",
    "noviembre": "11", "diciembre": "12",
    "ene": "01", "feb": "02", "mar": "03", "abr": "04",
    "may": "05", "jun": "06", "jul": "07", "ago": "08",
    "sep": "09", "oct": "10", "nov": "11", "dic": "12"
}

# Regex para distintos formatos
patrones = [
    (r"\b(\d{2})/(\d{2})/(\d{4})\b", "%d/%m/%Y"),             # DD/MM/YYYY
    (r"\b(\d{4})-(\d{2})-(\d{2})\b", "%Y-%m-%d"),             # YYYY-MM-DD
    (r"\b(\d{2})-([A-Za-z]{3})-(\d{4})\b", "%d-%b-%Y"),       # DD-MMM-YYYY
    (r"\b([A-Za-z]+)\s(\d{1,2}),\s(\d{4})\b", None)           # Mes DD, YYYY
]

# Pedir texto al usuario
texto = input("Ingresa un texto que contenga fechas: ")

print("\nFechas encontradas y convertidas:")

for patron, formato in patrones:
    for match in re.finditer(patron, texto):
        original = match.group(0)
        estandar = None

        try:
            if formato:  
                # Procesar directamente con datetime
                estandar = datetime.strptime(original, formato).strftime("%Y-%m-%d")
            else:
                # Caso de "Mes DD, YYYY"
                mes = match.group(1).lower()
                dia = int(match.group(2))
                anio = int(match.group(3))
                if mes in meses:
                    estandar = f"{anio}-{meses[mes]}-{dia:02d}"
        except:
            pass

        if estandar:
            print(f"- Formato original: {original} → Estándar: {estandar}")
