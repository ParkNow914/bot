import sys
from unittest.mock import MagicMock

sys.modules["freqtrade"] = MagicMock()
sys.modules["freqtrade.configuration"] = MagicMock() 