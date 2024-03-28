def generate_vigenere_table():
    """
    Generate the Vigenère table for encryption and decryption.
    """
    table = [['' for _ in range(26)] for _ in range(26)]
    for row in range(26):
        for col in range(26):
            table[row][col] = chr(((row + col) % 26) + ord('A'))
    return table


def polyalphabetic_substitution_encrypt(plain_text, key):
    """
    Encrypt the plain text using a polyalphabetic substitution cipher (Vigenère cipher) with the given key.
    """
    table = generate_vigenere_table()
    encrypted_text = ''
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                encrypted_text += table[ord(char) - ord('A')][shift]
            else:
                encrypted_text += table[ord(char.upper()) - ord('A')][shift].lower()
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char

    return encrypted_text


# Example usage:
plain_text = input("Enter plain text: ")
key = input("Enter key: ")

encrypted_text = polyalphabetic_substitution_encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)
