import unittest
import vending_machine as v

vending = v.vendingMachine(cola_stock=1, crisp_stock=2, choc_stock=3)

class vending_machine_test(unittest.TestCase):
    def setUp(self):
        print('Testing vending machine functionality!')

    def tearDown(self):
        print('Well that was fun')

    def test_coin_input(self):
        vending.balance = 0
        self.assertEqual(vending.take_money(0.05), 0.05)

    def test_buy_cola(self):
        vending.balance = 1
        self.assertEqual(vending.purchase_cola(1), (0,0))
        vending.balance = 1.25
        self.assertEqual(vending.purchase_cola(1), (0, 0.25))

        vending.cola_stock = 1
        vending.balance = 2
        self.assertEqual(vending.purchase_cola(2), (1, 2))

        vending.balance = 0.5
        self.assertEqual(vending.purchase_cola(1), (1, 0.5))

    def test_buy_choc(self):
        vending.balance = 0.65
        self.assertNotEqual(vending.purchase_choc(2), (1,0))

        vending.balance = 0.65
        vending.choc_stock = 0
        self.assertEqual(vending.purchase_choc(1), (0,0.65))

    def test_buy_crisp(self):
        vending.balance = 0.5
        self.assertEqual(vending.purchase_crisp(1), (1, 0))

        vending.balance = 5
        self.assertEqual(vending.purchase_crisp(5), (2, 5))

        vending.balance = 0.25
        self.assertEqual(vending.purchase_crisp(1), (2, 0.25))


if __name__ == '__main__':
    unittest.main()
