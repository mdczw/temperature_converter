FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY temperature_converter.py .
CMD ["python3", "temperature_converter.py"]
