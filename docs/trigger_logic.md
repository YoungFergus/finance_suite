Equity Buy Trigger:

1. Reaches a date and invests all saved money into stock
2. Price goes {x}% below the 50 day moving average
Class Investment()
    self.ticker = None

    def get_recent_data()
        # query database with current data or the most recent date

Class Equity()
    self.current_price
    self.moving_average_50
    self.buy_threshold #percent to buy the stock at

equity_buy_trigger
    percent_diff = ABS(self.current_price - self.moving_average_50)/(self.moving_average_50)
    if percent_diff > self.buy_threshold
        


    