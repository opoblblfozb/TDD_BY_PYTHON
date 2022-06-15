from abc import ABCMeta, abstractclassmethod


class Expression(metaclass=ABCMeta):
    @abstractclassmethod
    def reduce(self, to: str, bank):
        raise NotImplementedError

    @abstractclassmethod
    def plus(self, addend):
        raise NotImplementedError
