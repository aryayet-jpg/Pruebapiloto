##############################3
def verificar_acceso(edad):
    if edad >= 18:
        return True
    else:
        return False

edad_usuario = int(input("Ingresa tu edad: "))

if verificar_acceso(edad_usuario):
    print("Eres mayor de edad. ¡Acceso permitido!")
else:
    print("Eres menor de edad. Acceso denegado.")
