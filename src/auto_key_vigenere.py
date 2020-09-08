import string
import re

regex = re.compile('[^a-zA-Z]')

def encrypt_auto_key_vigenere(plaintext, key):
	plaintext = regex.sub('', plaintext.lower())
	key = regex.sub('', key.lower())

	idx_plaintext = 0
	while len(key) < len(plaintext) :
		key += plaintext[idx_plaintext]
		idx_plaintext += 1
	
	print(key)
	
	result = ''

	for idx in range(len(plaintext)):
		alphabet_idx_plaintext = string.ascii_lowercase.index(plaintext[idx])
		alphabet_idx_key = string.ascii_lowercase.index(key[idx])
		alphabet_idx_after_encrypt = (alphabet_idx_plaintext + alphabet_idx_key) % 26

		result += string.ascii_uppercase[alphabet_idx_after_encrypt]
	
	return result, key

def decrypt_auto_key_vigenere(ciphertext, key):
	key = regex.sub('', key.lower())
	result = ''

	for idx in range(len(ciphertext)):
		alphabet_idx_chipertext = string.ascii_uppercase.index(ciphertext[idx])
		alphabet_idx_key = string.ascii_lowercase.index(key[idx])
		alphabet_idx_after_decrypt = (alphabet_idx_chipertext - alphabet_idx_key) % 26

		result += string.ascii_lowercase[alphabet_idx_after_decrypt]
	
	return result

ciphertext, key = encrypt_auto_key_vigenere('Kr9y_ ptO', 'coba.')
print(ciphertext, key)
plaintext = decrypt_auto_key_vigenere(ciphertext, key)
print(plaintext)