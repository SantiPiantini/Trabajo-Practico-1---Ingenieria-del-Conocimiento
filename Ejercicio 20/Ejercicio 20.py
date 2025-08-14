
def configApp(**kwargs):
    return dict(kwargs)

configuracion = configApp(modoOscuro=True, idioma="es", notificaciones=False)
print(configuracion)
