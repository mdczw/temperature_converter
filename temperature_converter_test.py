import unittest
import json
from temperature_converter import app

class TestTemperatureConversion(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_convert_temperature_successfully(self):
        # Test with valid input
        response = self.app.post('/convert-to-celsius', json={'fahrenheit_degrees': 41})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['celsius_degrees'], 5)
        self.assertTrue('app_identifier' in data)
        
    def test_convert_temperature_missed_data(self):
        # Test with invalid input (missing 'fahrenheit_degrees' key)
        response = self.app.post('/convert-to-celsius', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Fahrenheit temperature is required.')

    def test_convert_temperature_invalid_data(self):
        # Test with invalid input (non-numeric 'fahrenheit_degrees')
        response = self.app.post('/convert-to-celsius', json={'fahrenheit_degrees': 'invalid'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid input. Fahrenheit temperature must be a number.')

if __name__ == '__main__':
    unittest.main()