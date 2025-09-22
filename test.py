import unittest
from app import app

class PlusTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_getcode(self):
        res = self.client.get('/getcode')
        self.assertEqual(res.get_json(), {"message": "hello few"})

    def test_positive_plus(self):
        res = self.client.get('/plus/5/6')
        self.assertEqual(res.get_json(),{"sum":11})
    
if __name__ == "__main__":
    unittest.main()
    