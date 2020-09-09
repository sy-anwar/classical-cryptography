import string, math, numpy
from sympy import Matrix

class HillCipher:
    def __init__(self):
        self.key = ""
        self.plaintext = ""
        self.ciphertext = ""
        self.n_col = 0
        self.key_matrix = []
        self.inverse_key_matrix = []
        self.invertible = False
    
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

    def _generate_key(self):
        self.n_col = int(math.sqrt(len(self.key)))
        self.key_matrix = [[0]* self.n_col for i in range(self.n_col)]
        k = 0
        for i in range(self.n_col):
            for j in range(self.n_col):
                self.key_matrix[i][j] = ord(self.key[k]) % 65
                k += 1
        self.key_matrix = numpy.array(self.key_matrix)
        try:
            self.inverse_key_matrix = numpy.linalg.inv(self.key_matrix)
            self.invertible = True
        except numpy.linalg.LinAlgError:
            self.invertible = False

    def _postprocess_encrypt(self, spaces=0):
        if spaces == 0:
            return
        ciphertext = self.ciphertext
        self.ciphertext = [ciphertext[i-spaces:i] for i in range(spaces, len(ciphertext)+spaces, spaces)]
        self.ciphertext = " ".join(self.ciphertext)

    def encrypt(self, key, plaintext, spaces):
        self._preprocess_encrypt(key, plaintext)
        self._generate_key()

        if not self.invertible:
            return "Key Not Invertible"

        plaintext_group = [self.plaintext[i-self.n_col:i] for i in range(self.n_col, len(self.plaintext)+self.n_col, self.n_col)]
        
        self.ciphertext = ""
        for text in plaintext_group:
            plaintext_matrix = numpy.array([ord(text[i]) % 65 for i in range(len(text))])
            cipher_number = (self.key_matrix.dot(plaintext_matrix) % 26).tolist()
            self.ciphertext += "".join([chr(num + ord('A')) for num in cipher_number])

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

    def _postprocess_decrypt(self, spaces=0):
        if spaces == 0:
            return
        plaintext = self.plaintext
        self.plaintext = [plaintext[i-spaces:i] for i in range(spaces, len(plaintext)+spaces, spaces)]
        self.plaintext = " ".join(self.plaintext)

    def decrypt(self, key, ciphertext, spaces):
        self._preprocess_decrypt(key, ciphertext)
        self._generate_key()

        if not self.invertible:
            return "Key Not Invertible"

        ciphertext_group = [self.ciphertext[i-self.n_col:i] for i in range(self.n_col, len(self.ciphertext)+self.n_col, self.n_col)]
        self.inverse_key_matrix = numpy.array(Matrix(self.key_matrix).inv_mod(26).tolist())

        self.plaintext = ""
        for text in ciphertext_group:
            ciphertext_matrix = numpy.array([ord(text[i]) % 65 for i in range(len(text))])
            plain_number = (self.inverse_key_matrix.dot(ciphertext_matrix) % 26).tolist()
            self.plaintext += "".join([chr(num + ord('A')) for num in plain_number])

        self._postprocess_encrypt(spaces)

        return self.plaintext