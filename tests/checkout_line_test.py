
import unittest


def suite():
    suites = unittest.TestSuite()
    suites.addTest(WhenTestingDefaultCards())
    return suites


class WhenTestingDefaultCards(unittest.TestCase):

    def setUp(self):
        pass

    def test_example_1(self):
        self.assertEqual('', 'Finished at: t=7 minutes')

    def test_example_2(self):
        self.assertEqual('', 'Finished at: t=13 minutes')

    def test_example_3(self):
        self.assertEqual('', 'Finished at: t=6 minutes')

    def test_example_4(self):
        self.assertEqual('', 'Finished at: t=9 minutes')

    def test_example_5(self):
        self.assertEqual('', 'Finished at: t=11 minutes')


if __name__ == '__main__':
    unittest.main()