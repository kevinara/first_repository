from multiplicar import multiplicar

def test_multiplicar_in_range():
    got = multiplicar(5)
    want = "El número que digitaste es: 5"
    assert got == want

def test_multiplicar_out_of_range():
    got = multiplicar(76)
    want = "ERROR. \nEl número que se solicita debe estar en el rango entre 01 y 10."
    assert got == want