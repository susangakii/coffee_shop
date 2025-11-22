class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value): #mutable (can be changes once instantiated)
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
    
    #returns all orders for this customer
    def orders(self):
        from lib.classes.order import Order
        return [order for order in Order.all if order.customer == self]
    
    #returns unique list of coffees this customer has ordered
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    #creates a new order for this customer
    def create_order(self, coffee, price):
        from lib.classes.order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        #returns customer who spent the most on a given coffee
        customers_spending = {}
        from lib.classes.order import Order
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customers_spending:
                    customers_spending[order.customer] = 0
                customers_spending[order.customer] += order.price
        
        if not customers_spending:
            return None
        return max(customers_spending, key=customers_spending.get)