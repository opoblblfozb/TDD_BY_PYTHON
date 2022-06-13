from unittest import TestCase

from tdd_by_python.money import Money

"""
TODO
$5 + 10CHF = $5
$5 + $5 = $10
"""


class MoneyTest(TestCase):
    def test_doller_multiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def test_equal(self):
        self.assertTrue(Money.doller(5).__eq__(Money.doller(5)))
        self.assertFalse(Money.doller(5).__eq__(Money.doller(6)))
        self.assertFalse(Money.doller(15).__eq__(Money.franc(15)))

    def test_currency(self):
        self.assertEqual(Money.doller(5).currency(), "USD")
        self.assertEqual(Money.franc(5).currency(), "CHF")

    def test_simple_addition(self):
        sum = Money.doller(5).plus(Money.doller(5))
        self.assertEqual(Money.doller(10), sum)
