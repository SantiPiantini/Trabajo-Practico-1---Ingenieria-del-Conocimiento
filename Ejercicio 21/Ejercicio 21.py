puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenar(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)

resultado = ordenar(puntuaciones)
print(resultado)