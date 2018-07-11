import unittest

from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_root_endpoint(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        self.assertIn('It works!', response.data)

    def test_ping_endpoint(self):
        response = self.client.get('/ping')

        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        self.assertIn('Pong', response.data)

    def test_missing_endpoint(self):
        response = self.client.get('/missing')

        self.assertEqual(response.status_code, 404)
        self.assertIn('text/html', response.content_type)

