import unittest
from ventas import calcular_total

class TestVentas(unittest.TestCase):
    def test_calcular_total(self):
        self.assertEqual(calcular_total(25, 2), 50)

if __name__ == "__main__":
    unittest.main()