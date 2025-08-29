#############################
def buscar_mayor(a, b, c):
    numeros = [a, b, c]
    numeros.sort(reverse=True)
    return numeros

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

resultado = buscar_mayor(num1, num2, num3)
print("Números ordenados de mayor a menor:", resultado)
