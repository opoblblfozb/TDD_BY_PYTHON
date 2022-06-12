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
        five = Money.franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    def test_equal(self):
        self.assertTrue(Money.doller(5).__eq__(Money.doller(5)))
        self.assertFalse(Money.doller(5).__eq__(Money.doller(6)))
        self.assertTrue(Money.franc(5).__eq__(Money.franc(5)))
        self.assertFalse(Money.franc(5).__eq__(Money.franc(6)))
        self.assertFalse(Money.doller(15).__eq__(Money.franc(15)))

    def test_currency(self):
        self.assertEqual(Money.doller(5).currency(), "USD")
        self.assertEqual(Money.franc(5).currency(), "CHF")

    def test_diffrentclass_equality(self):
        self.assertEqual(Money(5, "CHF"), Franc(5, "CHF"))
