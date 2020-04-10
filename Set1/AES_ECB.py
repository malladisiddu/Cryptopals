from Crypto.Cipher import AES
def aes_ecb(ciphertext,key):
# Using in built modules
	cipher = AES.new(key,AES.MODE_ECB)
# Decrypting the cipher text into plaintext
	plaintext =  cipher.decrypt(ciphertext)
	return plaintext
key = 'YELLOW SUBMARINE'
ct = open('7.txt')
ciphertext = (ct.read()).decode('base64')
flag = aes_ecb(ciphertext,key)
print 'Flag is: ',flag
