from logger import Logger
from orderfactory import OrderFactory


class Franchise:
    def __init__(self,number):
        self.location_number = number
        
    def place_order(self):
        log = Logger()
        order = OrderFactory()
        print(f'Welcome to The Best Food You Ever Had, location #{self.location_number}')
        print('What would you like to order?')
        user_input = input("Enter '1' for pizza, '2' for pasta, '3' for salad. ")
        print(user_input)
    
        if user_input == str(1):
            log.log_transaction(order.create_order('pizza'), self.location_number)
            
        elif user_input == str(2):
            log.log_transaction(order.create_order('pasta'), self.location_number)
            
        elif user_input == str(3):
            log.log_transaction(order.create_order('salad'), self.location_number)
            
        else:
            print('Invalid Input')
            

