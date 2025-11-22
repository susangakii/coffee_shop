class Coffee:
    all = []
    
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):  # only set once (immutable)
            if isinstance(value, str) and len(value) >= 3:
                self._name = value
            else:
                raise ValueError("Name must be a string with at least 3 characters")
    
    #return all orders for this coffee
    def orders(self):
        from lib.classes.order import Order
        return [order for order in Order.all if order.coffee == self]
    
    #return a unique list of customers who ordered this coffee (no duplicates)
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    #return the total number of orders for this coffee
    def num_orders(self):
        return len(self.orders())
    
    #return the average price of orders for this coffee
    def average_price(self):
        orders = self.orders()
        if orders:
            total = sum(order.price for order in orders)
            return total / len(orders)
        return 0
