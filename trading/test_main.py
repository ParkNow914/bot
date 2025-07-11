from main import SuperBotTrading

def test_trading_init():
    bot = SuperBotTrading()
    assert bot.config is not None 