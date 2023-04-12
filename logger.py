class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, Order, number):
        self.transaction_count =+ 1


        Order = open('log.txt', 'a')
        Order.write(f'TRX#{self.transaction_count}: {self.dish_name} at {self.number}. Total: {self.daily_sales + self.price}')
        Order.close()
