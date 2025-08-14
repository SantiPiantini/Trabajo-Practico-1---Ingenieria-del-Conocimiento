
def analizarFinanzas(**kwargs):
    return sum(kwargs.values())

balance = analizarFinanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print('El balance final es de ', balance)