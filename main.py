def encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
plaintext = "Hello, World!"
shift = 3

# Encrypt the plaintext
encrypted_text = encrypt(plaintext, shift)
print("Encrypted text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
