from math import gcd as bltin_gcd
import string
import re
import sympy

regex = re.compile('[^a-zA-Z]')

def isCoprime(a, b):
    return bltin_gcd(a, b) == 1

def encrypt_affine(plaintext, m, b):
	if not isCoprime(m, 26) :
		return 'm tidak relative prima dengan 26'

	plaintext = regex.sub('', plaintext.lower())	
	result = ''

	for i in range(len(plaintext)) :
		alphabet_idx = string.ascii_lowercase.index(plaintext[i])
		alphabet_idx_encrypted = ((m * alphabet_idx) + (b % 26)) % 26

		result += string.ascii_uppercase[alphabet_idx_encrypted]
	
	return result

def decrypt_affine(chipertext, m, b) :
	if not isCoprime(m, 26) :
		return 'm tidak relative prima dengan 26'

	chipertext = regex.sub('', chipertext.upper())	
	result = ''
	m_inverse = sympy.mod_inverse(m, 26)
	
	for i in range(len(chipertext)) :
		alphabet_idx = string.ascii_uppercase.index(chipertext[i])
		alphabet_idx_decrypted = (m_inverse * (alphabet_idx - b)) % 26

		result += string.ascii_lowercase[alphabet_idx_decrypted]
	
	return result

chipertext = encrypt_affine('yuk coba tuh', 7, 10)
print(chipertext)
plaintext = decrypt_affine(chipertext, 7, 10)
print(plaintext)


