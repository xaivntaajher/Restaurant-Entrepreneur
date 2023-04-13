class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, Order, location_number):
        self.transaction_count =+ 1

        log = open('log.txt', 'a')
        log.write(f'TRX#{self.transaction_count}: {Order.dish_name} at {location_number} - ${Order.price}.Total: ${self.daily_sales + Order.price} \n')
        log.close()
