import string
import random
import re

class FullVigenere:
	def __init__(self):
		self.alphabet_uppercase = list(string.ascii_uppercase)
		self.full_vigenere_array = []
		self.regex = re.compile('[^a-zA-Z]')

	def postProcessSpace(self, text, spaces=0):
		text = [text[i-spaces:i] for i in range(spaces, len(text)+spaces, spaces)]
		text = " ".join(text)
		return text

	def generate_full_vigenere_table(self):
		table = []
		for x in range(26):
			isDuplicate = True
			while isDuplicate:
				temp_alphabet = self.alphabet_uppercase
				random.shuffle(temp_alphabet)
				temp_string = ''.join(temp_alphabet)
				if temp_string not in table :
					isDuplicate = False
			table.append(temp_string)
		return table

	def encrypt_full_vigenere(self, plaintext, key, spaces=0):
		plaintext = self.regex.sub('', plaintext.lower())
		key = self.regex.sub('', key.lower())
		self.full_vigenere_array = self.generate_full_vigenere_table()
		key_len = len(key)
		result = ''

		for idx_plaintext in range(len(plaintext)):
			idx_key = idx_plaintext % key_len
			vigenere_column = string.ascii_lowercase.index(plaintext[idx_plaintext])
			vigenere_row = string.ascii_lowercase.index(key[idx_key])
			
			result += self.full_vigenere_array[vigenere_row][vigenere_column]
		
		if spaces :
			result = self.postProcessSpace(result, spaces)

		return result

	def decrypt_full_vigenere(self, ciphertext, key, spaces=0):
		ciphertext = self.regex.sub('', ciphertext.upper())
		key = self.regex.sub('', key.lower())
		key_len = len(key)
		result = ''

		for idx_ciphertext in range(len(ciphertext)):
			idx_key = idx_ciphertext % key_len
			idx_row = string.ascii_lowercase.index(key[idx_key])
			vigenere_row = self.full_vigenere_array[idx_row]
			alphabet_idx = vigenere_row.index(ciphertext[idx_ciphertext])
			
			result += string.ascii_lowercase[alphabet_idx]
		
		if spaces :
			result = self.postProcessSpace(result, spaces)

		return result

# fv = FullVigenere()
# ciphertext = fv.encrypt_full_vigenere('Kr9y_ ptOcobacoba', 'coba.', 5)
# print(ciphertext)
# print(fv.full_vigenere_array)
# plaintext = fv.decrypt_full_vigenere(ciphertext, 'coba.', 5)
# print(plaintext)