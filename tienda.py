def calcular_descuento(compra):
    if compra <= 0:
        raise ValueError("El importe de la compra debe ser mayor que $0.")

    if compra > 10000:
        porcentaje = 15
    elif compra >= 5000:
        porcentaje = 10
    elif compra >= 1000:
        porcentaje = 5
    else:
        porcentaje = 0

    monto_descuento = round(compra * porcentaje / 100, 2)
    total = round(compra - monto_descuento, 2)
    return porcentaje, monto_descuento, total


def pedir_compra():
    while True:
        entrada = input("Ingresa el monto de la compra: $").strip()
        try:
            compra = float(entrada)
        except ValueError:
            print("Error: debe ingresar un número válido.\n")
            continue

        if compra <= 0:
            print("Error: el importe de la compra debe ser mayor que $0.\n")
            continue

        return compra


if __name__ == "__main__":
    compra = pedir_compra()
    porcentaje, monto_descuento, total = calcular_descuento(compra)

    print(f"Compra: ${compra:.2f}")
    print(f"Descuento: {porcentaje}%")
    print(f"Monto del descuento: ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
