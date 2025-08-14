inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizarStock(viejo, vendidos):
    return [viejo[i] - vendidos[i] for i in range(len(vendidos))]


actualizado = actualizarStock(inventario, ventas)
print(actualizado)
