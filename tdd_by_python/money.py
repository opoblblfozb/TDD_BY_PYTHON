from __future__ import annotations

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

    def reduce(self, to: str, bank) -> Money:
        rate = bank.get_rate(self.currency(), to)
        return Money(self._amount / rate, to)


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str, bank) -> Money:
        amount: int = (
            self.augend.reduce(to, bank)._amount + self.addend.reduce(to, bank)._amount
        )
        return Money(amount, to)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


assert Money.reduce.__annotations__ == {"to": "str", "return": "Money"}
