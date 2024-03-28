def create_playfair_matrix(key):
    key = key.replace(' ', '').upper()  # Remove spaces and convert to uppercase
    key = ''.join(dict.fromkeys(key))    # Remove duplicate characters
    key = key.replace('J', 'I')          # Replace J with I
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Playfair matrix without 'J'
    matrix = ''
    
    for char in key:
        matrix += char
        alphabet = alphabet.replace(char, '')  # Remove key character from alphabet

    matrix += alphabet  # Add remaining alphabet characters to the matrix

    return matrix

def find_char_position(matrix, char):
    row = col = -1
    for i in range(5):
        for j in range(5):
            if matrix[i*5 + j] == char:
                row = i
                col = j
                break
    return row, col

def playfair_encrypt(plaintext, key):
    plaintext = plaintext.replace(' ', '').upper()  # Remove spaces and convert to uppercase
    plaintext = plaintext.replace('J', 'I')        # Replace J with I
    matrix = create_playfair_matrix(key)
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i+1] if i+1 < len(plaintext) else 'X'  # Add 'X' if plaintext length is odd
        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)
        if row1 == row2:  # Same row, shift right
            ciphertext += matrix[row1*5 + (col1 + 1) % 5]
            ciphertext += matrix[row2*5 + (col2 + 1) % 5]
        elif col1 == col2:  # Same column, shift down
            ciphertext += matrix[((row1 + 1) % 5) * 5 + col1]
            ciphertext += matrix[((row2 + 1) % 5) * 5 + col2]
        else:  # Form a rectangle, take opposite corners
            ciphertext += matrix[row1 * 5 + col2]
            ciphertext += matrix[row2 * 5 + col1]
    return ciphertext

def main():
    key = "PLAYFAIR"
    plaintext = "Must see you over Cadogan West. Coming at once."
    ciphertext = playfair_encrypt(plaintext, key)
    print("Encrypted message:", ciphertext)

if __name__ == "__main__":
    main()
