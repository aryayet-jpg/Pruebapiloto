##############################
def es_par(numero):
    return numero % 2 == 0

num = int(input("Ingrese un número: "))

if es_par(num):
    print(f"El número {num} es PAR.")
else:
    print(f"El número {num} es IMPAR.")
