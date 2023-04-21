import unittest
from pruevas import igualdad, Is_vf_X, Noigual, veri_lis

class CaseTest(unittest.TestCase):
    
    def test_igualdad(self):
        fun = igualdad(5,5)
        self.assertEqual(fun,True)
    def test_vORf(self):
        fun = Is_vf_X(True)
        if fun:
            self.assertTrue(fun)
        else:
            self.assertFalse(fun)
            
if __name__ == "__main__":
    unittest.main()