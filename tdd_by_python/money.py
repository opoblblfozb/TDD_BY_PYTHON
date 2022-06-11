class Money:
    def __init__(self, amount):
        self._amount = amount
    def __eq__(self, obj):
        return self._amount == obj._amount

class Doller(Money):
    def times(self, multiplier):
        return Doller(self._amount * multiplier)
    
class Franc:
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)
    
    def __eq__(self, obj):
        return self.__amount == obj.__amount