from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:

    def create_order(self, order):
        self.order = order
        if order == 'Pizza':
            return Pizza()
        elif order == 'Pasta':
            return Pasta()
        elif order == 'Salad':
            return Salad()