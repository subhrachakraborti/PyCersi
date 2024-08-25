import unittest
import pycersi as p  # Import your package

class TestPyCersi(unittest.TestCase):

    def test_digirev(self):
        # Test the digirev function
        self.assertEqual(p.digirev(1234), 4321)
        self.assertEqual(p.digirev(0), 0)
        self.assertEqual(p.digirev(9876), 6789)

    def test_digisum(self):
        # Test the digisum function
        self.assertEqual(p.digisum(1234), 10)
        self.assertEqual(p.digisum(0), 0)
        self.assertEqual(p.digisum(9999), 36)

    def test_digipro(self):
        # Test the digipro function
        self.assertEqual(p.digipro(1234), 24)
        self.assertEqual(p.digipro(0), 0)
        self.assertEqual(p.digipro(1111), 1)

    def test_isabundant(self):
        # Test the isabundant function
        self.assertTrue(p.isabundant(12))  # 12 is an abundant number
        self.assertFalse(p.isabundant(5))  # 5 is not an abundant number

    def test_ishappy(self):
        # Test the ishappy function
        self.assertTrue(p.ishappy(19))  # 19 is a happy number
        self.assertFalse(p.ishappy(20))  # 20 is not a happy number

    def test_isperfect(self):
        # Test the isperfect function
        self.assertTrue(p.isperfect(6))  # 6 is a perfect number
        self.assertFalse(p.isperfect(10))  # 10 is not a perfect number

if __name__ == '__main__':
    unittest.main()
