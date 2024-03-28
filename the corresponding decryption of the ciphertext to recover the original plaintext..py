import numpy as np

def text_to_numbers(text):
    text = text.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def encrypt(message, key):
    message = text_to_numbers(message)
    key = np.array(key).reshape(2, 2)
    while len(message) % 2 != 0:
        message.append(23)  # Append 'X' if message length is odd (X is 23 in ASCII)
    message_matrix = np.array(message).reshape(-1, 2)
    encrypted_message = ""
    for chunk in message_matrix:
        encrypted_chunk = np.dot(key, chunk) % 26
        encrypted_message += numbers_to_text(encrypted_chunk)
    return encrypted_message

def decrypt(ciphertext, key):
    key = np.array(key).reshape(2, 2)
    key_inverse = np.linalg.inv(key)
    determinant = int(round(np.linalg.det(key)))
    key_inverse *= determinant * np.linalg.inv(key).astype(int) % 26
    key_inverse %= 26
    return encrypt(ciphertext, key_inverse)

def main():
    message = "meet me at the usual place at ten rather than eight oclock"
    key = [9, 4, 5, 7]

    print("Original message:", message)

    encrypted_message = encrypt(message, key)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
