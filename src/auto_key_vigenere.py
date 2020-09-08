import string
import re

class AutoKeyVigenere:
	def __init__(self):
		self.regex = re.compile('[^a-zA-Z]')

	def postProcessSpace(self, text, spaces=0):
		text = [text[i-spaces:i] for i in range(spaces, len(text)+spaces, spaces)]
		text = " ".join(text)
		return text

	def encrypt_auto_key_vigenere(self, plaintext, key, spaces=0):
		plaintext = self.regex.sub('', plaintext.lower())
		key = self.regex.sub('', key.lower())

		idx_plaintext = 0
		while len(key) < len(plaintext) :
			key += plaintext[idx_plaintext]
			idx_plaintext += 1
		
		result = ''

		for idx in range(len(plaintext)):
			alphabet_idx_plaintext = string.ascii_lowercase.index(plaintext[idx])
			alphabet_idx_key = string.ascii_lowercase.index(key[idx])
			alphabet_idx_after_encrypt = (alphabet_idx_plaintext + alphabet_idx_key) % 26

			result += string.ascii_uppercase[alphabet_idx_after_encrypt]
		
		if spaces :
			result = self.postProcessSpace(result, spaces)

		return result, key

	def decrypt_auto_key_vigenere(self, ciphertext, key, spaces=0):
		ciphertext = self.regex.sub('', ciphertext.upper())
		key = self.regex.sub('', key.lower())
		result = ''

		for idx in range(len(ciphertext)):
			alphabet_idx_chipertext = string.ascii_uppercase.index(ciphertext[idx])
			alphabet_idx_key = string.ascii_lowercase.index(key[idx])
			alphabet_idx_after_decrypt = (alphabet_idx_chipertext - alphabet_idx_key) % 26

			result += string.ascii_lowercase[alphabet_idx_after_decrypt]

		if spaces :
			result = self.postProcessSpace(result, spaces)

		return result

# ak = AutoKeyVigenere()
# ciphertext, key = ak.encrypt_auto_key_vigenere('Kr9y_ ptOUYE', 'coba.', 5)
# print(ciphertext, key)
# plaintext = ak.decrypt_auto_key_vigenere(ciphertext, key, 5)
# print(plaintext)