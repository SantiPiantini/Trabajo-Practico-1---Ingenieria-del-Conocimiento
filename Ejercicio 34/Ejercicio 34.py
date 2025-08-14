
encuestas = {
    "¿Cómo califica el servicio 1-5?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto 1=SI 0=NO?": [1, 1, 0, 1, 1, 0]
}

preguntas = list(encuestas.keys())

num_encuestados = int(input("Ingrese la cantidad de nuevas personas que responderán la encuesta: "))

for i in range(num_encuestados):
    print(f"\nEncuestado {i+1}:")
    for pregunta in preguntas:
        while True:
            try:
                respuesta = int(input(pregunta + " "))
                encuestas[pregunta].append(respuesta)
                break
            except ValueError:
                print("Respuesta inválida. Ingrese un número.")

def analizar_encuestas(diccionario):
    resultados = {}
    for pregunta, respuestas in diccionario.items():
        frecuencias = {}
        for respuesta in respuestas:
            frecuencias[respuesta] = frecuencias.get(respuesta, 0) + 1
        resultados[pregunta] = frecuencias
    return resultados

resultado = analizar_encuestas(encuestas)
print("\nResultados de la encuesta actualizados:")
for pregunta, frecs in resultado.items():
    print(f"\n{pregunta}")
    for valor, cantidad in frecs.items():
        print(f"  {valor}: {cantidad} respuestas")
