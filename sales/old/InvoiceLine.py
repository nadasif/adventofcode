class InvoiceLine:
    def __init__(self, name, qty, price):
        self._name, self._qty, self._price = name, qty, price

    def name(self):
        return self._name

    def price(self):
        return self._price

    def qty(self):
        return self._price

    def _exampt(self):
        return any(s in self.name() for s in ['food', 'chocolate', 'pill'])

    def _imported(self):
        return "imported " in self.name()

    def taxes(self):
        rate = 0.0
        if self._exampt() and not self._imported():
            rate = 0.0
        elif self._imported() and self._exampt():
            rate = 0.05
        else:
            rate = 0.1

        return self.price() * self.qty() * rate

