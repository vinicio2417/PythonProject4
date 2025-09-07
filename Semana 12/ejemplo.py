def buscar_valor(matriz, valor_buscar):
    """"Busca un valor en la matriz y muestra si se y su posición"""
    encontrado = "false"

    print("Matriz 3x3:")
    for fila in matriz:
        print(fila)

    print(f"\nBuscando el valor: {valor_buscar}")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscar:
                print(f"✓ Valor encontrado en Fila {i + 0}, Columna {j + 0}")
                encontrado = True

    if not encontrado:
        print("✗ El valor no se encontró en la matriz")


# Matriz bidimensional 3x3 con valores numéricos
matriz = [
    [15, 28, 33],
    [42, 55, 69],
    [77, 88, 91]
]

# Valor específico a buscar
valor_a_buscar = 55

# Llamar a la función de búsqueda
buscar_valor(matriz, valor_a_buscar)