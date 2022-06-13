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

    def reduce(self, to: str) -> Money:
        return Money(self._amount, to)


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Money:
        amount: int = self.augend._amount + self.addend._amount
        return Money(amount, to)


assert Money.reduce.__annotations__ == {"to": "str", "return": "Money"}
