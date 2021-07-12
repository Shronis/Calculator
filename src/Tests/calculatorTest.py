import unittest
from Calculator.calculator import Calculator
from csvReader import CsvReader


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
        test_data = CsvReader('/src/multi.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.mul(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_Calculator(self):
        test_data = CsvReader('/src/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_Calculator(self):
        test_data = CsvReader('/src/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_Calculator(self):
        test_data = CsvReader('/src/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqr(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squareroot_method_Calculator(self):
        test_data = CsvReader('/src/root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

if __name__ == '__main__':
    unittest.main()