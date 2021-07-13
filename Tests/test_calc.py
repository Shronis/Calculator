import unittest
from Calculator.calculator import Calculator
from csvReader.csvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_Calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_Calculator(self):
        self.assertEqual(self.calculator.result, 4)

    def test_add_method_Calculator(self):
        test_data = CsvReader('Tests/Data/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_method_Calculator(self):
        test_data = CsvReader('Tests/Data/multi.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.mul(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_Calculator(self):
        test_data = CsvReader('Tests/Data/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_Calculator(self):
        test_data = CsvReader('Tests/Data/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_Calculator(self):
        test_data = CsvReader('Tests/Data/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqr(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squareroot_method_Calculator(self):
        test_data = CsvReader('Tests/Data/root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

if __name__ == '__main__':
    unittest.main()
