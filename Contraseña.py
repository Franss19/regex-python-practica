import re

def validar_contrasena(contrasena):
    errores = []

    # Criterios
    if len(contrasena) < 8:
        errores.append("Debe tener al menos 8 caracteres.")
    if not re.search(r"[A-Z]", contrasena):
        errores.append("Debe incluir al menos una letra mayúscula.")
    if not re.search(r"[a-z]", contrasena):
        errores.append("Debe incluir al menos una letra minúscula.")
    if not re.search(r"[0-9]", contrasena):
        errores.append("Debe incluir al menos un número.")
    if not re.search(r"[@$!%*?&#]", contrasena):
        errores.append("Debe incluir al menos un carácter especial (@$!%*?&#).")

    return errores

# Pedir al usuario su contraseña
contrasena = input("Ingresa tu contraseña: ")

# Validar
errores = validar_contrasena(contrasena)

if not errores:
    print("✅ Contraseña válida y segura.")
else:
    print("❌ Contraseña inválida. Faltan los siguientes requisitos:")
    for e in errores:
        print(" -", e)
