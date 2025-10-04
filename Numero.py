import re

# Patrón para números de teléfono mexicanos (10 dígitos en varios formatos)
patron = re.compile(
    r'(\d{10}|\d{3}-\d{3}-\d{4}|\d{3}\s\d{3}\s\d{4}|\(\d{3}\)\s?\d{3}-\d{4})'
)

# Pedir al usuario el texto
texto = input("Ingresa un texto que contenga números de teléfono: ")

# Buscar teléfonos en el texto
telefonos = patron.findall(texto)

# Mostrar resultados
if telefonos:
    print("📞 Teléfonos encontrados:", telefonos)
else:
    print("❌ No se encontraron teléfonos válidos.")
