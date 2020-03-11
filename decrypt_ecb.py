import base64 as b264

from Crypto.Cipher import AES

def decrypt_ecb(ciphertext, key):
     cipher = AES.new(key, AES.MODE_ECB)
     plaintext = cipher.decrypt(ciphertext)
     return plaintext

key = 'YELLOW SUBMARINE'
with open('7.txt') as ct:
	ciphertext = b264.b64decode(ct.read())

flag = decrypt_ecb(ciphertext, key)

print flag
     
