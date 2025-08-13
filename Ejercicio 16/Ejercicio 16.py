def crear_perfil(**kwargs):
    return dict(kwargs)

perfil = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")
print(perfil)