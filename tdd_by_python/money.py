class Money:
    ...

class Doller:
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Doller(self.__amount * multiplier)
    
    def __eq__(self, obj):
        return self.__amount == obj.__amount

class Franc:
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)
    
    def __eq__(self, obj):
        return self.__amount == obj.__amount