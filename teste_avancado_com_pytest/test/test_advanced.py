import pytest
from teste_avancado_com_pytest.exercise import str_to_bool


@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    # verificar casos de teste com as opções Y y 1 YES
    assert str_to_bool(string) is True

@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    #verificar casos de teste com as opções N n O NO
    assert str_to_bool(string) is False

