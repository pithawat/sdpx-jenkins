import unittest
from app import app

class PlusTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_getcode(self):
        res = self.client.get('/getcode')
        self.assertEqual(res.get_json(), {"message": "hello link"})

    def test_positive_plus(self):
        res = self.client.get('/plus/5/6')
        self.assertEqual(res.get_json(),{"sum":11})
    
    def test_x_is_3dot7(self):
        res = self.client.get('is2hornor/3.7')
        self.assertEqual(res.get_json(),{"gpax":False})
        
    def test_x_is_3dot4(self):
        res = self.client.get('is2hornor/3.4')
        self.assertEqual(res.get_json(),{"gpax":True})
    
    def test_x_is_3dot1(self):
        res = self.client.get('is2hornor/3.1')
        self.assertEqual(res.get_json(),{"gpax":False})

if __name__ == "__main__":
    unittest.main()
    