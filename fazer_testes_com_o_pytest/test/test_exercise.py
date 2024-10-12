import sys
import os
import pytest

# Adiciona o caminho para o diretório raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from fazer_testes_com_o_pytest.exercise import admin_command


class TestAdminCommand:

    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected
        
    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True)
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"
