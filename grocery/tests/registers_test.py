
import unittest
from collections import deque

from grocery.registers import Registers


def suite():
    suites = unittest.TestSuite()
    suites.addTest(WhenTestingRegister())
    return suites


class WhenTestingRegister(unittest.TestCase):

    def setUp(self):
        self.store = Registers()
        self.customers = {'1': [['2', 'A']], '2': [['1', 'A']]}
        self.num_customers = 2
        self.num_registers = 1
        self.store._init_registers()

    def test_queue_customer(self):
        self.store.time = 8
        self.num_customers = 1
        self.num_registers = 1
        self.store._queue_customer([2, 'A'])
        self.assertDictEqual(self.store.registers[0],
                             {'rate': 2, 'pop_time': 12, 'line': deque([2])})

    def test_update_registers_initialized_registered(self):
        store = Registers()
        store.num_registers = 1
        store._init_registers()
        store._update_registers()
        self.assertDictEqual(store.registers[0],
                             {'rate': 2, 'pop_time': -1, 'line': deque([])})

    def test_update_register_time_to_pop_customer(self):
        self.store.time = 12
        self.store.registers[0] = dict({'rate': 2, 'pop_time': 12,
                                        'line': deque([2])})
        self.store._update_register(self.store.registers[0])
        self.assertDictEqual(self.store.registers[0],
                             {'rate': 2, 'pop_time': -1, 'line': deque([])})

    def test_update_register_not_time_to_pop_customer(self):
        self.store.time = 11
        self.store.registers[0] = dict({'rate': 2, 'pop_time': 12,
                                        'line': deque([2])})
        self.store._update_register(self.store.registers[0])
        self.assertDictEqual(self.store.registers[0],
                             {'rate': 2, 'pop_time': 12, 'line': deque([2])})

    def test_find_shortest_line_tie_goes_to_empty(self):
        store = Registers()
        store.time = 0
        store.num_customers = 5
        store.num_registers = 2
        store._init_registers()
        store._queue_customer([2, 'A'])
        length, shortest_line = store._find_shortest_line()
        self.assertEqual(shortest_line, 1)

    def test_find_shortest_line_empty_line(self):
        store = Registers()
        store.time = 0
        store.num_customers = 5
        store.num_registers = 2
        store._init_registers()
        store._queue_customer([2, 'A'])
        store._queue_customer([2, 'A'])
        length, shortest_line = store._find_shortest_line()
        self.assertEqual(shortest_line, 0)

    def test_find_shortest_line(self):
        store = Registers()
        store.time = 0
        store.num_customers = 5
        store.num_registers = 2
        store._init_registers()
        store._queue_customer([2, 'A'])
        store._queue_customer([2, 'A'])
        store._queue_customer([2, 'A'])
        length, shortest_line = store._find_shortest_line()
        self.assertEqual(shortest_line, 1)

    def test_find_last_customer_with_least_items(self):
        store = Registers()
        store.time = 0
        store.num_customers = 5
        store.num_registers = 2
        store._init_registers()
        store._queue_customer([2, 'A'])
        store._queue_customer([2, 'A'])
        store._queue_customer([3, 'A'])
        store._queue_customer([6, 'A'])
        length, shortest_line = store._find_shortest_line()
        self.assertEqual(shortest_line, 0)

if __name__ == '__main__':
    unittest.main()
