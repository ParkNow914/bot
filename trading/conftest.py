import sys
from unittest.mock import MagicMock

# Mock freqtrade antes de qualquer import
mock_freqtrade = MagicMock()
mock_freqtrade.configuration = MagicMock()
mock_freqtrade.configuration.Configuration = MagicMock()
mock_freqtrade.configuration.Configuration.return_value = MagicMock()

sys.modules["freqtrade"] = mock_freqtrade
sys.modules["freqtrade.configuration"] = mock_freqtrade.configuration 