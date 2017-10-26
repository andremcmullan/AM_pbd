

import unittest

from calculatorA import Calculator
		
class TestCalculator(unittest.TestCase):

	def test_calculator_divide(self):
        result = Calculator().divide(5,5)
        self.assertEqual(1, result)
        #result = Calculator().divide(5,0)
        #self.assertEqual(0, result)
        result = Calculator().divide(5,1)
        self.assertEqual(5, result)
        result = Calculator().divide(5,0.2)
        self.assertEqual(25, result)
        result = Calculator().divide(5,4)
        self.assertEqual(1.25, result)    

	def test_calculator_multiply(self):
		result = Calculator().multiply(5,5)
		self.assertEqual(25, result)
		result = Calculator().multiply(5,0)
		self.assertEqual(0, result)
		result = Calculator().multiply(5,1)
		self.assertEqual(5, result)
		result = Calculator().multiply(5,0.2)
		self.assertEqual(1, result)

	def test_calculator_add(self):
		result = Calculator().add(5, 5)
		self.assertEqual(10, result)
		result = Calculator().add(2, 3)
		self.assertEqual(5, result)
		result = Calculator().add(2, 0)
		self.assertEqual(2, result)
		result = Calculator().add('2', '5')
		self.assertEqual('25', result)
		
	def test_calculator_substract(self):
		result = Calculator().subtract(5, 5)
		self.assertEqual(0, result)
		
	def test_calculator_exponent(self):
		result = Calculator().exponent(5, 2)
		self.assertEqual(25, result)
		result = Calculator().exponent(2, 3)
		self.assertEqual(8, result)
		result = Calculator().exponent(2, 0)
		self.assertEqual(1, result)
        
    def test_calculator_sqr(self):
        result = self.calc.sqr(10)
        self.assertEqual(100, result)
        result = self.calc.sqr(6)
        self.assertEqual(36, result)
        result = self.calc.sqr(9)
        self.assertEqual(81, result)        

    def test_calculator_cbe(self):
        result = self.calc.cbe(10)
        self.assertEqual(1000, result)
        result = self.calc.cbe(6)
        self.assertEqual(216, result)
        result = self.calc.cbe(9)
        self.assertEqual(729, result)

    def test_calculator_tan(self):
        result = self.calc.tan_calcu(3)
        self.assertAlmostEqual(-0.142546543074, result)
        result = self.calc.tan_calcu(52)
        self.assertAlmostEqual(-6.05327238279, result)
        result = self.calc.tan_calcu(31)
        self.assertAlmostEqual(-0.441695568021, result)        

    def test_calculator_sin(self):
        result = self.calc.sin_calcu(68)
        self.assertAlmostEqual(-0.897927680689, result)
        result = self.calc.sin_calcu(12)
        self.assertAlmostEqual(-0.536572918, result)
        result = self.calc.sin_calcu(23)
        self.assertAlmostEqual(-0.846220404175, result)        
               
    def test_calculator_cos(self):
        result = self.calc.cos_calcu(25)
        self.assertAlmostEqual(0.991202811863, result)
        result = self.calc.cos_calcu(45)
        self.assertAlmostEqual(0.525321988818, result)
        result = self.calc.cos_calcu(7)
        self.assertAlmostEqual(0.753902254343, result)   	
		
		
			

if __name__ == '__main__':
			unittest.main()
		
 

