def gcd(a, b):
    """
    Find the greatest common divisor of two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """
    Find the modular multiplicative inverse of a number.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def break_affine_cipher(cipher_text, most_frequent_letter, second_most_frequent_letter):
    """
    Break the affine cipher using the frequencies of the most and second most frequent letters in the ciphertext.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    most_frequent_index = alphabet.index(most_frequent_letter)
    second_most_frequent_index = alphabet.index(second_most_frequent_letter)

    # Calculate the shift between the most frequent and second most frequent letters
    shift = (most_frequent_index - second_most_frequent_index) % 26

    # Find 'a' and 'b' based on the calculated shift
    a = mod_inverse(shift, 26)
    b = (alphabet.index(most_frequent_letter) - (a * most_frequent_index)) % 26

    return a, b


# Example usage:
cipher_text = input("Enter cipher text: ").upper()
most_frequent_letter = 'B'  # Enter the most frequent letter in the ciphertext
second_most_frequent_letter = 'U'  # Enter the second most frequent letter in the ciphertext

a, b = break_affine_cipher(cipher_text, most_frequent_letter, second_most_frequent_letter)
print("Parameters 'a' and 'b' of the affine cipher:", a, b)
