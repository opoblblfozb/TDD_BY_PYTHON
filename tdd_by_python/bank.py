from tdd_by_python.expression import Expression

from .expression import Expression
from .money import Money, Sum


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce((to))
