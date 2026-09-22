import unittest
from analyzer import AcademicPerformanceAnalyzer

class TestAcademicPerformanceAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = AcademicPerformanceAnalyzer(pass_mark=35.0)

    def test_basic_metrics(self):
        marks = [50, 60, 70, 80, 90]
        stats = self.analyzer.analyze(marks)
        self.assertEqual(stats.total_students, 5)
        self.assertEqual(stats.highest_mark, 90)
        self.assertEqual(stats.lowest_mark, 50)
        self.assertEqual(stats.mean, 70.0)
        self.assertEqual(stats.median, 70.0)
        self.assertEqual(stats.pass_count, 5)
        self.assertEqual(stats.fail_count, 0)
        self.assertEqual(stats.pass_percentage, 100.0)

    def test_pass_fail_split(self):
        marks = [20, 30, 40, 50]
        stats = self.analyzer.analyze(marks)
        self.assertEqual(stats.pass_count, 2)
        self.assertEqual(stats.fail_count, 2)
        self.assertEqual(stats.pass_percentage, 50.0)

    def test_empty_marks_exception(self):
        with self.assertRaises(ValueError):
            self.analyzer.analyze([])

if __name__ == "__main__":
    unittest.main()
