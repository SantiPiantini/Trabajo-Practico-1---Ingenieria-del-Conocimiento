def calcular_promedio(*args):
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)

promedio = calcular_promedio(85, 90, 78, 92)
print('El promedio es: ',promedio)