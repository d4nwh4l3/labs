class Caesar:
    def __init__(self, key=0):
        self._key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    def set_key(self, key):
        self._key = key

    def encrypt(self, plaintext):
        return self._shift_text(plaintext, self._key)

    def decrypt(self, ciphertext):
        return self._shift_text(ciphertext, -self._key)

    def _shift_text(self, text, shift):
        result = []
        for char in text:
            if char.isalpha():
                shifted_char = self._shift_char(char.lower(), shift)
                result.append(shifted_char)
            elif char.isspace():
                result.append(char)
            else:
                shifted_char = self._shift_special_char(char, shift)
                result.append(shifted_char)
        return ''.join(result)

    def _shift_char(self, char, shift):
        base = ord('a')
        shifted = (ord(char) - base + shift) % 26 + base
        return chr(shifted)

    def _shift_special_char(self, char, shift):
        shifted = (ord(char) + shift) % 128
        return chr(shifted)