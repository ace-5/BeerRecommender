import unittest
from packages import beer

class TestBeer(unittest.TestCase):
    def test_float_number(self):
        self.assertEqual(len(beer.random(5.5)), 5)
    
    def test_negative_number(self):
        self.assertEqual(len(beer.random(-5)), 0)
    
    def test_postive_integer(self):
        self.assertEqual(len(beer.random(5)), 5)
    

    def test_get_specified_beer(self):
        result = '{\n  "name": "Buzz",\n  "tagline": "A Real Bitter Experience.",\n  "description": "A light, crisp and bitter IPA brewed with English and American hops. A small batch brewed only once."\n}'
        self.assertEqual(beer.get_specified_beer(6, 9)[0], result)

if __name__ == "__main__":
    unittest.main()
