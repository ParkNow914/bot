import sys
from unittest.mock import MagicMock

# Mock selenium antes de qualquer import
mock_selenium = MagicMock()
mock_selenium.webdriver = MagicMock()
mock_selenium.webdriver.Chrome = MagicMock()
mock_selenium.webdriver.Chrome.return_value = MagicMock()

sys.modules["selenium"] = mock_selenium
sys.modules["selenium.webdriver"] = mock_selenium.webdriver 