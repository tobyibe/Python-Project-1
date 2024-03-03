import unittest
from IntricateInteger import IntricateInteger
from IntricateIntegers import IntricateIntegers
from CommutativeIntricateMultiplication import has_commutative_intricate_multiplication
from IntricatePeculiarProperty import has_intricate_peculiar_property
from AssociativeIntricateMultiplication import has_associative_intricate_multiplication

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

    def test_peculiar_property(self):
        """Test that x ⊗ x = x holds for alpha = n - 1."""
        for n in range(1, 51):  # Testing n from 1 to 50
            alpha = n - 1  # Set alpha to n - 1
            all_hold = True  # Assume property holds for all x initially
            for x in range(n):
                ii = IntricateInteger(x, n, alpha)
                result = ii * ii
                if result.object != x:  # Check if the peculiar property does not hold
                    all_hold = False
                    break  # No need to check further if any x fails
            self.assertTrue(all_hold, f"Peculiar property does not hold for n={n}, alpha={alpha}")

    def test_commutativity(self):
        """Test if the multiplication operation is commutative for various n and alpha."""
        for n in range(1, 51):  # Test a range of n values
            for alpha in range(n):  # Test all alpha values within each n
                with self.subTest(n=n, alpha=alpha):
                    self.assertTrue(has_commutative_intricate_multiplication(n, alpha),
                                    f"Multiplication not commutative for n={n}, alpha={alpha}")

    def test_associativity(self):
        """Test if the multiplication operation is associative for specific n and alpha values that follow a pattern discovered in my results."""
        for n in range(1, 21):  # Test a range of n values as requested in specification
            for alpha in range(n):  # Test all alpha values within each n
                with self.subTest(n=n, alpha=alpha):
                    if (n%2==0 and alpha==n/2) or alpha==0: #This if statement and the results verify my conjucture written within the AssociativeIntricateMultiplication file
                            self.assertTrue(has_associative_intricate_multiplication(n, alpha),
                                    f"Multiplication not associative for n={n}, alpha={alpha}")
    
    def test_iteration(self):
        """Test the iteration of IntricateIntegers objects."""
        counter=0 # Use a counter to keep count of value in Zn set
        for x in IntricateIntegers(3,2): # Testing for loop interation over an instance of IntricateIntegers
           self.assertEqual(x, f"<{counter} mod 3 | 2>")
           counter+=1


if __name__ == '__main__':
    unittest.main()
