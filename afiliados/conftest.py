import sys
from unittest.mock import MagicMock

sys.modules["requests"] = MagicMock()
sys.modules["bs4"] = MagicMock()
sys.modules["bs4.BeautifulSoup"] = MagicMock() 