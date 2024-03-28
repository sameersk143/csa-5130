import string
from collections import Counter

def load_text(filename):
    """Load text from a file."""
    with open(filename, 'r') as file:
        return file.read().upper()

def save_text(filename, text):
    """Save text to a file."""
    with open(filename, 'w') as file:
        file.write(text)

def calculate_frequency(text):
    """Calculate letter frequency in the text."""
    text = text.replace(" ", "")
    counter = Counter(text)
    total_letters = sum(counter.values())
    frequency = {char: count / total_letters for char, count in counter.items()}
    return frequency

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the provided key."""
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_text += key[char]
        else:
            decrypted_text += char
    return decrypted_text

def frequency_attack(ciphertext, known_frequency, n=10):
    """Perform a frequency attack on the ciphertext."""
    decrypted_texts = []
    for _ in range(n):
        key = {}
        shuffled_alphabet = list(string.ascii_uppercase)
        for cipher_char, _ in known_frequency.most_common():
            plain_char = max(shuffled_alphabet, key=lambda x: known_frequency[x])
            key[cipher_char] = plain_char
            shuffled_alphabet.remove(plain_char)
        decrypted_text = decrypt(ciphertext, key)
        decrypted_texts.append(decrypted_text)
        known_frequency = Counter(decrypted_text)
    return decrypted_texts

def main():
    # Load ciphertext from a file
    ciphertext = load_text("ciphertext.txt")

    # Calculate letter frequency in English
    english_frequency = {
        'E': 0.127, 'T': 0.091, 'A': 0.082, 'O': 0.075, 'I': 0.070,
        'N': 0.067, 'S': 0.063, 'H': 0.061, 'R': 0.060, 'D': 0.043,
        'L': 0.040, 'C': 0.028, 'U': 0.028, 'M': 0.024, 'W': 0.024,
        'F': 0.022, 'G': 0.020, 'Y': 0.019, 'P': 0.019, 'B': 0.015,
        'V': 0.009, 'K': 0.008, 'J': 0.002, 'X': 0.001, 'Q': 0.001,
        'Z': 0.001
    }

    # Perform frequency attack
    decrypted_texts = frequency_attack(ciphertext, english_frequency, n=10)

    # Save the decrypted texts to files
    for i, text in enumerate(decrypted_texts):
        save_text(f"decrypted_text_{i+1}.txt", text)

if __name__ == "__main__":
    main()
