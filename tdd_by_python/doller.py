
class Doller:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Doller(self.amount * multiplier)
    
    def __eq__(self, obj):
        return self.amount == obj.amount