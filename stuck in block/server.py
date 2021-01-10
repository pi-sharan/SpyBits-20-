from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import *
from secret import flag

key = flag[:32]

iv = b"--Go_Corona_Go--"

def encrypt(m):

	xor = lambda a,b : long_to_bytes(bytes_to_long(a)^bytes_to_long(b))

	cipher = AES.new(key,AES.MODE_ECB)

	prevCipherBlock = iv

	ciphertext = b""

	for i in range(0,len(m)//16):

		enc = cipher.encrypt(prevCipherBlock)

		currCipherBlock = xor(m[ i*16 : (i+1)*16 ] , enc )

		ciphertext += currCipherBlock

		prevCipherBlock = currCipherBlock

	return ciphertext.hex()


def main():

	print("Hey, happy to see you hacking.\n".center(100))
	print("Let's begin. We'll give you only the encryption service this time.\n")


	while True:

		print("1. Encryption")
		print("2. Get encrypted flag")
		print("3. Exit")

		try:

			type = int(input("\nGive your choice now > ").strip())

			if type == 1:

				message = input("Enter your message > ").strip()

				ciphertext = encrypt(pad(message.encode(),16))

				print("Here, take it > {}\n".format(ciphertext))

			elif type == 2:


				ciphertext = encrypt(pad(flag,16))

				print("Take the super encrypted flag > {}\n".format(ciphertext))


			else:

				print("\nOk . Bye !!")
				break
		except:

			print("\nWrong choice. Bye !!")
			break


if __name__ == '__main__':
	main()
