import unittest
import hello

class TestSum(unittest.TestCase):
    def test_2_2_calc(self):
        res = hello.calc(2, 2)
        self.assertAlmostEqual(res, 8.965, places = 3, msg = 'Should be 8.965')

    def test_2_3_calc(self):
        res = hello.calc(2, 3)
        self.assertAlmostEqual(res, 257.097, places = 3, msg = 'Should be 257.097')

    def test_3_2_calc(self):
        res = hello.calc(3, 2)
        self.assertAlmostEqual(res, 27.965, places = 3, msg = 'Should be 27.965')
    
    def test_3_3_calc(self):
        res = hello.calc(3, 3)
        self.assertAlmostEqual(res, 6562.097, places = 3, msg = 'Should be 6562.097')

    def test_3_4_calc(self):
        res = hello.calc(3, 4)
        self.assertAlmostEqual(res, 14348908.290, places = 3, msg = 'Should be 14348908.290')
    
    def test_4_3_calc(self):
        res = hello.calc(4, 3)
        self.assertAlmostEqual(res, 65537.097, places = 3, msg = 'Should be 65537.097')
    
    def test_4_4_calc(self):
        res = hello.calc(4, 4)
        self.assertAlmostEqual(res, 1073741825.290, places = 3, msg = 'Should be 1073741825.290')

if __name__ == '__main__':
    unittest.main()