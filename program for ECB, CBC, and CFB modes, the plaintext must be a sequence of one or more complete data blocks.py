from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_ECB(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_ECB(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext

def encrypt_CBC(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_CBC(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext

def encrypt_CFB(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_CFB(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    # Example plaintext and key
    plaintext = b"This is a secret message."
    key = get_random_bytes(16)  # 16 bytes for AES key
    iv = get_random_bytes(16)   # 16 bytes for AES IV

    # ECB mode
    print("ECB Mode:")
    ciphertext_ecb = encrypt_ECB(plaintext, key)
    decrypted_plaintext_ecb = decrypt_ECB(ciphertext_ecb, key)
    print("Plaintext:", plaintext)
    print("Ciphertext (ECB):", ciphertext_ecb)
    print("Decrypted plaintext (ECB):", decrypted_plaintext_ecb)

    # CBC mode
    print("\nCBC Mode:")
    ciphertext_cbc = encrypt_CBC(plaintext, key, iv)
    decrypted_plaintext_cbc = decrypt_CBC(ciphertext_cbc, key, iv)
    print("Plaintext:", plaintext)
    print("Ciphertext (CBC):", ciphertext_cbc)
    print("Decrypted plaintext (CBC):", decrypted_plaintext_cbc)

    # CFB mode
    print("\nCFB Mode:")
    ciphertext_cfb = encrypt_CFB(plaintext, key, iv)
    decrypted_plaintext_cfb = decrypt_CFB(ciphertext_cfb, key, iv)
    print("Plaintext:", plaintext)
    print("Ciphertext (CFB):", ciphertext_cfb)
    print("Decrypted plaintext (CFB):", decrypted_plaintext_cfb)

if __name__ == "__main__":
    main()
