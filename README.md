# Coffee Shop Order System

A Python object-oriented programming (OOP) project modeling relationships between customers, coffees, and orders in a coffee shop system.

## Description

This project implements a coffee shop ordering system with three main classes: `Customer`, `Coffee`, and `Order`. It demonstrates object-oriented programming principles including encapsulation, property decorators, class methods, and aggregate methods for analyzing order data.

## Project Structure

```
coffee-shop/
├── lib/
│   └── classes/
│       ├── __init__.py
│       ├── customer.py
│       ├── coffee.py
│       ├── debug.py
│       └── order.py
├── tests/
│   ├── __init__.py
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── __init__.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Features

- **Customer Management**: Create and track customers with validated names
- **Coffee Tracking**: Manage coffee types and their orders
- **Order System**: Record orders with price validation
- **Analytics**: Calculate average prices, count orders, and identify top customers

## Installation

1. Clone the repository
2. Install dependencies using Pipenv:

```bash
pipenv install
```

3. Activate the virtual environment:

```bash
pipenv shell
```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests and stop at first failure:

```bash
pytest -x
```

## Classes

### Customer
- Manages customer information with mutable names (1-15 characters)
- Tracks all orders placed by the customer
- Creates new orders
- Identifies customers who spent the most on specific coffees

### Coffee
- Represents coffee types with immutable names (minimum 3 characters)
- Tracks all orders for the coffee
- Calculates average price and total order count
- Lists all customers who ordered the coffee

### Order
- Links customers to coffees with prices ($1.0-$10.0)
- Immutable once created
- Validates customer and coffee instances
- Maintains a registry of all orders

## License

This project is licensed under the MIT License.

## Author

Susan Gakii - Code Challenge