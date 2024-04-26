The Temperature Converter is a Python-based web application with an HTTP API that converts Fahrenheit to Celsius and responds with the Celsius temperature along with a randomly generated app identifier.

## Local
To run the application locally, enter the commands:
```
pip3 install -r requirements.txt
pip3 temperature_converter.py
```

To check for correctness enter:
```
curl -X POST -H "Content-Type: application/json" -d '{"fahrenheit_degrees": 100}' http://localhost:5000/convert-to-celsius
```

## Docker
To run an application inside a Docker container, enter the following commands:
```
docker build -t temperature_converter .
docker run -d -p 8080:5000 --name temperature_converter temperature_converter
```

## Kubernetes
To run the application in Kubernetes enter the following command:
```
helm install my-app helm-charts/app/
```
## Locust
To run the Locust in Kubernetes enter the following command:
```
helm install locust locust/
```