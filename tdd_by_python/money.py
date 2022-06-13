from .expression import Expression


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, obj):
        return self._amount == obj._amount and self.currency() == obj.currency()

    @staticmethod
    def doller(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend) -> Expression:
        return Sum(self, addend)


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend
