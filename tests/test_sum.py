import unittest
import sum

class TestSumFunc(unittest.TestCase):
    
    def test_sumFunc(self):
        self.assertEqual(sum.sumTwo(10, 20), 20+10)
    
    def test_sumFunc1(self):
        self.assertEqual(sum.sumTwo(20, 10), 10+20)
    
    def test_two_float(self):
        self.assertEqual(sum.sumTwo(1.222, 3.332), 1.222+3.332, msg="Sum of two float does not match")
    
    def test_three_float(self):
        self.assertAlmostEqual(sum.sumThree(3.43332, 5.4444, 9.1111), 3.43332+5.4444+9.1111)




if __name__ == "__main__":
    unittest.main()