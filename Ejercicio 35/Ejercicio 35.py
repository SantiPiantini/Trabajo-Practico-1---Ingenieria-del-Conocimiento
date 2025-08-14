
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def filtrar_rutas(rutas, maximos):
    if len(rutas) != len(maximos):
        raise ValueError("La cantidad de rutas y de distancias máximas debe coincidir.")
    return [ruta for ruta, max_dist in zip(rutas, maximos) if ruta[2] <= max_dist]

validas = filtrar_rutas(rutas, distancias_max)
print(validas)