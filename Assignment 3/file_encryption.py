def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)
# Test the encryption and decryption functions
original_text = "Hello, World!"
shift_value = 3

encrypted_text = encrypt(original_text, shift_value)
decrypted_text = decrypt(encrypted_text, shift_value)

print("Original Text:", original_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)\
