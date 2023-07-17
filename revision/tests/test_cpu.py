from typing import List
import unittest
from classes import CPU
from tests.data_for_tests.cpu_data import prices, brands, performance, cores, names


class TestCPU(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = CPU()

    def test_get_brand_names_method(self):
        self.assertEqual(self.cpu.get_brand_names(), brands)
        self.assertNotEqual(self.cpu.get_brand_names(), None)
        self.assertIsInstance(self.cpu.get_brand_names(), List)

    def test_get_names_method(self):
        self.assertEqual(self.cpu.get_names(), names)
        self.assertNotEqual(self.cpu.get_names(), None)
        self.assertIsInstance(self.cpu.get_names(), List)

    def test_get_prices_method(self):
        self.assertEqual(self.cpu.get_prices(), prices)
        self.assertNotEqual(self.cpu.get_prices(), None)
        self.assertIsInstance(self.cpu.get_prices(), List)

    def test_core_count_method(self):
        self.assertEqual(self.cpu.get_core_count(), cores)
        self.assertNotEqual(self.cpu.get_core_count(), None)
        self.assertIsInstance(self.cpu.get_core_count(), List)

    def test_perfomance_method(self):
        self.assertEqual(self.cpu.get_perfomance(), performance)
        self.assertNotEqual(self.cpu.get_perfomance(), None)
        self.assertIsInstance(self.cpu.get_perfomance(), List)


if __name__ == "__main__":
    unittest.main()
