compra = float(input("Ingresa el monto de la compra: $"))

if compra < 0:
    print("Error: el monto de la compra no puede ser negativo.")
else:
    if compra > 10000:
        descuento = 0.15
    elif compra >= 5000:
        descuento = 0.10
    elif compra >= 1000:
        descuento = 0.05
    else:
        descuento = 0

    monto_descuento = compra * descuento
    total = compra - monto_descuento

    print(f"\nCompra: ${compra:.2f}")
    print(f"Porcentaje de descuento: {descuento * 100:.0f}%")
    print(f"Monto del descuento: ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
