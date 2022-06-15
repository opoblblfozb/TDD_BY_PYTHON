from unittest import TestCase

from tdd_by_python.bank import Bank
from tdd_by_python.expression import Expression
from tdd_by_python.money import Money, Sum

"""
TODO
$5 + 10CHF = $5
$5 + $5 = $10
bank.reduce(Money)
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
        five: Money = Money.doller(5)
        sum: Expression = five.plus(five)
        bank: Bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(10), result)

    def test_plus_return_sum(self):
        five: Money = Money.doller(5)
        result: Expression = five.plus(Money.doller(5))
        self.assertEqual(five, result.augend)
        self.assertEqual(five, result.addend)

    def test_reduce_sum(self):
        sum: Expression = Sum(Money.doller(3), Money.doller(4))
        bank: Bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(7), result)

    def test_reduce_money(self):
        bank: Bank = Bank()
        result = bank.reduce(Money.doller(6), "USD")
        self.assertEqual(Money.doller(6), result)

    def test_reduce_money_different_currency(self):
        bank: Bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result: Money = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.doller(1), result)

    def test_mixed_addition(self):
        bank: Bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        five_bucks = Money.doller(5)
        ten_franc = Money.franc(10)
        result = bank.reduce(five_bucks.plus(ten_franc), "USD")
        self.assertEqual(Money.doller(10), result)
