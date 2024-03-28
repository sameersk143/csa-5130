def text_to_numbers(text):
    """Convert a string of uppercase letters to a list of corresponding numbers."""
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    """Convert a list of numbers to a string of corresponding uppercase letters."""
    return ''.join([chr(num + ord('A')) for num in numbers])

def inverse_matrix(matrix):
    """Calculate the inverse of a 2x2 matrix."""
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det_inv = pow(det, -1, 26)  # Calculate the modular inverse of the determinant
    inverse = [
        [matrix[1][1] * det_inv % 26, -matrix[0][1] * det_inv % 26],
        [-matrix[1][0] * det_inv % 26, matrix[0][0] * det_inv % 26]
    ]
    return inverse

def multiply_matrix(matrix1, matrix2):
    """Multiply two 2x2 matrices."""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = (matrix1[i][0] * matrix2[0][j] + matrix1[i][1] * matrix2[1][j]) % 26
    return result

def encrypt(message, key):
    """Encrypt a message using the Hill cipher."""
    message = text_to_numbers(message)
    key = [[key[0], key[1]], [key[2], key[3]]]
    while len(message) % 2 != 0:
        message.append(23)  # Append 'X' if message length is odd (X is 23 in ASCII)
    encrypted_message = ""
    for i in range(0, len(message), 2):
        chunk = [message[i], message[i+1]]
        encrypted_chunk = multiply_matrix(key, [chunk])
        encrypted_message += numbers_to_text(encrypted_chunk[0])
    return encrypted_message

def known_plaintext_attack(plaintext, ciphertext):
    """Recover the encryption key from known plaintext-ciphertext pairs."""
    P = [[plaintext[0], plaintext[1]], [plaintext[2], plaintext[3]]]
    C = [[ciphertext[0], ciphertext[1]], [ciphertext[2], ciphertext[3]]]
    key = multiply_matrix(C, inverse_matrix(P))
    return [key[0][0], key[0][1], key[1][0], key[1][1]]

def main():
    # Example known plaintext and corresponding ciphertext
    known_plaintext = "HELLO"
    corresponding_ciphertext = "JVDND"

    # Perform known plaintext attack
    recovered_key = known_plaintext_attack(text_to_numbers(known_plaintext), text_to_numbers(corresponding_ciphertext))
    print("Recovered key:")
    print(recovered_key)

    # Test the recovered key by encrypting a new message
    new_message = "WORLD"
    print("New message:", new_message)
    encrypted_message = encrypt(new_message, recovered_key)
    print("Encrypted message using recovered key:", encrypted_message)

if __name__ == "__main__":
    main()

