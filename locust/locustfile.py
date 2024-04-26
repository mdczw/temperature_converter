from locust import HttpUser, task
import random

class TemperatureConverterUser(HttpUser):
    @task
    def test_convert_temperature(self):
        self.client.post("/convert-to-celsius", json={"fahrenheit_degrees":random.randrange(500)})
