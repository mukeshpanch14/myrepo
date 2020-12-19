import unittest
import bmiCalculation as bmc

class TestBMICalculation(unittest.TestCase):
    
    def test_calculateBMI(self):
        tbmc=bmc.BMICalculation('sample.json')
        self.assertRaises(ZeroDivisionError,tbmc.calculateBMI,5,0)
        self.assertRaises(ValueError,tbmc.calculateBMI,'a',1)
        self.assertRaises(ValueError,tbmc.calculateBMI,5,'a')
        self.assertRaises(ValueError,tbmc.calculateBMI,-5,1)
        self.assertAlmostEqual(round(tbmc.calculateBMI(87,175),2),28.41)
        
    def test_checkBMIRange(self):
        tbmc=bmc.BMICalculation('sample.json')
        self.assertRaises(ValueError,tbmc.checkBMIRange,-4)
        self.assertRaises(ValueError,tbmc.checkBMIRange,0)
        
        
    if __name__ == '__main__':
        unittest.main()