import string
import random
import re

alphabet_uppercase = list(string.ascii_uppercase)
full_vigenere_array = []
regex = re.compile('[^a-zA-Z]')

def generate_full_vigenere_table():
	table = []
	for x in range(26):
		isDuplicate = True
		while isDuplicate:
			temp_alphabet = alphabet_uppercase
			random.shuffle(temp_alphabet)
			temp_string = ''.join(temp_alphabet)
			if temp_string not in table :
				isDuplicate = False
		table.append(temp_string)
	return table

def encrypt_full_vigenere(plaintext, key):
	global full_vigenere_array
	
	plaintext = regex.sub('', plaintext.lower())
	key = regex.sub('', key.lower())
	full_vigenere_array = generate_full_vigenere_table()
	key_len = len(key)
	result = ''

	for idx_plaintext in range(len(plaintext)):
		idx_key = idx_plaintext % key_len
		vigenere_column = string.ascii_lowercase.index(plaintext[idx_plaintext])
		print(vigenere_column)
		vigenere_row = string.ascii_lowercase.index(key[idx_key])
		print(vigenere_row)

		result += full_vigenere_array[vigenere_row][vigenere_column]
	
	return result

def decrypt_full_vigenere(ciphertext, key):
	key = regex.sub('', key.lower())
	key_len = len(key)
	result = ''

	for idx_ciphertext in range(len(ciphertext)):
		idx_key = idx_ciphertext % key_len
		idx_row = string.ascii_lowercase.index(key[idx_key])
		vigenere_row = full_vigenere_array[idx_row]
		alphabet_idx = vigenere_row.index(ciphertext[idx_ciphertext])
		
		result += string.ascii_lowercase[alphabet_idx]
	
	return result

ciphertext = encrypt_full_vigenere('Kr9y_ ptO', 'coba.')
print(ciphertext)
plaintext = decrypt_full_vigenere(ciphertext, 'coba.')
print(plaintext)