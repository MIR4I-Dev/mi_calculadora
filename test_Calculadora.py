import pytest
from Calculadora import Calculadora

def test_sumar():
    calc=Calculadora()
    assert calc.sumar(3,5)==8
    assert calc.sumar(-3,-23)==-26
    assert calc.sumar(0,0)==0
    
    
def test_restar():
    calc=Calculadora()
    assert calc.restar(10,5)==5
    assert calc.restar(-2,-13)==11
    assert calc.restar(0,0)==0
    
def test_multiplicar():
    calc=Calculadora()
    assert calc.multiplicar(2,4)==8
    assert calc.multiplicar(12,20)==240
    assert calc.multiplicar(0,0)==0
    
def test_dividir():
    calc=Calculadora()
    assert calc.dividir(10,2)==5
    assert calc.dividir(2,4)==0.5
    assert calc.dividir(40,4)==10
    with pytest.raises(ValueError):
        calc.dividir(40,0)