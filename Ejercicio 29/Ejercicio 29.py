notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def promedios_estudiantes(lista):
    return {nombre: sum(calificaciones) / len(calificaciones) for nombre, calificaciones in lista}

resultado = promedios_estudiantes(notas_estudiantes)
print(resultado)