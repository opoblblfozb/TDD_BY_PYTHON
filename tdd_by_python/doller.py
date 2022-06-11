
class Doller:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Doller(self.amount * multiplier)
    
    def equals(self, obj):
        return self.amount == obj.amount