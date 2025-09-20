import unittest
from app import app

class PlusTest(unittest.TestCase):

    def test_getcode(self):
        res = app.hello()
        self.assertEqual(res,"hello")

    def test_positive_plus(self):
        res = app.plus(5,6)
        self.assertEqual(res,11)
    
if __name__ == "__main__":
    unittest.main()
    