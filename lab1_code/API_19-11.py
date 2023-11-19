from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route("/")
def witajSwiecie():
    return "Hello, World!"

@app.route("/dane")
def dane():
    return jsonify({'imie': 'Maria', 'nazwisko': 'Harmash', 'email': 'mashagarmash.17@gmail.com'})

@app.route("/dane", methods=['POST'])
def LoadJson():
    content_type=request.headers.get('Content-type')
    if(content_type=='application/json'):
        mojeDane=request.get_json()
        return mojeDane

app.run()