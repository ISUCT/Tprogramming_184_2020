import unittest
import hello

class TestSum(unittest.TestCase):

    def test_task_a(self):
        res = hello.task_a(1.25, 3.25, 0.4)
        expected = [(1.25, 1.5627118033190683), 
                (1.65, 1.444483346894103), 
                (2.05, 1.9965848768889245), 
                (2.4499999999999997, 2.2878864247889314), 
                (2.8499999999999996, 2.508805958133056), 
                (3.2499999999999996, 2.692928296997281)]
        self.assertAlmostEqual(res, expected, places=3)


    def test_task_b(self):
        res = hello.task_b([1.84, 2.71, 3.81, 4.56, 5.62])
        expected = [(1.84, 1.7791658793122687), 
                (2.71, 2.43670615212377), 
                (3.81, 2.913109519389466), 
                (4.56, 3.164503036090737), 
                (5.62, 3.4668624552335574)]
        self.assertAlmostEqual(res, expected, places=3)

    def test_calc1(self):
        res = hello.calc(1.65)
        expected = 1.444
        self.assertAlmostEqual(res, expected, places=2)

    def test_calc2(self):
        res = hello.calc(4.56)
        expected = 3.164
        self.assertAlmostEqual(res, expected, places=2)

if __name__ == '__main__':
    unittest.main()