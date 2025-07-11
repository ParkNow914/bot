import sys
from unittest.mock import MagicMock

# Mock BeautifulSoup
class MockBeautifulSoup:
    def __init__(self, *args, **kwargs):
        self.find_all = MagicMock(return_value=[])
        self.find = MagicMock(return_value=None)
        self.text = "Conteúdo simulado"
        self.get = MagicMock(return_value="")

bs4_mock = MagicMock()
bs4_mock.BeautifulSoup = MockBeautifulSoup
sys.modules["bs4"] = bs4_mock

# Mock Selenium
selenium_mock = MagicMock()
selenium_mock.webdriver = MagicMock()
selenium_mock.webdriver.Chrome = MagicMock()
selenium_mock.webdriver.Chrome.return_value = MagicMock()

sys.modules["selenium"] = selenium_mock
sys.modules["selenium.webdriver"] = selenium_mock.webdriver 