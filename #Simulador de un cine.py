#Simulador de un cine
asientos = 50
cine = []
dinero = []

def ingreso_cine(boleto):
    if len(cine) < asientos:
        if boleto not in cine:
            cine.append(boleto)
            dinero =  boleto*5
            print("La cantidad de boletos:", boleto, "se a realizado con exito, su total a pagar es de:", dinero ,"Muchas gracias.")
        else:
            print("Compra hecha con exito.")
    else:
        print("Sala de cine lleno.")

def entradas_vendidas(boleto):
    if boleto in cine:
        cine.remove(boleto)
        print("Boleto", boleto, "salió.")
    else:
        print("Vehículo no encontrado.")

def mostrar_espacios():
    disponibles = asientos - len(cine)
    print("Espacios disponibles:", disponibles)

while True:
    print(" ##### MEGACINE UTC #####  ")
    print("\nOpciones:")
    print("1. Comprar Entradas")
    print("2. Consultar Asientos Disponibles")
    print("3. Consultar Entradas Vendidas")
    print("4. Consultar Recaudacion total")
    print("5. Salir")
    opcion = input("Elija opción: ")

    if opcion == "1":
        print("Los boletos tienen un precio de 5$ por persona")
        boleto = input("¿Cuantas entradas desea comprar?: ").upper()
        ingreso_cine(boleto)
    elif opcion == "2":
        disponibles = asientos - len(cine)
        print("Asientos disponibles:", disponibles)
    elif opcion == "3":
        mostrar_espacios()
    elif opcion == "4":
        
        print("Recaudacion total es de:", dinero)
        
    elif opcion == "5":
        print("Gracias por visitar MEGACINES UTC")
    
        
