import sys
from unittest.mock import MagicMock

sys.modules["selenium"] = MagicMock()
sys.modules["selenium.webdriver"] = MagicMock()
sys.modules["bs4"] = MagicMock()
sys.modules["bs4.BeautifulSoup"] = MagicMock() 