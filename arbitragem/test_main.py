from unittest.mock import patch
import sys

with patch.dict(sys.modules, {"selenium": object(), "selenium.webdriver": object(), "bs4": object(), "bs4.BeautifulSoup": object()}):
    from main import SuperBotArbitragem

def test_arbitragem_init():
    bot = SuperBotArbitragem()
    assert bot is not None 