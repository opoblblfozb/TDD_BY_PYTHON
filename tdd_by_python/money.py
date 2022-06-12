from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, obj):
        return (
            self._amount == obj._amount
            and self.__class__.__name__ == obj.__class__.__name__
        )

    @staticmethod
    def doller(amount):
        return Doller(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

    @abstractmethod
    def times(self, multiplier):
        raise NotImplementedError


class Doller(Money):
    def times(self, multiplier):
        return Doller(self._amount * multiplier)

    @staticmethod
    def currency():
        return "USD"


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    @staticmethod
    def currency():
        return "CHF"
