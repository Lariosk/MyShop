import pytest

def calcular_descuento(compra):
    if compra > 10000:
        return 0.15
    elif compra >= 5000:
        return 0.10
    elif compra >= 1000:
        return 0.05
    else:
        return 0

# --- Pruebas unitarias con pytest ---
@pytest.mark.parametrize("compra, esperado", [
    (500, 0.0),
    (1000, 0.05),
    (5000, 0.10),
    (12000, 0.15)
])
def test_descuentos(compra, esperado):
    assert calcular_descuento(compra) == esperado


# --- Ejecución interactiva por consola (Opcional si se ejecuta como script) ---
if __name__ == "__main__":
    try:
        compra = float(input("Ingresa el monto de la compra: $"))
        
        if compra < 0:
            print("Error: El monto no puede ser negativo.")
        else:
            descuento = calcular_descuento(compra)
            monto_descuento = compra * descuento
            total = compra - monto_descuento

            print(f"\nCompra: ${compra:.2f}")
            print(f"Descuento: {descuento * 100:.0f}%")
            print(f"Monto del descuento: ${monto_descuento:.2f}")
            print(f"Total a pagar: ${total:.2f}")
            
    except ValueError:
        print("Error: Ingresa un valor numérico válido.")