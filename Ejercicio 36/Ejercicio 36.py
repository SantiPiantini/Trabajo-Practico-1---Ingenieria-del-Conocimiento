inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}



def actualizar_inventario(tienda, **kwargs):
    if tienda not in inventario:
        return f"La tienda '{tienda}' no existe en el inventario."

    for producto, cambio in kwargs.items():
        if producto in inventario[tienda]:
            inventario[tienda][producto] += cambio
        else:
            inventario[tienda][producto] = cambio

    return inventario


resultado = actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)
print(resultado)