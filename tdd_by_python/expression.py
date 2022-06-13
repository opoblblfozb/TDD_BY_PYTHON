from abc import ABCMeta, abstractclassmethod


class Expression(metaclass=ABCMeta):
    @abstractclassmethod
    def reduce(self, to: str):
        raise NotImplementedError
