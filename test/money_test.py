from unittest import TestCase
import pytest

from tdd_by_python.doller import Doller

"""
TODO
$5 * 10CHF = $5
amount を privateにする
Moneyの丸め込みをどうする？
"""

class MoneyTest(TestCase):
    def test_multiplication(self):
        five = Doller(5)
        product: Doller = five.times(2)
        self.assertEqual(10, product.amount)
        product: Doller = five.times(3)
        self.assertEqual(15, product.amount)