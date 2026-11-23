import unittest

from main import generate_probable_prime, is_probable_prime


class PrimalityTests(unittest.TestCase):
    def test_known_values(self):
        for value in (2, 3, 5, 11, 37, 101, 104729):
            self.assertTrue(is_probable_prime(value), value)
        for value in (-3, 0, 1, 4, 9, 25, 561, 1105):
            self.assertFalse(is_probable_prime(value), value)

    def test_exact_bit_length(self):
        result = generate_probable_prime(20)
        self.assertEqual(result.bit_length(), 20)
        self.assertEqual(result % 2, 1)
        self.assertTrue(is_probable_prime(result))

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            generate_probable_prime(1)
        with self.assertRaises(ValueError):
            is_probable_prime(17, rounds=0)


if __name__ == "__main__":
    unittest.main()
