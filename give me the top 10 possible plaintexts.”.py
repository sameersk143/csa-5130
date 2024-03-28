import string

def letter_frequency_attack(ciphertext, top_n=10):
    # Define the English letter frequencies
    english_letter_frequencies = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
        'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
        'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
        'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
        'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
        'Z': 0.07
    }

    # Convert ciphertext to uppercase and remove non-alphabetic characters
    ciphertext = ''.join(char.upper() for char in ciphertext if char.isalpha())

    # Calculate the frequencies of each letter in the ciphertext
    ciphertext_letter_frequencies = {}
    for char in ciphertext:
        if char in ciphertext_letter_frequencies:
            ciphertext_letter_frequencies[char] += 1
        else:
            ciphertext_letter_frequencies[char] = 1

    # Calculate the shift for each letter based on the difference in frequencies
    shifts = {}
    for letter, frequency in english_letter_frequencies.items():
        if letter in ciphertext_letter_frequencies:
            ciphertext_frequency = ciphertext_letter_frequencies[letter] / len(ciphertext)
            shift = ord(letter) - ord('A') - ord(max(ciphertext_letter_frequencies, key=ciphertext_letter_frequencies.get)) + ord('A')
            shifts[letter] = shift

    # Sort shifts by likelihood
    sorted_shifts = sorted(shifts.items(), key=lambda x: x[1], reverse=True)

    # Generate possible plaintexts based on the top_n shifts
    possible_plaintexts = []
    for letter, shift in sorted_shifts[:top_n]:
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                plaintext += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                plaintext += char
        possible_plaintexts.append((plaintext, shift))

    return possible_plaintexts

def main():
    ciphertext = "KHOORZRUOG"
    top_n = 5

    print(f"Performing letter frequency attack on ciphertext: {ciphertext}")
    print(f"Finding top {top_n} possible plaintexts...")
    possible_plaintexts = letter_frequency_attack(ciphertext, top_n=top_n)

    print("\nTop possible plaintexts:")
    for plaintext, shift in possible_plaintexts:
        print(f"Shift {shift}: {plaintext}")

if __name__ == "__main__":
    main()
