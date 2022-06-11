from unittest import TestCase
import pytest

from tdd_by_python.doller import Doller

"""
TODO
$5 * 10CHF = $5
$5 * 2 = $10
amount を privateにする
Dollerの副作用どうする？
Moneyの丸め込みをどうする？
"""

class MoneyTest(TestCase):
    def test_multiplication(self):
        five = Doller(5)
        five.times(2)
        self.assertEqual(10, five.amount)