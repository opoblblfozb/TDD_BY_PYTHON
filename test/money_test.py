from unittest import TestCase
import pytest

from tdd_by_python.doller import Doller
from tdd_by_python.franc import Franc

"""
TODO
$5 + 10CHF = $5
5CHF * 2 = 10CHF
Moneyの丸め込みをどうする？
hashCode()
nullとの等価性比較
他のオブジェクトとの等価性比較
"""

class MoneyTest(TestCase):
    def test_doller_multiplication(self):
        five = Doller(5)
        self.assertEqual(Doller(10), five.times(2))
        self.assertEqual(Doller(15), five.times(3))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))
    
    def test_equal(self):
        self.assertTrue(Doller(5).__eq__(Doller(5)))
        self.assertFalse(Doller(5).__eq__(Doller(6)))

