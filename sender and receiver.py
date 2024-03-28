import string

def generate_cipher(keyword):
    alphabet = list(string.ascii_uppercase)
    cipher = []

    # Mark letters of keyword as used in the alphabet list
    for char in keyword:
        char = char.upper()
        if char in alphabet:
            alphabet.remove(char)
            cipher.append(char)

    # Filling the remaining unused letters in the cipher sequence
    cipher.extend(alphabet)

    return ''.join(cipher)

def encrypt(plaintext, cipher):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext.append(cipher[ord(char) - ord('A')])
            else:
                ciphertext.append(cipher[ord(char.upper()) - ord('A')].lower())
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def main():
    keyword = "CIPHER"
    plaintext = "Hello, World!"

    cipher = generate_cipher(keyword)
    ciphertext = encrypt(plaintext, cipher)

    print("Plaintext:", plaintext)
    print("Cipher:", cipher)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
