# Create class Worker with fields name and salary.
# If salary negative raise ValueError
# Create a method get_tax_value() that calculate tax from salary .
# Tax must be calculate like "progressive tax" with next step:
# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker.
# Don`t use assertRaises in tests.

import unittest
import sys


class Worker:
    salary = 0.0

    def __init__(self, *args):
        if len(args) == 2:
            if args[1] < 0:
                raise ValueError
            self.name = args[0]
            self.salary = args[1]

    def get_tax_value(self):
        percents = [0.0, 0.1, 0.15, 0.21, 0.3, 0.4, 0.47]
        threshold = [0, 1000, 3000, 5000, 10000, 20000, 50000, sys.maxsize]
        taxes = 0
        income = self.salary
        for i in range(len(percents)):
            if i == (len(threshold) - 1) or income < threshold[i + 1]:
                taxes += (income - threshold[i]) * percents[i]
                break
            else:
                taxes += (threshold[i + 1] - threshold[i]) * percents[i]
        return taxes


class WorkerTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_tax(self):
        self.assertEqual(Worker('Andri', 999).get_tax_value(), 0.0)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(Worker('Nat', -2), ValueError)

    def tearDown(self):
        pass
