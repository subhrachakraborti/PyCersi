import unittest
import pycersi as p
import io
import sys
import math
import json

class TestPyCersi(unittest.TestCase):

    def test_fiboupto(self):
        self.assertEqual(p.fiboupto(10), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(p.fiboupto(0), [0])
        self.assertEqual(p.fiboupto(1), [0, 1, 1])

    def test_fiborange(self):
        self.assertEqual(p.fiborange(5), [0, 1, 1, 2, 3])
        self.assertEqual(p.fiborange(1), [0])
        self.assertEqual(p.fiborange(0), [])

    def test_gcd(self):
        self.assertEqual(p.gcd([12, 18, 24]), 6)
        self.assertEqual(p.gcd([15, 25, 35]), 5)
        self.assertEqual(p.gcd([7, 11]), 1)

    def test_lcm(self):
        self.assertEqual(p.lcm([2, 3, 4]), 12)
        self.assertEqual(p.lcm([5, 10, 15]), 30)
        self.assertEqual(p.lcm([7]), 7)

    def test_digirev(self):
        self.assertEqual(p.digirev(1234), 4321)
        self.assertEqual(p.digirev(1000), 1)
        self.assertEqual(p.digirev(0), 0)

    def test_digipro(self):
        self.assertEqual(p.digipro(1234), 24)
        self.assertEqual(p.digipro(1000), 0)
        self.assertEqual(p.digipro(0), 0)

    def test_digisum(self):
        self.assertEqual(p.digisum(1234), 10)
        self.assertEqual(p.digisum(1000), 1)
        self.assertEqual(p.digisum(0), 0)

    def test_numSquareSum(self):
        self.assertEqual(p.numSquareSum(123), 14)
        self.assertEqual(p.numSquareSum(0), 0)
        self.assertEqual(p.numSquareSum(7), 49)

    def test_isabundant(self):
        self.assertTrue(p.isabundant(12))
        self.assertFalse(p.isabundant(10))
        self.assertFalse(p.isabundant(6))

    def test_isarmstrong(self):
        self.assertTrue(p.isarmstrong(153))
        self.assertTrue(p.isarmstrong(370))
        self.assertFalse(p.isarmstrong(100))

    def test_isautomorphic(self):
        self.assertTrue(p.isautomorphic(5))
        self.assertTrue(p.isautomorphic(76))
        self.assertFalse(p.isautomorphic(10))

    def test_isbuzz(self):
        self.assertTrue(p.isbuzz(7))
        self.assertTrue(p.isbuzz(14))
        self.assertTrue(p.isbuzz(17))
        self.assertFalse(p.isbuzz(22))

    def test_iscircularprime(self):
        self.assertTrue(p.iscircularprime("197"))
        self.assertTrue(p.iscircularprime("71"))
        self.assertFalse(p.iscircularprime("123"))

    def test_iscurzon(self):
        self.assertTrue(p.iscurzon(5))
        self.assertTrue(p.iscurzon(14))
        self.assertFalse(p.iscurzon(8))

    def test_iscomposite(self):
        self.assertTrue(p.iscomposite(12))
        self.assertTrue(p.iscomposite(15))
        self.assertFalse(p.iscomposite(7))

    def test_iscoprime(self):
        self.assertTrue(p.iscoprime([3, 4, 5]))
        self.assertFalse(p.iscoprime([6, 8, 10]))

    def test_isdisarium(self):
        self.assertTrue(p.isdisarium(135))
        self.assertTrue(p.isdisarium(89))
        self.assertFalse(p.isdisarium(100))

    def test_isdudeney(self):
        self.assertTrue(p.isdudeney(512))  # 8^3 = 512, 5+1+2 = 8
        self.assertFalse(p.isdudeney(1000))

    def test_isduck(self):
        self.assertTrue(p.isduck(3210))
        self.assertTrue(p.isduck(7056))
        self.assertFalse(p.isduck(123))

    def test_iseven(self):
        self.assertTrue(p.iseven(2))
        self.assertTrue(p.iseven(100))
        self.assertFalse(p.iseven(15))

    def test_isfibonacci(self):
        self.assertTrue(p.isfibonacci(8))
        self.assertTrue(p.isfibonacci(13))
        self.assertFalse(p.isfibonacci(7))

    def test_ishappy(self):
        self.assertTrue(p.ishappy(19))
        self.assertTrue(p.ishappy(28))
        self.assertFalse(p.ishappy(4))

    def test_isharshad(self):
        self.assertFalse(p.isharshad(19))  
        self.assertTrue(p.isharshad(20))
        self.assertTrue(p.isharshad(21))

    def test_isheteromecic(self):
        self.assertTrue(p.isheteromecic(6))  # 6 = 2 * 3
        self.assertTrue(p.isheteromecic(12))  # 12 = 3 * 4
        self.assertFalse(p.isheteromecic(7))

    def test_iskrishnamurthy(self):
        self.assertTrue(p.iskrishnamurthy(145))  # 1! + 4! + 5! = 145
        self.assertFalse(p.iskrishnamurthy(123))


    def test_ismagic(self):
        self.assertTrue(p.ismagic(1))
        self.assertTrue(p.ismagic(10))
        self.assertFalse(p.ismagic(11))

    def test_isneon(self):
        self.assertTrue(p.isneon(9))  # 9^2 = 81, 8+1 = 9
        self.assertFalse(p.isneon(10))

    def test_isniven(self):
        self.assertFalse(p.isniven(19))  # Same as isharshad
        self.assertTrue(p.isniven(21))

    def test_isoblong(self):
        self.assertTrue(p.isoblong(6))  # 6 = 2 * 3
        self.assertTrue(p.isoblong(12))  # 12 = 3 * 4
        self.assertFalse(p.isoblong(7))

    def test_isodd(self):
        self.assertTrue(p.isodd(3))
        self.assertTrue(p.isodd(101))
        self.assertFalse(p.isodd(20))

    def test_ispalindrome(self):
        self.assertTrue(p.ispalindrome(121))
        self.assertTrue(p.ispalindrome(11))
        self.assertFalse(p.ispalindrome(123))

    def test_isperfect(self):
        self.assertTrue(p.isperfect(6))  # 1+2+3 = 6
        self.assertTrue(p.isperfect(28))  # 1+2+4+7+14 = 28
        self.assertFalse(p.isperfect(12))

    def test_isprime(self):
        self.assertTrue(p.isprime(2))
        self.assertTrue(p.isprime(17))
        self.assertFalse(p.isprime(1))
        self.assertFalse(p.isprime(15))

    def test_ispronic(self):
        self.assertTrue(p.ispronic(6))  # 6 = 2 * 3
        self.assertTrue(p.ispronic(12))  # 12 = 3 * 4
        self.assertFalse(p.ispronic(7))

    def test_issunny(self):
        self.assertTrue(p.issunny(24))  # 24 + 1 = 25, which is a perfect square
        self.assertFalse(p.issunny(23))

    def test_ispecial(self):
        self.assertTrue(p.ispecial(59))  # 5 + 9 + 5 * 9 = 59
        self.assertFalse(p.ispecial(60))

    def test_isspy(self):
        self.assertTrue(p.isspy(1124))  # 1+1+2+4 = 1*1*2*4 = 8
        self.assertFalse(p.isspy(1123))

    def test_istwinprime(self):
        self.assertTrue(p.istwinprime(3, 5))
        self.assertTrue(p.istwinprime(17, 19))
        self.assertFalse(p.istwinprime(3, 7))

    def test_istwistedprime(self):
        self.assertTrue(p.istwistedprime(13))  # 13 and 31 are both prime
        self.assertFalse(p.istwistedprime(23))  # 23 is prime but 32 is not

    def test_isunique(self):
        self.assertTrue(p.isunique(1234))
        self.assertFalse(p.isunique(1224))

    def test_istech(self):
        self.assertTrue(p.istech(2025))  # (20+25)^2 = 2025
        self.assertFalse(p.istech(2024))

    def test_isugly(self):
        self.assertTrue(p.isugly(6))
        self.assertTrue(p.isugly(8))
        self.assertFalse(p.isugly(14))

    def test_ar_circle(self):
        self.assertAlmostEqual(p.ar_circle(1), 2 * math.pi, places=7)
        self.assertAlmostEqual(p.ar_circle(2), 4 * math.pi, places=7)

    def test_ar_rect(self):
        self.assertEqual(p.ar_rect(4, 5), 20)
        self.assertEqual(p.ar_rect(3), 3)  # Testing default value of b=1

    def test_ar_triangle(self):
        self.assertAlmostEqual(p.ar_triangle(3, 4, 5), 6, places=7)
        self.assertAlmostEqual(p.ar_triangle(5, 5, 5), 10.825317547305483, places=7)


    def test_ismagic(self):
        self.assertTrue(p.ismagic(1))
        self.assertTrue(p.ismagic(10))
        self.assertFalse(p.ismagic(11))

    def test_isneon(self):
        self.assertTrue(p.isneon(9))  # 9^2 = 81, 8+1 = 9
        self.assertFalse(p.isneon(10))

    def test_isniven(self):
        self.assertTrue(p.isniven(18))  # Same as isharshad
        self.assertFalse(p.isniven(22))

    def test_isoblong(self):
        self.assertTrue(p.isoblong(6))  # 6 = 2 * 3
        self.assertTrue(p.isoblong(12))  # 12 = 3 * 4
        self.assertFalse(p.isoblong(7))

    def test_isodd(self):
        self.assertTrue(p.isodd(3))
        self.assertTrue(p.isodd(101))
        self.assertFalse(p.isodd(20))

    def test_ispalindrome(self):
        self.assertTrue(p.ispalindrome(121))
        self.assertTrue(p.ispalindrome(11))
        self.assertFalse(p.ispalindrome(123))

    def test_isperfect(self):
        self.assertTrue(p.isperfect(6))  # 1+2+3 = 6
        self.assertTrue(p.isperfect(28))  # 1+2+4+7+14 = 28
        self.assertFalse(p.isperfect(12))

    def test_isprime(self):
        self.assertTrue(p.isprime(2))
        self.assertTrue(p.isprime(17))
        self.assertFalse(p.isprime(1))
        self.assertFalse(p.isprime(15))

    def test_ispronic(self):
        self.assertTrue(p.ispronic(6))  # 6 = 2 * 3
        self.assertTrue(p.ispronic(12))  # 12 = 3 * 4
        self.assertFalse(p.ispronic(7))

    def test_issunny(self):
        self.assertTrue(p.issunny(24))  # 24 + 1 = 25, which is a perfect square
        self.assertFalse(p.issunny(23))

    def test_ispecial(self):
        self.assertTrue(p.ispecial(59))  # 5 + 9 + 5 * 9 = 59
        self.assertFalse(p.ispecial(60))

    def test_isspy(self):
        self.assertTrue(p.isspy(1124))  # 1+1+2+4 = 1*1*2*4 = 8
        self.assertFalse(p.isspy(1123))

    def test_istwinprime(self):
        self.assertTrue(p.istwinprime(3, 5))
        self.assertTrue(p.istwinprime(17, 19))
        self.assertFalse(p.istwinprime(3, 7))

    def test_istwistedprime(self):
        self.assertTrue(p.istwistedprime(13))  # 13 and 31 are both prime
        self.assertFalse(p.istwistedprime(23)) 

    def test_isunique(self):
        self.assertTrue(p.isunique(1234))
        self.assertFalse(p.isunique(1224))

    def test_istech(self):
        self.assertTrue(p.istech(2025))  # (20+25)^2 = 2025
        self.assertFalse(p.istech(2024))

    def test_isugly(self):
        self.assertTrue(p.isugly(6))
        self.assertTrue(p.isugly(8))
        self.assertFalse(p.isugly(14))

    def test_ar_circle(self):
        self.assertAlmostEqual(p.ar_circle(1), 2 * math.pi, places=7)
        self.assertAlmostEqual(p.ar_circle(2), 4 * math.pi, places=7)

    def test_ar_rect(self):
        self.assertEqual(p.ar_rect(4, 5), 20)
        self.assertEqual(p.ar_rect(3), 3)  # Testing default value of b=1

    def test_ar_triangle(self):
        self.assertAlmostEqual(p.ar_triangle(3, 4, 5), 6, places=7)
        self.assertAlmostEqual(p.ar_triangle(5, 5, 5), 10.825317547305483, places=7)
        self.assertAlmostEqual(p.ar_triangle(17, 21, 10), 84, places=7)

    def test_floyd(self):
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        p.floyd(3)
        sys.stdout = sys.__stdout__
        expected_output = "Floyd's Triangle\n1  \n2  3  \n4  5  6  \n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_fact(self):
        self.assertEqual(p.fact(5), 120)
        self.assertEqual(p.fact(0), 1)
        self.assertEqual(p.fact(1), 1)

    def test_factor(self):
        self.assertEqual(p.factor(12), [2, 3, 4, 6])
        self.assertEqual(p.factor(17), [])  # Prime number
        self.assertEqual(p.factor(1), [])

    def test_digiwords(self):
        # Basic behavior checks for number-to-word conversion.
        self.assertEqual(p.digiwords(0), "zero")
        self.assertEqual(p.digiwords(42), "Forty Two")
        self.assertEqual(p.digiwords(1999), "One Thousand Nine Hundred Ninety Nine")

    def test_comb(self):
        self.assertEqual(p.comb(5, 2), 10)
        self.assertEqual(p.comb(4, 4), 1)
        self.assertEqual(p.comb(3, 0), 1)

    def test_perm(self):
        self.assertEqual(p.perm(5, 2), 20)
        self.assertEqual(p.perm(4, 4), 24)
        self.assertEqual(p.perm(3, 0), 1)

    # Stack Functions Tests
    def test_stack_operations(self):
        stack = []
        p.s_push(stack, 1)
        p.s_push(stack, 2)
        p.s_push(stack, 3)

        self.assertEqual(p.s_size(stack), 3)
        self.assertFalse(p.s_Empty(stack))

        self.assertEqual(p.s_pop(stack), 3)
        self.assertEqual(p.s_top(stack), 2)

        p.s_pop(stack)
        p.s_pop(stack)
        self.assertTrue(p.s_Empty(stack))

        # Test underflow condition
        self.assertIsNone(p.s_pop(stack))

    def test_s_display(self):
        stack = [1, 2, 3]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        p.s_display(stack)
        sys.stdout = sys.__stdout__
        expected_output = "Current elements are : \n3\n2\n1\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # New Scientific and Intelligence APIs
    def test_convert_units(self):
        self.assertAlmostEqual(p.convert_units(1000, "m", "km"), 1.0, places=9)
        self.assertAlmostEqual(p.convert_units(1, "au", "km"), 149597870.7, places=3)
        with self.assertRaises(ValueError):
            p.convert_units(1, "foo", "m")

    def test_dimensional_analysis(self):
        result = p.dimensional_analysis(["m", "m"], ["s", "s"])
        self.assertEqual(result["units"], {"m": 2, "s": -2})
        self.assertEqual(result["expression"], "m^2 / s^2")

        no_dim = p.dimensional_analysis(["m"], ["m"])
        self.assertEqual(no_dim["expression"], "dimensionless")

    def test_solve_linear(self):
        self.assertEqual(p.solve_linear(2, -4), 2.0)
        with self.assertRaises(ValueError):
            p.solve_linear(0, 1)

    def test_solve_quadratic(self):
        real_case = p.solve_quadratic(1, -3, 2)
        self.assertEqual(real_case["type"], "quadratic")
        self.assertEqual(real_case["discriminant"], 1)
        self.assertEqual(real_case["roots"], (2.0, 1.0))

        complex_case = p.solve_quadratic(1, 2, 5)
        self.assertEqual(complex_case["type"], "quadratic")
        self.assertEqual(complex_case["discriminant"], -16)
        self.assertTrue(isinstance(complex_case["roots"][0], complex))

        linear_fallback = p.solve_quadratic(0, 2, -4)
        self.assertEqual(linear_fallback, {"type": "linear", "root": 2.0})

    def test_symbolic_derivative(self):
        self.assertEqual(p.symbolic_derivative("3x^3-2x+7"), "9x^2-2")
        self.assertEqual(p.symbolic_derivative("x^2+x"), "2x+1")
        self.assertEqual(p.symbolic_derivative("7"), "0")

    def test_statistics(self):
        stats = p.statistics([1, 2, 3, 4])
        self.assertEqual(stats["count"], 4)
        self.assertEqual(stats["sum"], 10.0)
        self.assertEqual(stats["min"], 1.0)
        self.assertEqual(stats["max"], 4.0)
        self.assertEqual(stats["mean"], 2.5)
        self.assertEqual(stats["median"], 2.5)
        self.assertAlmostEqual(stats["variance"], 1.25, places=9)
        self.assertAlmostEqual(stats["std_dev"], 1.1180339887, places=7)

        with self.assertRaises(ValueError):
            p.statistics([])

    def test_analyze_number_outputs(self):
        text_report = p.analyze(153)
        self.assertIn("153 is:", text_report)
        self.assertIn("Armstrong number", text_report)
        self.assertIn("Harshad number", text_report)

        dict_report = p.analyze_number(153, output="dict")
        self.assertEqual(dict_report["number"], 153)
        self.assertTrue("Armstrong number" in dict_report["properties"])

        json_report = p.analyze(153, output="json")
        decoded = json.loads(json_report)
        self.assertEqual(decoded["number"], 153)
        self.assertIn("properties", decoded)

        with self.assertRaises(TypeError):
            p.analyze_number(153.0)
    
if __name__ == '__main__':
    unittest.main()