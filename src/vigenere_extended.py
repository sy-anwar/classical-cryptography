import string

class VigenereExtended:
    def __init__(self):
        self.key = ""
        self.plaintext = ""
        self.ciphertext = ""  

    def _generate_key_encrypt(self):
        if len(self.key) >= len(self.plaintext):
            return
        key = self.key
        for i in range(len(self.plaintext) - len(key)):
            self.key += key[i % len(key)]

    def _postprocess_encrypt(self, spaces=0):
        if spaces == 0:
            return
        ciphertext = self.ciphertext
        self.ciphertext = [ciphertext[i-spaces:i] for i in range(spaces, len(ciphertext)+spaces, spaces)]
        self.ciphertext = " ".join(self.ciphertext)

    def encrypt(self, key, plaintext, spaces):
        self.key = key
        self.plaintext = plaintext
        self._generate_key_encrypt()

        self.ciphertext = ""
        for i in range(len(self.plaintext)):
            ch = (ord(self.plaintext[i]) + ord(self.key[i])) % 256
            if not chr(ch).isprintable():
                self.ciphertext += '\\' + hex(ch)[1:]
            else:
                self.ciphertext += chr(ch)

        self._postprocess_encrypt(spaces)

        return self.ciphertext

    def _generate_key_decrypt(self):
        if len(self.key) >= len(self.ciphertext):
            return
        key = self.key
        for i in range(len(self.ciphertext) - len(key)):
            self.key += key[i % len(key)]

    def _postprocess_decrypt(self, spaces=0):
        if spaces == 0:
            return
        plaintext = self.plaintext
        self.plaintext = [plaintext[i-spaces:i] for i in range(spaces, len(plaintext)+spaces, spaces)]
        self.plaintext = " ".join(self.plaintext)

    def decrypt(self, key, ciphertext, spaces):
        self.key = key
        self.ciphertext = ciphertext
        self._generate_key_decrypt()

        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            ch = (ord(self.ciphertext[i]) - ord(self.key[i]) + 256) % 256
            self.plaintext += chr(ch)

        self._postprocess_decrypt(spaces)

        return self.plaintext