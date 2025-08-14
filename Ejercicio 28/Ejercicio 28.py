biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def librosPost2000(diccionario):
    return [titulo for titulo, datos in diccionario.items() if datos["año"] > 2000]

resultado = librosPost2000(biblioteca)
print(resultado)