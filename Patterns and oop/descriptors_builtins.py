class Order:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

    # Called only if undefined attribute was called
    def __getattr__(self, item):
        return f'Attr {item} not exists'

    def __setattr__(self, key, value):
        if key in ('value', 'price'):
            if value <= 0:
                raise ValueError(f'{key} can not be negative')
        return super().__setattr__(key, value)


apple_order = Order('apple', 1, 10)

# Will write "not exists"
print(apple_order.hey)

# Will throw error as expected cause (value || price) can not be negative
# apple_order.value = -4

# Will work fine
apple_order.new_attr = -4

print(apple_order.price)
