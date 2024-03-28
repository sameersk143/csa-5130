def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = int(key[key_index])
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = int(key[key_index])
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext

def main():
    plaintext = "HELLO"
    key = "3 19 5"
    
    # Encryption
    ciphertext = vigenere_encrypt(plaintext, key.split())
    print("Ciphertext:", ciphertext)
    
    # Decryption
    decrypted_text = vigenere_decrypt(ciphertext, key.split())
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
