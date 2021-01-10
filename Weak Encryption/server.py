from Crypto.Util.number import *
from secret import flag

flag=bytes_to_long(flag.encode())


def genkey():
	p=getPrime(512)
	q=getPrime(512)
	N=p*q
	phi=(p-1)*(q-1)
	e=0x10001
	d=inverse(e,phi)
	assert GCD(e,phi)==1
	return N,e,d,pow(flag,e,N)

def main():

	N,e,d,c=genkey()
	print("Welcome to our secret RSA service.\n".center(100))
	print("Due to the corona virus epidemic, We are hiding our modulus but can your the public exponent = 0x10001.\n")
	print("Here's our secret Message : 0x{:x}\n".format(c))
	while True:
		print("1. Encryption")
		print("2. Decryption")
		print("Give me choice > ",end="")

		try:
			type=int(input())
		except:
			print("\nOops! That was not allowed number. Exiting!!")
			break

		if type==1:
			try:
				m=int(input("\nGive me your message > "))
			except:
				print("\nNeed an integer number. Exiting!!")
				break
			ct=pow(m%N,e,N)
			print("\nHere's your encrypted message : 0x{:x}\n".format(ct))


		elif type==2:
			try:
				ct=int(input("\nGive me the ciphertext > "))
			except:
				print("\nNeed an integer number. Exiting!!")
				break
			if ct==c:
				print("\nNo.Thats not allowed. Exiting!!")
				break

			m=pow(ct%N,d,N)
			print("\nHere's your message : 0x{:x}\n".format(m))

		else:
			print("\nWrong Choice. Exiting!!")
			break

if __name__ == '__main__':
	main()
