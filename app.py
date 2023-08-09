from flask import (Flask, render_template, request, jsonify)

app = Flask(__name__)

@app.route('/')
def index():
    print('request for index page received')
    return render_template('index.html')

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
