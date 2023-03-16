import unittest
from io import StringIO
from unittest.mock import patch
from atm import Bank, Customer


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_create_customer(self):
        self.bank.login("Alice")
        self.assertIn("Alice", self.bank.customers)

    def test_deposit(self):
        self.bank.login("Alice")
        self.bank.deposit(100)
        self.assertEqual(self.bank.current_customer.balance, 100)

    def test_withdraw(self):
        self.bank.login("Alice")
        self.bank.deposit(100)
        self.bank.withdraw(50)
        self.assertEqual(self.bank.current_customer.balance, 50)

    def test_transfer(self):
        self.bank.login("Alice")
        self.bank.deposit(100)
        self.bank.login("Bob")
        self.bank.transfer("Bob", 50)
        self.assertEqual(self.bank.current_customer.balance, 50)
        self.assertEqual(self.bank.customers["Bob"].balance, 50)

    def test_logout(self):
        self.bank.login("Alice")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.bank.logout()
            self.assertEqual(fake_out.getvalue().strip(), "Goodbye, Alice!")
        self.assertIsNone(self.bank.current_customer)


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")

    def test_deposit(self):
        self.customer.deposit(100)
        self.assertEqual(self.customer.balance, 100)

    def test_withdraw(self):
        self.customer.deposit(100)
        self.customer.withdraw(50)
        self.assertEqual(self.customer.balance, 50)

    def test_transfer(self):
        self.target = Customer("Bob")
        self.customer.deposit(100)
        self.customer.transfer("Bob", 50)
        self.assertEqual(self.customer.balance, 50)
        self.assertEqual(self.target.balance, 50)
        self.assertEqual(self.target.owed["Alice"], 50)

    def test_show_balance(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.customer.show_balance()
            self.assertEqual(fake_out.getvalue().strip(), "Your balance is $0")


if __name__ == '__main__':
    unittest.main()
