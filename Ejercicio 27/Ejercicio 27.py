ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def calcularVentas(ventas):
    total = sum(ventas)
    prom = total / len(ventas)
    maximo = ventas.index(max(ventas)) + 1
    return total, prom, maximo


total, prom, maximo = calcularVentas(ventas_mensuales)
print('Total de ventas mensuales: ', total)
print('Promedio de ventas mensuales: ', prom)
print('Maximo de ventas mensuales: ', maximo)