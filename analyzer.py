"""
Student Performance & Academic Analytics Engine
Statistical analysis module for student grade distributions and cohort metrics.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
import math


@dataclass
class CohortStats:
    total_students: int
    highest_mark: float
    lowest_mark: float
    mean: float
    median: float
    std_dev: float
    pass_count: int
    fail_count: int
    pass_percentage: float
    grade_distribution: Dict[str, int]
    percentiles: Dict[str, float]
    outliers: List[float]


class AcademicPerformanceAnalyzer:
    """
    Production-grade statistical analyzer for student exam marks and grade distributions.
    """

    DEFAULT_GRADE_BOUNDS = {
        "A+ (90-100)": (90, 100),
        "A  (80-89)":  (80, 89.99),
        "B  (70-79)":  (70, 79.99),
        "C  (50-69)":  (50, 69.99),
        "D  (35-49)":  (35, 49.99),
        "F  (<35)":    (0, 34.99),
    }

    def __init__(self, pass_mark: float = 35.0):
        self.pass_mark = pass_mark

    def analyze(self, marks: List[float]) -> CohortStats:
        """
        Compute full statistical profile of a mark distribution.
        """
        if not marks:
            raise ValueError("Marks list cannot be empty.")

        n = len(marks)
        sorted_marks = sorted(marks)
        highest = sorted_marks[-1]
        lowest = sorted_marks[0]
        total_sum = sum(sorted_marks)
        mean = total_sum / n

        # Median calculation
        if n % 2 == 1:
            median = sorted_marks[n // 2]
        else:
            median = (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2.0

        # Standard Deviation
        variance = sum((x - mean) ** 2 for x in sorted_marks) / (n if n > 1 else 1)
        std_dev = math.sqrt(variance)

        # Pass / Fail
        pass_students = [m for m in sorted_marks if m >= self.pass_mark]
        fail_students = [m for m in sorted_marks if m < self.pass_mark]
        pass_pct = (len(pass_students) / n) * 100.0

        # Grade distribution
        grades: Dict[str, int] = {k: 0 for k in self.DEFAULT_GRADE_BOUNDS}
        for m in sorted_marks:
            assigned = False
            for label, (low, high) in self.DEFAULT_GRADE_BOUNDS.items():
                if low <= m <= high or (high == 100 and m >= 100):
                    grades[label] += 1
                    assigned = True
                    break
            if not assigned and m < 35:
                grades["F  (<35)"] += 1

        # Percentiles
        def get_percentile(p: float) -> float:
            k = (n - 1) * (p / 100.0)
            f = math.floor(k)
            c = math.ceil(k)
            if f == c:
                return sorted_marks[int(k)]
            return sorted_marks[f] * (c - k) + sorted_marks[c] * (k - f)

        percentiles = {
            "25th (Q1)": round(get_percentile(25), 2),
            "50th (Q2)": round(median, 2),
            "75th (Q3)": round(get_percentile(75), 2),
            "90th": round(get_percentile(90), 2),
        }

        # Outliers via IQR
        q1 = percentiles["25th (Q1)"]
        q3 = percentiles["75th (Q3)"]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = [m for m in sorted_marks if m < lower_bound or m > upper_bound]

        return CohortStats(
            total_students=n,
            highest_mark=highest,
            lowest_mark=lowest,
            mean=round(mean, 2),
            median=round(median, 2),
            std_dev=round(std_dev, 2),
            pass_count=len(pass_students),
            fail_count=len(fail_students),
            pass_percentage=round(pass_pct, 2),
            grade_distribution=grades,
            percentiles=percentiles,
            outliers=outliers,
        )

    def print_report(self, stats: CohortStats) -> None:
        """Render a formatted terminal report."""
        print("=" * 60)
        print("           ACADEMIC PERFORMANCE COHORT REPORT")
        print("=" * 60)
        print(f"Total Cohort Size    : {stats.total_students}")
        print(f"Highest Score        : {stats.highest_mark}")
        print(f"Lowest Score         : {stats.lowest_mark}")
        print(f"Cohort Mean (Avg)    : {stats.mean}")
        print(f"Cohort Median        : {stats.median}")
        print(f"Standard Deviation   : {stats.std_dev}")
        print(f"Pass Rate            : {stats.pass_percentage}% ({stats.pass_count} passed, {stats.fail_count} failed)")
        print("-" * 60)
        print("Percentile Benchmarks:")
        for k, v in stats.percentiles.items():
            print(f"  • {k:<12}: {v}")
        print("-" * 60)
        print("Grade Distribution:")
        for grade, count in stats.grade_distribution.items():
            bar = "█" * count
            print(f"  • {grade:<16}: {count:>2} | {bar}")
        print("=" * 60)


if __name__ == "__main__":
    analyzer = AcademicPerformanceAnalyzer(pass_mark=35.0)
    print("Academic Performance Analyzer CLI")
    try:
        raw_input = input("Enter student marks separated by space: ").strip()
        if not raw_input:
            print("Using sample cohort dataset...")
            sample_marks = [78, 85, 92, 45, 60, 32, 95, 88, 73, 54, 28, 99, 81]
            stats = analyzer.analyze(sample_marks)
        else:
            marks = [float(x) for x in raw_input.split()]
            stats = analyzer.analyze(marks)
        analyzer.print_report(stats)
    except Exception as e:
        print(f"Error during analysis: {e}")
