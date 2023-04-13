from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:

    def create_order(self, order):
        self.order = order
        if order == 'pizza':
            return Pizza()
        elif order == 'pasta':
            return Pasta()
        elif order == 'salad':
            return Salad()