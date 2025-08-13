empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def empleadosConSalarioMayor(diccionario, salarioTope):
    return{id_emp: datos for id_emp, datos in diccionario.items() if datos[2] > salarioTope}


maximo = int(input("Introduce un salario tope: "))
resultado = empleadosConSalarioMayor(empleados, maximo)

print(resultado)