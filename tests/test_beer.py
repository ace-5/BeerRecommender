import unittest
from packages import beer

class TestBeer(unittest.TestCase):
    def test_float_number(self):
        self.assertEqual(len(beer.random(5.5)), 5)
    
    def test_negative_number(self):
        self.assertEqual(len(beer.random(-5)), 5)
    
    def test_postive_integer(self):
        self.assertEqual(len(beer.random(5)), 5)
    
    def test_argument_instance(self):
        no_of_suggestion = 'a'
        self.assertIsInstance(no_of_suggestion, int)

if __name__ == "__main__":
    unittest.main()
