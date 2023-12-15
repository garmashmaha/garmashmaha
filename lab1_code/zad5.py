from flask import Flask, request, jsonify
import re  # Dodaj tę linię

app = Flask(__name__)

def count_characters(text, words):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Sortowanie znaków w kolejności ASCII bez użycia wbudowanych metod sortowania
    sorted_chars = insertion_sort(char_count)
    sorted_words = insertion_sort_words(words)

    # Liczenie wystąpień słów
    word_count = count_word_occurrences(text, sorted_words)

    return sorted_chars, word_count

# Prosty algorytm sortowania przez wstawianie dla znaków
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

# Prosty algorytm sortowania przez wstawianie dla słów
def insertion_sort_words(words):
    for i in range(1, len(words)):
        current_word = words[i]
        j = i - 1
        while j >= 0 and current_word < words[j]:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = current_word
    
    return words

# Liczenie wystąpień słów w tekście
def count_word_occurrences(text, words):
    word_count = {}
    for word in words:
        pattern = r'\b' + word + r'\b'  # Szukaj całych słów, a nie tylko sekwencji znaków
        matches = re.findall(pattern, text)
        word_count[word] = len(matches)
    return word_count

@app.route('/count_chars_and_words', methods=['POST'])
def count_chars_and_words():
    if 'string' not in request.form or 'words' not in request.form:
        return jsonify({"error": "Brak parametru 'string' lub 'words'."}), 400
    
    text = request.form['string']
    words = request.form['words'].split(',')  # Parametr 'words' przekazany jako ciąg słów oddzielonych przecinkami
    
    sorted_chars, word_count = count_characters(text, words)
    
    return jsonify({"character_count": sorted_chars, "word_count": word_count})

if __name__ == '__main__':
    app.run(debug=True)
