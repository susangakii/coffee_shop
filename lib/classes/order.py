class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not hasattr(self, '_price'):  # only set once (immutable)
            if isinstance(value, (int, float)) and 1.0 <= value <= 10.0:
                self._price = float(value)
            else:
                raise ValueError("Price must be a number between 1.0 and 10.0")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from lib.classes.customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be a Customer instance")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from lib.classes.coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be a Coffee instance")