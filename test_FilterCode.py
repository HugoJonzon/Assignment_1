import math
import unittest
from FilterCode import Filter2

class TestFilter(unittest.TestCase):
    def test_get_resonance_point(self):
        self.assertAlmostEqual(Filter2("HP",1/(3.1415**2),4,5).get_resonance_point(),0.25)

    def test_get_damping_factor(self):
        self.assertAlmostEqual(Filter2("HP",5,2,3).get_damping_factor(),0.9487)
          
    def test_get_transfer(self):
        transferLP = "1 / (s^2*{} + s*{} + 1)".format(20, 12)
        transferHP = "(s^2*{}) / (s^2*{} + s*{} + 1)".format(20,20, 12) 
        self.assertEqual(Filter2("LP",5,4,3).get_transfer(),transferLP)
        self.assertEqual(Filter2("HP",5,4,3).get_transfer(),transferHP)
        
    def test_wrong_input_type(self):
        with self.assertRaises(ValueError):
            Filter2("WRONG",1,1,1)
        
    def test_wrong_val(self):
        with self.assertRaises(ValueError):
            Filter2("LP",-1,1,1)
            Filter2("LP",1,-1,1)
            Filter2("LP",1,1,-1)
