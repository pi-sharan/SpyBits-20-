from cipher import PRNG
from Crypto.Random.random import *
from secret import flag

print("Hey, this is the my stream cipher for secure encryption. Try to hack it.\n")

key = getrandbits(256)

Cipher = PRNG(key)


def  encrypt(m):

	enc = ""

	for i in m:

		encV = 0

		for _ in range(8):

			encV = (encV<<1) | Cipher.generateBit()

		encblock = hex( i ^ encV )[2:].zfill(2)

		enc += encblock


	return enc


while True:

	print("1. Encryption")
	print("2. Get Flag (encrypted)")
	print("3. Exit")

	try:

		type = int(input("\nGive me what do want to do > ").strip())

		if type == 1:

			m = input("Give your message buddy > ").strip().encode()

			print("Here's your message : {}".format(encrypt(m)))

		elif type == 2:

			print("Here's your encrypted flag : {}".format(encrypt(flag)))

		else:

			print("Ok..Bye!!\n")
			break
	except:

		print("Error occured. Exiting!!\n")
		break

