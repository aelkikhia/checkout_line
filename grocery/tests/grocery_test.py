import unittest

from grocery.registers import Registers


def suite():
    suites = unittest.TestSuite()
    suites.addTest(WhenTestingGroceryExample1())
    return suites


class WhenTestingGroceryExample1(unittest.TestCase):

    def test_example_1(self):
        store = Registers()
        store.customers = dict({1: [[2, 'A']], 2: [[1, 'A']]})
        store.num_customers = 2
        store.num_registers = 1
        store.process_customers()
        self.assertEqual(store.get_time(), 7)

    def test_example_2(self):
        store = Registers()
        store.customers = dict({8: [[2, 'A']], 1: [[5, 'A']], 2: [[1, 'B']],
                                3: [[5, 'A']], 5: [[3, 'B']]})
        store.num_customers = 5
        store.num_registers = 2
        store.process_customers()
        self.assertEqual(store.get_time(), 13)

    def test_example_3(self):
        store = Registers()
        store.customers = dict({1: [[2, 'A'], [2, 'A']], 2: [[1, 'A']],
                                3: [[2, 'A']]})
        store.num_customers = 4
        store.num_registers = 2
        store.process_customers()
        self.assertEqual(store.get_time(), 6)

    def test_example_4(self):
        store = Registers()
        store.customers = dict({1: [[2, 'A'], [3, 'A']],
                                2: [[1, 'A'], [1, 'A']]})
        store.num_customers = 4
        store.num_registers = 2
        store.process_customers()
        self.assertEqual(store.get_time(), 9)

    def test_example_5(self):
        store = Registers()
        store.customers = dict({1: [[3, 'A'], [5, 'A']], 3: [[1, 'A']],
                                4: [[1, 'A'], [1, 'B']]})
        store.num_customers = 5
        store.num_registers = 2
        store.process_customers()
        self.assertEqual(store.get_time(), 11)

if __name__ == '__main__':
    unittest.main()
