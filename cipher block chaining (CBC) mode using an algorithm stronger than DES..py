from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_CBC_3DES(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode(), DES3.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def main():
    # Example plaintext, key, and initialization vector (IV)
    plaintext = "This is a secret message."
    key = get_random_bytes(24)  # 24 bytes for 3DES key
    iv = get_random_bytes(8)    # 8 bytes for DES IV

    # Encrypt using CBC mode with 3DES
    ciphertext = encrypt_CBC_3DES(plaintext, key, iv)

    print("Plaintext:", plaintext)
    print("Key:", key)
    print("IV:", iv)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
