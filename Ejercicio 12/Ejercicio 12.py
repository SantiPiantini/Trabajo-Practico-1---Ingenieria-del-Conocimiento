# Lista de productos como tuplas
productos= [
    ('laptop', 1200, 5),
    ('mouse', 25, 50),
    ('teclado', 100, 30)
]

def productoMasCaro(listaProductos):
    return max(listaProductos, key=lambda producto: producto[1])

masCaro = productoMasCaro(productos)
print('El prodcuto mas caro es: ', masCaro[0], 'con valor: ', masCaro[1] )