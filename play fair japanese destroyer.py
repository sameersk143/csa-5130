def create_playfair_matrix(key):
    key = key.replace(' ', '').upper()  # Remove spaces and convert to uppercase
    key = ''.join(dict.fromkeys(key))    # Remove duplicate characters
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

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)
        if row1 == row2:  # Same row, shift left
            plaintext += matrix[row1*5 + (col1 - 1) % 5]
            plaintext += matrix[row2*5 + (col2 - 1) % 5]
        elif col1 == col2:  # Same column, shift up
            plaintext += matrix[((row1 - 1) % 5) * 5 + col1]
            plaintext += matrix[((row2 - 1) % 5) * 5 + col2]
        else:  # Form a rectangle, swap column
            plaintext += matrix[row1 * 5 + col2]
            plaintext += matrix[row2 * 5 + col1]
    return plaintext

def main():
    ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
    key = "KENNEDY"
    plaintext = playfair_decrypt(ciphertext.replace(' ', ''), key)
    print("Decrypted message:", plaintext)

if __name__ == "__main__":
    main()
