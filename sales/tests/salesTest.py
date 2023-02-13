import unittest
from sales.main import InvoiceLine

from sales.main.Parser import parseLine


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_lineParser(self):
        line = parseLine('1 book at 10.00')

        self.assertEqual(1, line.qty())


if __name__ == '__main__':
    unittest.main()
