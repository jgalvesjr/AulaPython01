import operacoes
import pytest 
def testarSomar():
    assert operacoes.somar(1,1) == 2

def testarSubtrair():
    assert operacoes.subtrair(2,1)  == 1
    
def testarMultiplicar():
    assert operacoes.multiplicar(2,3) == 6
    
def testarDividir():
    assert operacoes.dividir(4,2) == 2
    with pytest.raises(ValueError):
        operacoes.dividir(1,0)

# python -m pytest -vv

#executar python -m pytest -vv pelo codigo
if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__, "-vv"]))