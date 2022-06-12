class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, obj):
        return self._amount == obj._amount and self.currency() == obj.currency()

    @staticmethod
    def doller(amount):
        return Doller(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    def times(self, multiplier):
        raise NotImplementedError

    def currency(self):
        return self._currency


class Doller(Money):
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)


class Franc(Money):
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)
