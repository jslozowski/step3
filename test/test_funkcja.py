from tkinter.filedialog import test
import funkcja

def test_potega_dodatnia():
    assert funkcja.potega_dodatnia(2,2) == 4
    assert funkcja.potega_dodatnia(2,4) == 16
    assert funkcja.potega_dodatnia(2,0) == 1
    assert funkcja.potega_dodatnia(5,-1) == "b ma byc dodatnie"

test_potega_dodatnia()

def test_dodawanie_dwoch():
    assert funkcja.dodawanie_dwoch(2,2) == 4
    assert funkcja.dodawanie_dwoch(2,0) == 2
    assert funkcja.dodawanie_dwoch(2,-1) == 1

test_dodawanie_dwoch()