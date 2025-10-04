import re

# Expresión regular (puedes cambiar a la estricta si quieres limitar TLDs)
patron = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$')

# Pedir al usuario su correo
correo = input("Ingresa tu correo electrónico: ")

# Validar
if patron.match(correo):
    print("✅ Correo válido")
else:
    print("❌ Correo inválido")
