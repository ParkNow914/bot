from unittest.mock import patch
import sys

with patch.dict(sys.modules, {"gpt4all": object()}):
    from main import SuperBotConteudo

def test_conteudo_init():
    bot = SuperBotConteudo()
    assert bot is not None 