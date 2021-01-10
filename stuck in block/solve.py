from pwn import *
from binascii import *
import string

#r=process(['python3','server.py'])
r=remote('18.204.91.223',5002)

def getciphertext(m):

	r.sendline("1")

	r.sendline(m)

	r.recvuntil("take it > ")

	return unhexlify(r.recvline().strip())

r.sendline("2")
r.recvuntil("flag > ")

encFlag = unhexlify(r.recvline().strip())

flag=b""

charSet = string.printable

while True:

	for i in string.printable:
		if encFlag[len(flag)]==getciphertext(flag+i.encode())[len(flag)]:
			flag+=i.encode()
			print(flag)
			break

	if flag[-1]==ord("}"):
		break
