#####################333333333

def calcular_edad(aÑo_nacimiento):
    # Obtener el año actual
    anio_actual = datetime.datetime.now().year
    # Calcular la edad
    edad = anio_actual - anio_nacimiento
    return edad

# Pedir al usuario que ingrese su año de nacimiento
anio = int(input("Ingresa tu año de nacimiento: "))

# Calcular y mostrar la edad
edad = calcular_edad(anio)
print(f"Tienes {edad} años.")
