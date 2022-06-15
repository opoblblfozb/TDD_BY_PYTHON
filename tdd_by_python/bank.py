from __future__ import annotations

from tdd_by_python.expression import Expression

from .money import Money, Sum


class Bank:
    def reduce(self, source, to: str) -> Money:
        return source.reduce(to, self)

    def add_rate(self, _from: str, _to: str, rate: int):
        ...

    def get_rate(self, _from: str, _to: str):
        return 2 if _from == "CHF" and _to == "USD" else 1
