import pytest
from tienda import calcular_descuento


@pytest.mark.parametrize("compra, porcentaje_esperado", [
    (500, 0),
    (999.99, 0),
    (1000, 5),
    (4999.99, 5),
    (5000, 10),
    (10000, 10),
    (10000.01, 15),
    (25000, 15),
])
def test_porcentaje_segun_rango(compra, porcentaje_esperado):
    porcentaje, _, _ = calcular_descuento(compra)
    assert porcentaje == porcentaje_esperado


def test_calculo_de_descuento_y_total():
    porcentaje, descuento, total = calcular_descuento(6000)
    assert porcentaje == 10
    assert descuento == 600.00
    assert total == 5400.00


def test_total_mas_descuento_igual_a_compra():
    _, descuento, total = calcular_descuento(12345.67)
    assert round(descuento + total, 2) == 12345.67


@pytest.mark.parametrize("compra_invalida", [0, -1, -5000])
def test_importe_no_positivo_lanza_error(compra_invalida):
    with pytest.raises(ValueError):
        calcular_descuento(compra_invalida)
