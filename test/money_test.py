from unittest import TestCase

from tdd_by_python.money import Doller, Franc, Money

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
DollerとFrancの比較
"""


class MoneyTest(TestCase):
    def test_doller_multiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def test_equal(self):
        self.assertTrue(Money.doller(5).__eq__(Money.doller(5)))
        self.assertFalse(Money.doller(5).__eq__(Money.doller(6)))
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(6)))
        self.assertFalse(Money.doller(15).__eq__(Franc(15)))
