##########################3
 def convertir_minutos(minutos):
    horas = minutos // 60         
    minutos_sobrantes = minutos % 60  
    return horas, minutos_sobrantes

minutos_ingresados = int(input("Ingrese la cantidad de minutos: "))
h, m = convertir_minutos(minutos_ingresados)
print(f"{minutos_ingresados} minutos son {h} hora(s) y {m} minuto(s).")
