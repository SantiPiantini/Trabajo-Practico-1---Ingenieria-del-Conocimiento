estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_estudiantes(diccionario):
    promedios = {}
    for id_est, materias in diccionario.items():
        todas_notas = []
        for notas in materias.values():
            todas_notas.extend(notas)
        promedio_general = sum(todas_notas) / len(todas_notas)
        promedios[id_est] = promedio_general

    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    return ranking

resultado = ranking_estudiantes(estudiantes)
print("Ranking de estudiantes:")
for posicion, (id_est, promedio) in enumerate(resultado, start=1):
    print(f"{posicion}. ID {id_est} - Promedio: {promedio:.2f}")