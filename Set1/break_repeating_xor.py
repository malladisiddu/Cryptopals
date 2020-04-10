from base64 import b64decode as b264

def hammming_distance(plaintext1,plaintext2):
#Hamming distance is the measure of difference between two strings i.e., no. of differing bits between given two strings
	hamming_distance = 0
#zip enables us to compare the corresponding bits
#by xoring we can find the differing bits since xor of two unequals is 1
	for b1,b2 in zip(plaintext1,plaintext2):
		difference = ord(b1) ^ ord(b2)
		#count the number of 1's in the differnce
		hamming_distance += sum([1 for bit in bin(ord(difference)) if bit == '1'])
	return hamming_distance

	
