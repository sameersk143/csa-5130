def generate_matrix(key):
    # Create a 5x5 matrix initialized with empty strings
    matrix = [['' for _ in range(5)] for _ in range(5)]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Excluding 'J' (combining I and J)

    # Populate the matrix with the keyword
    key = key.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    key = ''.join(dict.fromkeys(key))  # Remove duplicate letters
    key_index = 0
    alpha_index = 0

    # Fill the matrix row by row
    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                matrix[i][j] = key[key_index]
                key_index += 1
            else:
                while alphabet[alpha_index] in key:
                    alpha_index += 1
                matrix[i][j] = alphabet[alpha_index]
                alpha_index += 1

    return matrix

def prepare_input(text):
    # Remove spaces and non-alphabetic characters, convert to uppercase
    text = ''.join(filter(str.isalpha, text.upper()))
    # Replace 'J' with 'I'
    text = text.replace('J', 'I')
    # If the length of text is odd, add a padding character 'X' at the end
    if len(text) % 2 != 0:
        text += 'X'
    return text

def encrypt(plaintext, key):
    matrix = generate_matrix(key)
    plaintext = prepare_input(plaintext)
    ciphertext = []

    for i in range(0, len(plaintext), 2):
        pair1 = plaintext[i]
        pair2 = plaintext[i + 1]
        row1, col1 = None, None
        row2, col2 = None, None

        # Find the positions of the two letters in the matrix
        for row in range(5):
            if pair1 in matrix[row]:
                row1, col1 = row, matrix[row].index(pair1)
            if pair2 in matrix[row]:
                row2, col2 = row, matrix[row].index(pair2)
        # Case 1: If the letters are in the same row
        if row1 == row2:                    
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        # Case 2: If the letters are in the same column
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        # Case 3: If the letters form a rectangle
        else:
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])

    return ''.join(ciphertext)

# Example usage:
plaintext = "HELLO WORLD"
key = "KEYWORD"
encrypted_text = encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
