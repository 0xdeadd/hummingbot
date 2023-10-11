from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


class Example2(ScriptStrategyBase):
    markets = {
        "binance_paper_trade": {"ETH-USDT"},
        "kucoin_paper_trade": {"ETH-USDT"},
        "gate_io_paper_trade": {"ETH-USDT"},
    }

    @property
    def format_status(self) -> str:
        """
        Returns status of the current strategy on user balances and current active orders. This function is called
        when status command is issued. Override this function to create custom status display output.
        """
        if not self.ready_to_trade:
            return "Market connectors are not ready."
        lines = []
        warning_lines = []
        warning_lines.extend(self.network_warning(self.get_market_trading_pair_tuples()))

        balance_df = self.get_balance_df()
        lines.extend(["", "  Balances:"] + ["    " + line for line in balance_df.to_string(index=False).split("\n")])
        market_status_df = self.get_market_status_df_with_depth()


        warning_lines.extend(self.balance_warning(self.get_market_trading_pair_tuples()))
        if len(warning_lines) > 0:
            lines.extend(["", "*** WARNINGS ***"] + warning_lines)
        return "\n".join(lines)

    def get_market_status_df_with_depth(self):
        market_status_df = self.market_status_data_frame(self.get_market_trading_pair_tuples())
        return market_status_df