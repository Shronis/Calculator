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

if __name__ == '__main__':
    unittest.main()