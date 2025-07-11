from unittest.mock import patch
import sys

with patch.dict(sys.modules, {"freqtrade": object(), "freqtrade.configuration": object()}):
    from main import SuperBotTrading

def test_trading_init():
    bot = SuperBotTrading()
    assert bot.config is not None 