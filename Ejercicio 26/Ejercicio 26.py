def registro_empleado(nombre, edad, salario, **kwargs):
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario
    }
    empleado.update(kwargs)
    return empleado

empleado = registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
print(empleado)