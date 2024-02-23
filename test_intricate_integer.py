import unittest
from IntricateInteger import IntricateInteger
  # Adjust this import as necessary

class TestIntricateInteger(unittest.TestCase):
    def test_initialization(self):
        """Test initialization and attributes of IntricateInteger objects."""
        obj = IntricateInteger(3, 7, 2)
        self.assertEqual(obj.object, 3)
        self.assertEqual(obj.mod, 7)
        self.assertEqual(obj.mul, 2)

    def test_str(self):
        """Test the string representation of IntricateInteger objects."""
        obj = IntricateInteger(3, 7, 2)
        self.assertEqual(str(obj), "<3 mod 7 | 2>")

    def test_multiplication(self):
        """Test multiplication operation between two IntricateInteger objects."""
        a = IntricateInteger(3, 5, 4)
        b = IntricateInteger(2, 5, 4)
        result = a * b
        # Calculate the expected result according to the custom operation
        expected_result = (3 + 2 + 4 * (6)) % 5  # Using LCM of 3 and 2 as 6 for this example
        self.assertEqual(result.object, expected_result)

    def test_incompatible_multiplication(self):
        """Test multiplication operation with incompatible IntricateInteger objects."""
        a = IntricateInteger(3, 5, 4)
        b = IntricateInteger(2, 6, 4)  # Different modulus
        with self.assertRaises(ArithmeticError):
            _ = a * b

    def test_invalid_initialization(self):
        """Test initialization with invalid parameters."""
        with self.assertRaises(ValueError):
            _ = IntricateInteger(-1, 5, 4)  # Invalid value
        with self.assertRaises(ValueError):
            _ = IntricateInteger(3, -5, 4)  # Invalid modulus
        with self.assertRaises(ValueError):
            _ = IntricateInteger(3, 5, -1)  # Invalid multiplier

if __name__ == '__main__':
    unittest.main()
