import unittest
import time
from HW7 import measure_time

def sample_function(n):
    # Затримує виконання на n секунд
    time.sleep(n)
    return n

class TestMeasureTime(unittest.TestCase):
    def test_measure_time(self):
        result, execution_time = measure_time(sample_function, 2)
        self.assertEqual(result, 2)  # Перевірка правильності результату
        self.assertAlmostEqual(execution_time, 2, delta=0.1)  # Перевірка часу виконання з похибкою

if __name__ == '__main__':
    unittest.main()


