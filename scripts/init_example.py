from hummingbot.strategy.script_strategy_base import ScriptStrategyBase

class InitialExample(ScriptStrategyBase):
    markets = {"binance_paper_trade": {"BTC-USDT", "ETH-USDT"}}

    def on_tick(self):
        self.logger().info("First Script !")