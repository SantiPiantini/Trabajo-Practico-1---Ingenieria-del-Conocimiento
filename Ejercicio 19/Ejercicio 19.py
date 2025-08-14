resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calcularGoles(diccionario):
    favor = sum(goles[0] for goles in diccionario.values())
    contra = sum(goles[1] for goles in diccionario.values())
    return favor, contra

favor, contra = calcularGoles(resultados)

print('Goles a favor ', favor)
print('Goles a contra', contra)