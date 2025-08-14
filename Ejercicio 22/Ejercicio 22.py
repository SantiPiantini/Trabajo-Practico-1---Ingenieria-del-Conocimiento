paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def calcularTotal(paquetes):
    return {destino: precio * dias for destino, precio, dias in paquetes}

resultado = calcularTotal(paquetes)
print(resultado)