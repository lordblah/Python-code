import unittest
from calculate import calculate

"""testing startard is to append the program name then add test to the end of it
    also explain in the def function name what the test is doing breifly in the rest of the name.
    example of this is test_add_method_returns_correct_name"""
class TestCalculate(unittest.TestCase):
    def Setup(self):
        self.calc = calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2,2))


    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError,self.calc.add,"Hello", "World")


if __name__ == '__main__':
    unittest.main()



