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


def encrypt_affine_caesar(a, b, plain_text):
    """
    Encrypt the plain text using the affine Caesar cipher with given parameters a and b.
    """
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                char_index = ord(char) - ord('A')
                cipher_index = (a * char_index + b) % 26
                cipher_text += chr(cipher_index + ord('A'))
            elif char.islower():
                char_index = ord(char) - ord('a')
                cipher_index = (a * char_index + b) % 26
                cipher_text += chr(cipher_index + ord('a'))
        else:
            cipher_text += char
    return cipher_text


# Example usage:
a = 5  # Choose a value for 'a'
b = 8  # Choose a value for 'b'
plain_text = input("Enter plain text: ")
cipher_text = encrypt_affine_caesar(a, b, plain_text)
print("Cipher text:", cipher_text)
