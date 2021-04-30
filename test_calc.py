import unittest
from Calculator import Calculator

class CalculatorTest(unittest.Testcase):
  def setUp(self):
    self.calculator = Calculator()  
  
  def test_add(self):
		self.assertEqual(self.calculator.add(10,5), 15)
    
  def test_sub(self):
    self.assertEqual(self.calculator.sub(5, 10), -5)
	
  def test_mult(self):
  	self.assertEqual(self.calculator.mult(5, 10), 50)
  
  def test_div(self):
    self.assertAlmostEqual(self.calculator.div(5, 10), .5)

if __name__ == "__main__":
	unittest.main()



