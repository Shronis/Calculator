import unittest
from calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_Calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_Calculator(self):
        self.assertEqual(self.calculator.result, 4)

    def test_add_method_Calculator(self):
        self.assertEqual(self.calculator.add(2,2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_Calculator(self):
        self.assertEqual(self.calculator.sub(2,2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiplication_method_Calculator(self):
        self.assertEqual(self.calculator.mul(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_division_method_Calculator(self):
        self.assertEqual(self.calculator.div(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_Calculator(self):
        self.assertEqual(self.calculator.sqr(2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_square_method_Calculator(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.result, 2)

if __name__ == '__main__':
    unittest.main()