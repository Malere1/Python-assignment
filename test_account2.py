import unittest
class TestPrimeNumber(unittest.TestCase):
def test_prime_numbers(self):

    def test_prime_numbers(self)
    self.assertTrue(is_prime(2))
    self.assertTrue(is_prime(3))
    self.assertTrue(is_prime(13))

    def test_non_prime_numbers(self):
    self.assertFalse(is_prime(4))
    self.assertFalse(is_prime(10))
    self.assertFalse(is_prime(25))

    def test_edge_cases(self):
    self.assertFalse(is_prime(1))
    self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-5))

