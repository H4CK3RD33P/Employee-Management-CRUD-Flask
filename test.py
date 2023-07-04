import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_employees_route(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()