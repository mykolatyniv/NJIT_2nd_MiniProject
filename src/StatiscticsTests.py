import unittest
from Statistics import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.Statistics = Calculator()

    def test_instantiate_Statistics(self):
        self.assertIsInstance(self.Statistics, Calculator)

    def test_population_mean(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.mean(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result']))

    def test_median(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.med(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result']))

    def test_mode(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.mod(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result']))

    def test_population_standard_deviation(self):
        test_data = CsvReader('/src/test1.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.population(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_variance_of_population_proportion(self):
        test_data = CsvReader('/src/test2.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_variance_of_population_proportion(self):
        test_data = CsvReader('/src/test3.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_z_score(self):
        test_data = CsvReader('/src/test4.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.score(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_standardized_score(self):
        test_data = CsvReader('/src/test5.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.standardized(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_population_correlation_coefficient(self):
        test_data = CsvReader('/src/test6.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.population(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_confidence_interval(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.confidence(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_population_variance(self):
        test_data = CsvReader('/src/test7.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_p_value(self):
        test_data = CsvReader('/src/test8.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.value(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_proportion(self):
        test_data = CsvReader('/src/test9.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.prop(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_sample_mean(self):
        test_data = CsvReader('/src/test10.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.smean(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_sample_standard_deviation(self):
        test_data = CsvReader('/src/test11.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.sample(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_variance_of_sample_proportion(self):
        test_data = CsvReader('/src/test12.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
