
def publicar(usuario, texto, **kwargs):
    publicacion = {
        "usuario": usuario,
        "texto": texto
    }
    publicacion.update(kwargs)
    return publicacion

post = publicar(
    "Juan",
    "Mi primer post!",
    etiquetas=["#hola", "#primerPost"],
    visibilidad="publica",
    likes=100
)

print(post)