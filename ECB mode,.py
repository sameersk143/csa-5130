from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_CBC(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_CBC(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_plaintext, AES.block_size).decode()
    return plaintext

def main():
    # Example plaintext, key, and initialization vector (IV)
    plaintext = "This is a secret message."
    key = get_random_bytes(16)  # 16 bytes for AES key
    iv = get_random_bytes(16)   # 16 bytes for AES IV

    # Encrypt using CBC mode
    ciphertext = encrypt_CBC(plaintext, key, iv)

    # Introduce an error in the transmitted ciphertext block (e.g., flip a bit)
    # Let's assume we flipped the first bit of the first ciphertext block
    modified_ciphertext = bytearray(ciphertext)
    modified_ciphertext[0] ^= 0x01  # Flip the first bit

    # Decrypt the modified ciphertext
    decrypted_plaintext = decrypt_CBC(modified_ciphertext, key, iv)

    print("Original plaintext:", plaintext)
    print("Decrypted plaintext with error in ciphertext:", decrypted_plaintext)

if __name__ == "__main__":
    main()
