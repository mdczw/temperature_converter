from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Generate a UUID for the app identifier
app_identifier = str(uuid.uuid4())

def convert_fahrenheit_to_celsius(fahrenheit_degrees):
    return (fahrenheit_degrees - 32) * 5 / 9

@app.route('/convert-to-celsius', methods=['POST'])
def convert_to_celsius():
    data = request.get_json()
    if 'fahrenheit_degrees' not in data:
        return jsonify({'error': 'Fahrenheit temperature is required.'}), 400

    try:
        fahrenheit_degrees = float(data['fahrenheit_degrees'])
        celsius_degrees = convert_fahrenheit_to_celsius(fahrenheit_degrees)
        return jsonify({'celsius_degrees': celsius_degrees, 'app_identifier': app_identifier}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input. Fahrenheit temperature must be a number.'}), 400

if __name__ == '__main__':
    print(f"App identifier: {app_identifier}")
    app.run(host="0.0.0.0", debug=True)
