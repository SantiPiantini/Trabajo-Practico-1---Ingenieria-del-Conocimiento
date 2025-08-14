hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def filtrar_tendencias(hashtags_array, tendencias_lista, minimo):
    return [hashtag for hashtag, frecuencia in tendencias_lista if frecuencia > minimo]

resultado = filtrar_tendencias(hashtags, tendencias, 100)
print(resultado)
