suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):

    if usuario not in suscripciones:
        suscripciones[usuario] = []

    suscripciones[usuario].append(suscripcion)

    if kwargs:
        suscripciones[usuario].append(kwargs)

    return suscripciones

resultado = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(resultado)
