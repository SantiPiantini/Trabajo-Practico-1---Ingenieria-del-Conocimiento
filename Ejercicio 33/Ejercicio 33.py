
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

precios_habitacion = {
    101: 150,
    102: 180,
    103: 200,
    104: 220,
    201: 250,
    202: 270
}

def habitaciones_ocupadas_en_fecha(reservas_dict, fecha):
    if fecha not in reservas_dict:
        return set()
    return {hab for _, hab, _ in reservas_dict[fecha]}

def habitaciones_disponibles_en_fecha(reservas_dict, fecha, precios):
    ocupadas = habitaciones_ocupadas_en_fecha(reservas_dict, fecha)
    return sorted([h for h in precios.keys() if h not in ocupadas])

def nueva_reserva_auto_precio(reservas_dict, fecha, nombre, habitacion, precios):
    if habitacion not in precios:
        return False, f"❌ La habitación {habitacion} no existe en la lista de tarifas."

    if fecha not in reservas_dict:
        reservas_dict[fecha] = []

    for _, hab, _ in reservas_dict[fecha]:
        if hab == habitacion:
            return False, f"Habitación {habitacion} no disponible el {fecha}."

    precio = precios[habitacion]
    reservas_dict[fecha].append((nombre, habitacion, precio))
    return True, f"Reserva confirmada para {nombre} en la habitación {habitacion} (precio: {precio}) el {fecha}."

def ingresos_por_fecha(reservas_dict, fecha):
    if fecha not in reservas_dict:
        return 0
    return sum(precio for _, _, precio in reservas_dict[fecha])

fecha = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ").strip()
nombre = input("Ingrese el nombre del huésped: ").strip()

while True:
    try:
        habitacion = int(input("Ingrese el número de habitación: ").strip())
    except ValueError:
        print("⚠️ Debe ingresar un número de habitación válido.")
        continue

    ok, mensaje = nueva_reserva_auto_precio(reservas, fecha, nombre, habitacion, precios_habitacion)
    if ok:
        print(mensaje)
        break
    else:
        print(mensaje)
        disponibles = habitaciones_disponibles_en_fecha(reservas, fecha, precios_habitacion)
        if not disponibles:
            print("No hay habitaciones disponibles para esa fecha.")
            break
        else:
            print("Habitaciones disponibles para esa fecha:", disponibles)
            print("Intenta con una de las habitaciones sugeridas.\n")

print("\nReservas actualizadas:", reservas)
print(f"Ingresos para {fecha}: {ingresos_por_fecha(reservas, fecha)}")
