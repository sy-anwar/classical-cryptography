import string
import re
from collections import OrderedDict

class Playfair:
	def __init__(self):
		self.regex = re.compile('[^a-zA-Z]')
		self.regex_without_j = re.compile('[^a-ik-zA-IK-Z]')

	def postProcessSpace(self, text, spaces=0):
		text = [text[i-spaces:i] for i in range(spaces, len(text)+spaces, spaces)]
		text = " ".join(text)
		return text

	def generate_key_matrix(self, key) :
		result = [['' for j in range(5)] for i in range(5)]
		key = self.regex_without_j.sub('', key.upper())
		key = list(OrderedDict.fromkeys(key).keys())

		idx_key = 0
		idx_alphabet = 0
		for i in range(5) :
			for j in range(5) :
				if idx_key < len(key) :
					result[i][j] = key[idx_key]
					idx_key += 1
				else :
					while string.ascii_uppercase[idx_alphabet] in key or string.ascii_uppercase[idx_alphabet] == 'J':
						idx_alphabet += 1
					result[i][j] = string.ascii_uppercase[idx_alphabet]
					idx_alphabet += 1

		return result

	def search_indices(self, key_matrix, char) :
		idx_row = 0
		while char not in key_matrix[idx_row] :
			idx_row += 1
		idx_collumn = key_matrix[idx_row].index(char)
		
		return idx_row, idx_collumn

	def encrypt_playfair(self, plaintext, key, spaces=0) :
		result = ''
		key_matrix = self.generate_key_matrix(key)
		
		plaintext = self.regex.sub('', plaintext.upper())
		plaintext = plaintext.replace('J', 'I')
		
		idx_plaintext = 0
		while idx_plaintext < len(plaintext) - 1 :
			if plaintext[idx_plaintext] == plaintext[idx_plaintext+1] :
				plaintext = plaintext[:idx_plaintext+1] + 'X' + plaintext[idx_plaintext+1:]
				idx_plaintext += 1
			idx_plaintext += 1
		
		if len(plaintext) % 2 == 1 :
			plaintext += 'X'

		idx_plaintext = 0
		while idx_plaintext < len(plaintext) - 1 :
			first = plaintext[idx_plaintext]
			second = plaintext[idx_plaintext+1]

			idx_row_first, idx_col_first = self.search_indices(key_matrix, first)
			idx_row_second, idx_col_second = self.search_indices(key_matrix, second)

			if (idx_row_first == idx_row_second) :
				first_after_encrypt = key_matrix[idx_row_first][(idx_col_first+1) % 5]
				second_after_encrypt = key_matrix[idx_row_second][(idx_col_second+1) % 5]
			elif (idx_col_first == idx_col_second) :
				first_after_encrypt = key_matrix[(idx_row_first+1) % 5][idx_col_first]
				second_after_encrypt = key_matrix[(idx_row_second+1) % 5][idx_col_second]
			else :
				first_after_encrypt = key_matrix[idx_row_first][idx_col_second]
				second_after_encrypt = key_matrix[idx_row_second][idx_col_first]
			
			result += first_after_encrypt + second_after_encrypt
			idx_plaintext +=2	
		
		if spaces:
			result = self.postProcessSpace(result, spaces)

		return result

	def decrypt_playfair(self, chipertext, key, spaces=0) :
		result = ''
		chipertext = self.regex.sub('', chipertext.upper())

		if len(chipertext) % 2 == 1 :
			return 'tidak dapat didekripsi dengan playfair'

		key_matrix = self.generate_key_matrix(key)
		idx_chipertext = 0

		while idx_chipertext < len(chipertext) - 1 :
			first = chipertext[idx_chipertext]
			second = chipertext[idx_chipertext+1]

			idx_row_first, idx_col_first = self.search_indices(key_matrix, first)
			idx_row_second, idx_col_second = self.search_indices(key_matrix, second)

			if (idx_row_first == idx_row_second) :
				first_after_decrypt = key_matrix[idx_row_first][(idx_col_first-1) % 5]
				second_after_decrypt = key_matrix[idx_row_second][(idx_col_second-1) % 5]
			elif (idx_col_first == idx_col_second) :
				first_after_decrypt = key_matrix[(idx_row_first-1) % 5][idx_col_first]
				second_after_decrypt = key_matrix[(idx_row_second-1) % 5][idx_col_second]
			else :
				first_after_decrypt = key_matrix[idx_row_first][idx_col_second]
				second_after_decrypt = key_matrix[idx_row_second][idx_col_first]
			
			result += first_after_decrypt + second_after_decrypt
			idx_chipertext +=2

		if spaces:
			result = self.postProcessSpace(result, spaces)

		return result.lower()

# pf = Playfair()
# chipertext = pf.encrypt_playfair('apa aja ya', 'testing', 5)
# print(chipertext)
# plaintext = pf.decrypt_playfair(chipertext, 'testing', 5)
# print(plaintext)
