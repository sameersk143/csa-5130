import re
from collections import Counter

def load_common_words():
    with open("common_words.txt", "r") as file:
        common_words = file.read().splitlines()
    return common_words

def load_ciphertext():
    with open("ciphertext.txt", "r") as file:
        ciphertext = file.read()
    return ciphertext

def count_characters(text):
    text = re.sub(r'[^a-zA-Z]', '', text)  # Remove non-alphabetic characters
    return Counter(text.lower())

def guess_characters(frequencies, known_mappings):
    # Make educated guesses based on the frequency analysis and known mappings
    guess = {
        'x': 'e',  # Most common character is guessed as 'e'
        'q': 't',  # Assuming 'q' corresponds to 't'
        'u': 'h',  # Assuming 'u' corresponds to 'h'
        'i': 'o',  # Assuming 'i' corresponds to 'o'
        'c': 'a',  # Assuming 'c' corresponds to 'a'
        'g': 'n',  # Assuming 'g' corresponds to 'n'
        'j': 'r',  # Assuming 'j' corresponds to 'r'
        'k': 's',  # Assuming 'k' corresponds to 's'
        'f': 'i',  # Assuming 'f' corresponds to 'i'
        'b': 'd',  # Assuming 'b' corresponds to 'd'
        'z': 'l',  # Assuming 'z' corresponds to 'l'
        'm': 'c',  # Assuming 'm' corresponds to 'c'
        'p': 'm',  # Assuming 'p' corresponds to 'm'
        'd': 'u',  # Assuming 'd' corresponds to 'u'
        'w': 'f',  # Assuming 'w' corresponds to 'f'
        'l': 'g',  # Assuming 'l' corresponds to 'g'
        'o': 'w',  # Assuming 'o' corresponds to 'w'
        'n': 'p',  # Assuming 'n' corresponds to 'p'
        'y': 'y',  # Assuming 'y' remains 'y'
        't': 'b',  # Assuming 't' corresponds to 'b'
        'v': 'v',  # Assuming 'v' remains 'v'
        's': 'k',  # Assuming 's' corresponds to 'k'
        'h': 'x',  # Assuming 'h' corresponds to 'x'
        'r': 'q',  # Assuming 'r' corresponds to 'q'
        'e': 'j',  # Assuming 'e' corresponds to 'j'
        'a': 'z',  # Assuming 'a' corresponds to 'z'
    }
    for key, value in known_mappings.items():
        guess[key] = value
    return guess

def decrypt(ciphertext, mapping):
    decrypted_text = ''
    for char in ciphertext:
        decrypted_text += mapping.get(char, char)
    return decrypted_text

def main():
    common_words = load_common_words()
    ciphertext = load_ciphertext()
    frequencies = count_characters(ciphertext)

    print("Character frequencies in the ciphertext:")
    print(frequencies.most_common())

    known_mappings = {}  # Add known character mappings here

    guessed_mapping = guess_characters(frequencies, known_mappings)
    decrypted_text = decrypt(ciphertext, guessed_mapping)

    print("\nDecrypted text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()
