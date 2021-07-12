import unittest
from csvReader import CsvReader
from StatCalc.Stat_Calc import Statistics

from pprint import pprint

class MyTestCase(unittest.TestCase):

    test_data = CsvReader('Tests/Data/Test_Data.csv').data
    answer = CsvReader('Tests/Data/Stat_Answers.csv').data
    column1 = [int(row['value1']) for row in test_data]

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        for row in self.answer:
            self.assertEqual(self.statistics.mean(self.column1), float(row['mean']))
            self.assertEqual(self.statistics.result, float(row['mean']))

    def test_median_statistics(self):
        for row in self.answer:
            self.assertEqual(self.statistics.median(self.column1), float(row['median']))
            self.assertEqual(self.statistics.result, float(row['median']))

    def test_mode_statistics(self):
        for row in self.answer:
            self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.statistics.result, float(row['mode']))

    def test_variance_statistics(self):
        for row in self.answer:
            self.assertEqual(self.statistics.variance(self.column1), float(row['variance']))
            self.assertEqual(self.statistics.result, float(row['variance']))

    def test_standard_deviation_statistics(self):
        for row in self.answer:
            self.assertEqual(self.statistics.stddev(self.column1), float(row['stddev']))
            self.assertEqual(self.statistics.result, float(row['stddev']))

if __name__ == '__main__':
    unittest.main()
