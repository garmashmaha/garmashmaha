from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/czy_znaja_sie', methods=['GET'])
def api_czy_znaja_sie():
    osoba1 = request.args.get('osoba1')
    osoba2 = request.args.get('osoba2')
    return jsonify(czy_znaja_sie(osoba1, osoba2))

@app.route('/znajomi', methods=['GET'])
def api_znajomi():
    osoba = request.args.get('osoba')
    return jsonify(znajomi(osoba))

@app.route('/kogo_zapytac', methods=['GET'])
def api_kogo_zapytac():
    osoba = request.args.get('osoba')
    rzecz = request.args.get('rzecz')
    return jsonify(kogo_zapytac(osoba, rzecz))

if __name__ == '__main__':
    app.run(debug=True)