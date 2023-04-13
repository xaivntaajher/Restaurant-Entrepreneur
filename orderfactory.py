from order import Order

class OrderFactory:

    def create_order(self, order):
        self.order = order
        if order == 'pizza':
            return Order('pizza', 20)
        elif order == 'pasta':
            return Order('pasta', 15)
        elif order == 'salad':
            return Order('salad', 7)