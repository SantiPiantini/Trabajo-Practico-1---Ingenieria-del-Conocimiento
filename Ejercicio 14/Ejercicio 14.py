temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def tempAnalisis(datos):
    promedio = sum(datos) / len(datos)
    maximo = max(datos)
    minimo = min(datos)
    return promedio, maximo, minimo

promedio, maximo, minimo = tempAnalisis(temperaturas)

print('La temperatura promedio es: ', promedio)
print('La temperatura maxima es: ', maximo)
print('La temperatura minima es: ', minimo)