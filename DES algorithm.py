from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def generate_keys(key):
    """Generate 16 keys using the appropriate shift schedule."""
    keys = []
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    pc2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    key = [key[i - 1] for i in pc1]  # Permuted Choice 1
    c = key[:28]  # Left half of key
    d = key[28:]  # Right half of key

    # Generate 16 subkeys
    for i in range(16):
        c = shift_left(c, i + 1)
        d = shift_left(d, i + 1)
        cd = c + d
        keys.append([cd[j - 1] for j in pc2])  # Permuted Choice 2

    return keys

def shift_left(lst, round):
    """Perform a circular left shift on the list."""
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    shift_amount = shifts[round - 1]
    return lst[shift_amount:] + lst[:shift_amount]

def decrypt_message(ciphertext, key):
    """Decrypt the message using DES algorithm."""
    keys = generate_keys(key)

    # Reverse the order of the keys
    keys = keys[::-1]

    cipher = DES.new(bytes(key), DES.MODE_ECB)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    key = "0123456789ABCDEF"  # Example key
    ciphertext = b'\xfd\x99\x1d\x3f\x15\xc6\xe3\x53'  # Example ciphertext

    # Decrypt the ciphertext
    plaintext = decrypt_message(ciphertext, key)
    print("Decrypted plaintext:", plaintext.decode())

if __name__ == "__main__":
    main()
