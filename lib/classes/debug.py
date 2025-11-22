
from customer import Customer
from coffee import Coffee
from order import Order

# reset class-level lists
Customer.all = []
Coffee.all = []
Order.all = []

# create customers
alice = Customer("Alice")
bob = Customer("Bob")

# create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# create orders
order1 = Order(alice, latte, 4.5)
order2 = Order(alice, espresso, 3.0)
order3 = Order(bob, latte, 5.0)
order4 = Order(bob, latte, 4.0)

# test relationships
print("=== Alice's Orders ===")
print(f"Orders: {len(alice.orders())}")
print(f"Coffees: {[c.name for c in alice.coffees()]}")

print("\n=== Latte Stats ===")
print(f"Num orders: {latte.num_orders()}")
print(f"Avg price: ${latte.average_price():.2f}")
print(f"Customers: {[c.name for c in latte.customers()]}")

print("\n=== Top Latte Spender ===")
top = Customer.most_aficionado(latte)
print(f"Most aficionado: {top.name}")

# test mutability
print("\n=== Mutability Tests ===")
alice.name = "Alicia"  
print(f"Customer name changed: {alice.name}")


import ipdb; ipdb.set_trace()