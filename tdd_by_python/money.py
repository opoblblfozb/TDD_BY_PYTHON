class Money:
    def __init__(self, amount):
        self._amount = amount
    def __eq__(self, obj):
        return self._amount == obj._amount

class Doller(Money):
    def times(self, multiplier):
        return Doller(self._amount * multiplier)
    
class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)