precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def calcular_beneficio(precios, operaciones):
    beneficio = 0
    acciones_en_mano = False
    precio_compra = 0

    for operacion, dia in operaciones:
        if operacion == "compra" and not acciones_en_mano:
            precio_compra = precios[dia]
            acciones_en_mano = True
        elif operacion == "venta" and acciones_en_mano:
            beneficio += precios[dia] - precio_compra
            acciones_en_mano = False

    return beneficio

resultado = calcular_beneficio(precios_diarios, operaciones)
print(f"Beneficio/Pérdida total: {resultado}")