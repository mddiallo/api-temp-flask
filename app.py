from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    celsius = data.get('celsius')
    if celsius is None:
        return jsonify({'error': 'Missing "celsius" value'}), 400
    fahrenheit = (celsius * 9/5) + 32
    return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit})

if __name__ == '__main__':
    app.run(debug=True)
