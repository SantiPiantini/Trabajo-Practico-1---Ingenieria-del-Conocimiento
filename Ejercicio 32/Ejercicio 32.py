def simularVentas(*args):
    totalIngresos = sum(cantidad * precio for _, cantidad, precio in args)
    return totalIngresos

total = simularVentas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print(f"Total de ingresos: ${total}")