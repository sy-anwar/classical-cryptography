import string, math
from vigenere_standard import VigenereStandard

class SuperEncription:
    def __init__(self):
        self._vigenere = VigenereStandard()
        self.key = ""
        self.plaintext = ""
        self.ciphertext = ""

    def _postprocess_encrypt(self, spaces=0):
        if spaces == 0:
            return
        ciphertext = self.ciphertext
        self.ciphertext = [ciphertext[i-spaces:i] for i in range(spaces, len(ciphertext)+spaces, spaces)]
        self.ciphertext = " ".join(self.ciphertext)

    def encrypt(self, key, plaintext, spaces, n_transposition):
        ct_vg = self._vigenere.encrypt(key, plaintext, 0)

        ciphertext_group = [ct_vg[i-n_transposition:i] for i in range(n_transposition, len(ct_vg)+n_transposition, n_transposition)]
        self.ciphertext = ""
        for i in range(n_transposition):
            for cipher in ciphertext_group:
                try:
                    self.ciphertext += cipher[i]
                except IndexError:
                    pass

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

    def decrypt(self, key, ciphertext, spaces, n_transposition):
        self._preprocess_decrypt(key, ciphertext)

        n_group =  math.ceil(len(self.ciphertext) / n_transposition)
        mod = len(self.ciphertext) % n_transposition
        ciphertext_group = [ "" for i in range(n_group)]
        
        count = 0
        for c in self.ciphertext:
            if count == n_group -1:
                if mod > 0:
                    ciphertext_group[count] += c
                    mod -=1
                else:
                    count = 0
                    ciphertext_group[count] += c
            else:
                ciphertext_group[count] += c

            count += 1
            if count == n_group:
                count = 0

        self.ciphertext = "".join(ciphertext_group).replace(" ", "")
        self.plaintext = self._vigenere.decrypt(self.key, self.ciphertext, spaces)

        return self.plaintext