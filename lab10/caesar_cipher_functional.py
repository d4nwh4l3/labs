def shift_char(char, shift):
    base = ord('a')
    shifted = (ord(char) - base + shift) % 26 + base
    return chr(shifted)

def shift_special_char(char, shift):
    shifted = (ord(char) + shift) % 128
    return chr(shifted)

def shift_text(text, shift):
    def shift_single(char):
        if char.isalpha():
            return shift_char(char.lower(), shift)
        elif char.isspace():
            return char
        else:
            return shift_special_char(char, shift)

    return ''.join(map(shift_single, text))

def encrypt(plaintext, key):
    return shift_text(plaintext, key)

def decrypt(ciphertext, key):
    return shift_text(ciphertext, -key)

def main():
    key = 3
    plaintext = "Hello, World!"
    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)

    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
