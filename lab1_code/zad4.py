from flask import Flask, request, jsonify

app = Flask(__name__)

def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Sortowanie znaków w kolejności ASCII bez użycia wbudowanych metod sortowania
    sorted_chars = insertion_sort(char_count)

    return sorted_chars

# Prosty algorytm sortowania przez wstawianie
def insertion_sort(char_count):
    keys = list(char_count.keys())
    for i in range(1, len(keys)):
        current_char = keys[i]
        j = i - 1
        while j >= 0 and ord(current_char) < ord(keys[j]):
            keys[j + 1] = keys[j]
            j -= 1
        keys[j + 1] = current_char
    
    sorted_chars = [(char, char_count[char]) for char in keys]
    return sorted_chars

@app.route('/count_chars', methods=['POST'])
def count_chars():
    if 'string' not in request.form:
        return jsonify({"error": "Brak parametru 'string'."}), 400
    
    text = request.form['string']
    result = count_characters(text)
    
    return jsonify({"character_count": result})

if __name__ == '__main__':
    app.run(debug=True)

