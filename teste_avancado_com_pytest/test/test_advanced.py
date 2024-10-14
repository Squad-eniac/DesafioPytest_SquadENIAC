import pytest
import os

from teste_avancado_com_pytest.exercise import str_to_bool


@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    # verificar casos de teste com as opções Y y 1 YES
    assert str_to_bool(string) is True

@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    #verificar casos de teste com as opções N n O NO
    assert str_to_bool(string) is False
    
@pytest.fixture
def temp_file(tmpdir):
    """
    Fixture para criar um arquivo temporário para os testes
    """
    temp_file = tmpdir.join('temp_file.txt')
    temp_file.write('Teste')
    return temp_file

class TestFile:
    def test_f(self, tmpfile):
        """
        Testa se o arquivo temporário foi criado corretamente e verifica seu conteúdo.
        """
        # Verifica se o arquivo existe
        assert tmpfile.exists()

        # Verifica o conteúdo do arquivo
        content = tmpfile.read()
        assert content == "conteúdo temporário"

