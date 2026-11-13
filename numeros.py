def analizar_numeros():
    numeros = []
    print("Por favor, ingresa 10 números:")
    
    # Solicitar 10 números mediante teclado
    for i in range(10):
        while True:
            try:
                num = float(input(f"Número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número real.")
    
    # Ordenar los números de mayor a menor (descendente) y de menor a mayor (ascendente)
    numeros_descendente = sorted(numeros, reverse=True)
    numeros_ascendente = sorted(numeros)
    
    # Identificar el número más alto y el más bajo
    maximo = max(numeros)
    minimo = min(numeros)
    
    # Presentar los resultados de manera clara
    print("\n--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Números ingresados (orden descendente - Mayor a Menor): {numeros_descendente}")
    print(f"Números ingresados (orden ascendente - Menor a Mayor): {numeros_ascendente}")
    print(f"Número más alto: {maximo}")
    print(f"Número más bajo: {minimo}")

analizar_numeros()
