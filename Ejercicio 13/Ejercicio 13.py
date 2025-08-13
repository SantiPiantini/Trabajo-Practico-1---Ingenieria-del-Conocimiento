estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promedioEstudiante(registros, matricula):
    if matricula in registros:
        calificaciones = registros[matricula]['calificaciones'].values()
        return sum(calificaciones) / len(calificaciones)
    else:
        return None


matricula = int(input("Ingresa tu matricula: "))
promedio = promedioEstudiante(estudiantes, matricula)

if promedio is not None:
    print(f'El promedio de {estudiantes[matricula]['nombre']} es: {promedio}')
else:
    print('No se encontro el numero de matricula')