import unittest

from fibo import calc_fibo

class TestMyFibo(unittest.TestCase):
    
    # def setUp(self):
    #    print("avvio test")

    # def tearDown(self):
    #    print("fine test")

    def test_base(self):
        self.assertEqual(calc_fibo(0), 0)
        self.assertEqual(calc_fibo(1), 1)

    def test_fibo_small(self):
        self.assertEqual(calc_fibo(6), 8)
        self.assertEqual(calc_fibo(8), 21)
        
    def test_fibo_big(self):
        self.assertEqual(calc_fibo(20), 6765)
        self.assertEqual(calc_fibo(30), 832040)

    def test_negative(self):
        with self.assertRaises(ValueError):
            calc_fibo(-1)
    
    def test_string(self):
        with self.assertRaises(TypeError) as cm:
            calc_fibo("ciao")
            calc_fibo("12")

        the_exception = cm.exception
        self.assertRegexpMatches(str(the_exception), r"\\CORSO:")

if __name__ == '__main__':
    unittest.main()