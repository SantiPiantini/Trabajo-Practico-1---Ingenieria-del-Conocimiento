usuarios = ["Ana", "Luis", "María"]

def configurar_perfiles(lista_usuarios, **kwargs):
    return {usuario: list(kwargs.items()) for usuario in lista_usuarios}

resultado = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
print(resultado)
