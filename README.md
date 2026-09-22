# 📊 Academic Performance & Cohort Analytics Engine

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge&logo=pytest)](test_analyzer.py)
[![CodeRabbit](https://img.shields.io/badge/CodeRabbit-Reviewed-ff69b4?style=for-the-badge&logo=coderabbit)](https://coderabbit.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> A modular Python library and CLI tool for statistical evaluation of academic exam scores, grade distributions, IQR outlier detection, and cohort percentiles.

---

## 📌 Features

* **Descriptive Statistics:** Computes Cohort Mean, Median, Variance, Standard Deviation, Max, and Min.
* **Percentile Benchmarking:** Computes exact 25th (Q1), 50th (Q2), 75th (Q3), and 90th percentile thresholds.
* **IQR Outlier Detection:** Automatically isolates extreme performance deviations using Interquartile Range fences.
* **Grade Categorization:** Evaluates cohort distribution into standard GPA/Grade bands (`A+`, `A`, `B`, `C`, `D`, `F`) with ASCII distribution visualizations.
* **Unit Tested:** 100% test coverage using Python's built-in `unittest` suite.

---

## 🚀 Quickstart

### Run the CLI
```bash
python3 analyzer.py
```

### Run Unit Tests
```bash
python3 -m unittest test_analyzer.py
```

### Usage as a Python Library
```python
from analyzer import AcademicPerformanceAnalyzer

analyzer = AcademicPerformanceAnalyzer(pass_mark=35.0)
scores = [78, 85, 92, 45, 60, 32, 95, 88, 73, 54, 28, 99, 81]

stats = analyzer.analyze(scores)
analyzer.print_report(stats)
```

---

## ⚡ Engineering & Quality Standards
* **CodeRabbit AI:** Configured with `.coderabbit.yaml` for automated PR code reviews.
* **GSD Engineering Protocol:** Strict type annotations, error boundary checks, and reproducible unit tests.