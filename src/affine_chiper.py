from math import gcd as bltin_gcd
import string
import re
import sympy

class AffineChiper:
	def __init__(self):
		self.regex = re.compile('[^a-zA-Z]')	

	def isCoprime(self, a, b):
		return bltin_gcd(a, b) == 1

	def postProcessSpace(self, text, spaces=0):
		text = [text[i-spaces:i] for i in range(spaces, len(text)+spaces, spaces)]
		text = " ".join(text)
		return text
		
	def encrypt_affine(self, plaintext, m, b, spaces=0):
		if not self.isCoprime(m, 26) :
			return 'm tidak relative prima dengan 26'

		plaintext = self.regex.sub('', plaintext.lower())	
		result = ''
		
		for i in range(len(plaintext)) :
			alphabet_idx = string.ascii_lowercase.index(plaintext[i])
			alphabet_idx_encrypted = ((m * alphabet_idx) + (b % 26)) % 26
			result += string.ascii_uppercase[alphabet_idx_encrypted]
		if spaces :		
			result = self.postProcessSpace(result, spaces)
		return result

	def decrypt_affine(self, chipertext, m, b, spaces=0) :
		if not self.isCoprime(m, 26) :
			return 'm tidak relative prima dengan 26'

		chipertext = self.regex.sub('', chipertext.upper())	
		result = ''
		m_inverse = sympy.mod_inverse(m, 26)
		
		for i in range(len(chipertext)) :
			alphabet_idx = string.ascii_uppercase.index(chipertext[i])
			alphabet_idx_decrypted = (m_inverse * (alphabet_idx - b)) % 26

			result += string.ascii_lowercase[alphabet_idx_decrypted]
		if spaces :
			result = self.postProcessSpace(result, spaces)
		return result

# af = AffineChiper()
# chipertext = af.encrypt_affine('yuk coba tuh', 7, 10)
# print(chipertext)
# plaintext = af.decrypt_affine(chipertext, 7, 10)
# print(plaintext)


