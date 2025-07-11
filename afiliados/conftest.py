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

# Mock requests
requests_mock = MagicMock()
requests_mock.get = MagicMock()
requests_mock.post = MagicMock()
sys.modules["requests"] = requests_mock 