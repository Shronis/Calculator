import unittest
from calculator import Calculator
from csvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_Calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_Calculator(self):
        self.assertEqual(self.calculator.result, 4)

    def test_add_method_Calculator(self):
        test_data = CsvReader('/src/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_method_Calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.mul(2,2),4)
        self.assertEqual(calculator.result,4)

    def test_subtract_method_Calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sub(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_division_method_Calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.div(2, 2), 1)
        self.assertEqual(calculator.result, 1)

    def test_square_method_Calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqr(2), 4)
        self.assertEqual(calculator.result, 4)

    def test_squareroot_method_Calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(9), 3)
        self.assertEqual(calculator.result, 3)

if __name__ == '__main__':
    unittest.main()