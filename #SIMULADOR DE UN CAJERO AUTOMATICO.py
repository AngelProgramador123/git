#SIMULADOR DE UN CAJERO
saldo = 0

while saldo >= 0:
    print("""
    ___CAJERO AUTOMATICO  ____
    1.Revisar saldo actual
    2.Transferir
    3.Retiro
    4.Salir
    ===================================
    """)

    operacion = int(input("Ingrese la operacion a realizar: "))

    match operacion:
        case 1:
            print(f"Saldo actual: {saldo: .2f}")

        case 2:
            deposito = float(input("Ingrese el monto ah depositar:$"))
            if deposito > 0:
                saldo += deposito
                print(f"Su saldo es: {saldo: .2f}")
            else:
                print("Deposito no valido")

        case 3:
            retiro = float(input("Ingrese el monto ah retirar:$"))
            if retiro <= 0:
                print("El valor debe ser mayor a 0")
            elif retiro > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= retiro
                print(f"Retiro con exito.Saldo restante: {saldo: .2f}")

        case 4:
            print("Gracias por utilizar este cajero")
            break
        case _:
            print("Opcion incorrecta")
            