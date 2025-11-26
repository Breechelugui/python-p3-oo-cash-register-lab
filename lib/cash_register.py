class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self._last_transaction = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)

        transaction_amount = price * quantity
        self.total += transaction_amount
        self._last_transaction = transaction_amount

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discounted_total = self.total * (100 - self.discount) / 100.0

            if discounted_total.is_integer():
                discounted_total = int(discounted_total)

            self.total = discounted_total

            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self._last_transaction

        if isinstance(self.total, float) and self.total.is_integer():
            self.total = int(self.total)

        self._last_transaction = 0
