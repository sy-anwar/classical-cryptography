import string

class VigenereStandard:
    def __init__(self):
        self.key = ""
        self.plaintext = ""
        self.ciphertext = ""
    
    def _preprocess_encrypt(self, key, plaintext):
        # omits numbers
        plaintext = "".join([i for i in plaintext if not i.isdigit()])
        key = "".join([i for i in key if not i.isdigit()])
        # omits spaces
        plaintext = plaintext.replace(" ", "")
        key = key.replace(" ", "")
        # omits punctuation
        plaintext = plaintext.translate(str.maketrans("","", string.punctuation))
        key = key.translate(str.maketrans("","", string.punctuation))
        # capitalize letters
        self.plaintext = plaintext.upper()
        self.key = key.upper()        

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
        self._preprocess_encrypt(key, plaintext)
        self._generate_key_encrypt()

        self.ciphertext = ""
        for i in range(len(self.plaintext)):
            ch = (ord(self.plaintext[i]) + ord(self.key[i])) % 26 + ord("A")
            self.ciphertext += chr(ch)

        self._postprocess_encrypt(spaces)

        return self.ciphertext

    def _preprocess_decrypt(self, key, ciphertext):
        # omits numbers
        ciphertext = "".join([i for i in ciphertext if not i.isdigit()])
        key = "".join([i for i in key if not i.isdigit()])
        # omits spaces
        ciphertext = ciphertext.replace(" ", "")
        key = key.replace(" ", "")
        # omits punctuation
        ciphertext = ciphertext.translate(str.maketrans("","", string.punctuation))
        key = key.translate(str.maketrans("","", string.punctuation))
        # capitalize letters
        self.ciphertext = ciphertext.upper()
        self.key = key.upper()        

    def _generate_key_decrypt(self):
        if len(self.key) >= len(self.ciphertext):
            return
        key = self.key
        for i in range(len(self.ciphertext) - len(key)):
            if self.ciphertext[i] != " ":
                self.key += key[i % len(key)]
            else:
                self.key += " "

    def _postprocess_decrypt(self, spaces=0):
        if spaces == 0:
            return
        plaintext = self.plaintext
        self.plaintext = [plaintext[i-spaces:i] for i in range(spaces, len(plaintext)+spaces, spaces)]
        self.plaintext = " ".join(self.plaintext)

    def decrypt(self, key, ciphertext, spaces):
        self._preprocess_decrypt(key, ciphertext)
        self._generate_key_decrypt()

        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            if self.ciphertext[i] != " ":
                ch = (ord(self.ciphertext[i]) - ord(self.key[i]) + 26) % 26 + ord("A")
                self.plaintext += chr(ch)
            else:
                self.plaintext += self.ciphertext[i]

        self._postprocess_decrypt(spaces)

        return self.plaintext