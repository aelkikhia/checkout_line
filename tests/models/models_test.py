
import unittest

from collections import deque
from models.models import Registers


def suite():
    suites = unittest.TestSuite()
    suites.addTest(WhenTestingRegister())
    return suites


class WhenTestingGroceryStore(unittest.TestCase):

    def setUp(self):
        self.customers = {'1': [['2', 'A']], '2': [['1', 'A']]}
        self.num_customers = 2
        self.num_registers = 1
        self.registers = None

    # def test_example_1(self):
    #     self.assertEqual('', 'Finished at: t=7 minutes')
    #
    # def test_example_2(self):
    #     self.assertEqual('', 'Finished at: t=13 minutes')
    #
    # def test_example_3(self):
    #     self.assertEqual('', 'Finished at: t=6 minutes')
    #
    # def test_example_4(self):
    #     self.assertEqual('', 'Finished at: t=9 minutes')
    #
    # def test_example_5(self):
    #     self.assertEqual('', 'Finished at: t=11 minutes')


class WhenTestingRegister(unittest.TestCase):

    def setUp(self):
        self.customers = {'1': [('2', 'A')], '2': [('1', 'A')]}
        self.num_customers = 2
        self.num_registers = 1
        self.store = Registers(self.num_registers, self.num_customers,
                               self.customers)
        self.store._init_registers()

    def test_queue_customer(self):
        self.store.time = 8
        self.store._queue_customer([2, 'A'])
        self.assertDictEqual(self.store.registers[0],
                             {'rate': 2, 'pop_time': 12, 'line': deque([2])})

    def test_update_registers_initialized_registered(self):
        store = Registers(1, 1, {})
        store._update_registers()
        self.assertDictEqual(self.store.registers[0],
                             {'rate': 2, 'pop_time': -1, 'line': deque([])})

    def test_update_register_time_to_pop_customer(self):
        self.store.time = 12
        self.store.registers[0] = dict({'rate': 2, 'pop_time': 12,
                                        'line': deque([2])})
        self.store._update_register(self.store.registers[0])
        self.assertDictEqual(self.store.registers[0],
                             {'rate': 2, 'pop_time': -1, 'line': deque([])})

    def test_update_register_not_time_to_pop_customer(self):
        self.store.time = 13
        self.store.registers[0] = dict({'rate': 2, 'pop_time': 12,
                                        'line': deque([2])})
        self.store._update_register(self.store.registers[0])
        self.assertDictEqual(self.store.registers[0],
                             {'rate': 2, 'pop_time': 12, 'line': deque([2])})


if __name__ == '__main__':
    unittest.main()