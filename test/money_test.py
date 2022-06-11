from unittest import TestCase
import pytest

from tdd_by_python.money import Doller, Franc

"""
TODO
$5 + 10CHF = $5
5CHF * 2 = 10CHF
Moneyの丸め込みをどうする？
hashCode()
nullとの等価性比較
他のオブジェクトとの等価性比較
DollerとFrancの重複
equalsの一般化
timesの一般化
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
    
    def test_doller_equal(self):
        self.assertTrue(Doller(5).__eq__(Doller(5)))
        self.assertFalse(Doller(5).__eq__(Doller(6)))

    def test_franc_equal(self):
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(6)))