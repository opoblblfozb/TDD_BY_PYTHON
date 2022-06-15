from __future__ import annotations

from tdd_by_python.expression import Expression

from .money import Money, Sum


class Bank:
    def __init__(self):
        self.rate_maps = {}

    def reduce(self, source, to: str) -> Money:
        return source.reduce(to, self)

    def add_rate(self, _from: str, _to: str, rate: int):
        self.rate_maps[(_from, _to)] = rate

    def get_rate(self, _from: str, _to: str):
        if _from == _to:
            return 1
        return self.rate_maps[(_from, _to)]
