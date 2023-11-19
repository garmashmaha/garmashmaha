from flask import Flask, jsonify

app=Flask(__name__)

@app.route("/")
def witajSwiecie():
    return "Hello, World!"

@app.route("/dane")
def dane():
    return jsonify({'imie': 'Maria', 'nazwisko': 'Harmash', 'email': 'mashagarmash.17@gmail.com'})

app.run