from logger import logger
from orderfactory import OrderFactory


class Franchise:
    def __init__(self,number):
        self.location_number = number
        
    def place_order(self):
        order = OrderFactory()
        print(f'Welcome to The Best Food You Ever Had, location #{self.location_number}')
        print('What would you like to order?')
        user_input = input("Enter '1' for Pizza, '2' for Pasta, '3' for Salad. ")
        print(user_input)

        while True:
            if user_input == str(1):
                return logger.log_transaction(order.create_order('Pizza'), self.location_number)
                
            elif user_input == str(2):
                return logger.log_transaction(order.create_order('Pasta'), self.location_number)
                
            elif user_input == str(3):
                return logger.log_transaction(order.create_order('Salad'), self.location_number)
                
            else:
                print('Invalid Input')
                return


             