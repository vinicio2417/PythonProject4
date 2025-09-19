def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento de una compra y el monto final a pagar.
    Retorna (descuento, monto_final).
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final


# Lista vacía para guardar las compras
compras = []

# Pedir al usuario cuántas compras quiere calcular
n = int(input("¿Cuántas compras desea ingresar? "))

for i in range(n):
    print(f"\nCompra {i + 1}:")
    monto = float(input("Ingrese el monto de la compra: "))

    # Preguntar si desea ingresar un porcentaje personalizado
    usar_personalizado = input("¿Desea ingresar un porcentaje de descuento? (s/n): ").lower()

    if usar_personalizado == "s":
        porcentaje = float(input("Ingrese el porcentaje de descuento: "))
        compras.append((monto, porcentaje))
    else:
        compras.append((monto,))  # Solo monto, aplica 10% por defecto

# Mostrar resultados en tabla
print("\nResultados:")
print(f"{'Monto Compra':>12} | {'% Descuento':>12} | {'Descuento':>10} | {'Monto Final':>12}")
print("-" * 55)

for compra in compras:
    if len(compra) == 1:
        descuento, final = calcular_descuento(compra[0])
        porcentaje = 10  # valor por defecto
    else:
        descuento, final = calcular_descuento(compra[0], compra[1])
        porcentaje = compra[1]

    print(f"{compra[0]:>12.2f} | {porcentaje:>12}% | {descuento:>10.2f} | {final:>12.2f}")