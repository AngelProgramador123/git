#SIMULADOR DE UN CAJERO AUTOMATICO
capacidad = 50
parqueadero = []

def ingresar_vehiculo(placa):
    if len(parqueadero) < capacidad:
        if placa not in parqueadero:
            parqueadero.append(placa)
            print("Vehículo", placa, "ingresado.")
        else:
            print("El vehículo ya está dentro.")
    else:
        print("Parqueadero lleno.")

def sacar_vehiculo(placa):
    if placa in parqueadero:
        parqueadero.remove(placa)
        print("Vehículo", placa, "salió.")
    else:
        print("Vehículo no encontrado.")

def mostrar_espacios():
    disponibles = capacidad - len(parqueadero)
    print("Espacios disponibles:", disponibles)

while True:
    print(" ##### BIENVENIDO AL PARQUEADERO 1 UTC #####  ")
    print("\nOpciones:")
    print("1. Ingresar vehículo")
    print("2. Sacar vehículo")
    print("3. Mostrar espacios")
    print("4. Salir")
    opcion = input("Elija opción: ")

    if opcion == "1":
        placa = input("Ingrese placa: ").upper()
        ingresar_vehiculo(placa)
    elif opcion == "2":
        placa = input("Ingrese placa: ").upper()
        sacar_vehiculo(placa)
    elif opcion == "3":
        mostrar_espacios()
    elif opcion == "4":
        print("Gracias por utilizar nuestros servicios")
        break
    else:
        print("Opción inválida.")
