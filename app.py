from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('searchindex.html')

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    return jsonify({'lat': lat, 'lon': lon})

if __name__ == '__main__':
    app.run(debug=True)
