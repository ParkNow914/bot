from unittest.mock import patch
import sys

with patch.dict(sys.modules, {"requests": object(), "bs4": object(), "bs4.BeautifulSoup": object()}):
    from main import SuperBotAfiliados

def test_afiliados_init():
    bot = SuperBotAfiliados()
    assert bot is not None 