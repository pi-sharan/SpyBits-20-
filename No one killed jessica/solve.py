from pwn import *
from Crypto.Util.number import *
from Crypto.Util.strxor import strxor
from binascii import *


r = process(['python3','server.py'])

def getData(type,m=None):


	r.sendlineafter("> ",type)

	if type == b"1":

		r.sendlineafter("> ",m)

	r.recvuntil("= ")

	enc = r.recvuntil(" ",drop=True)

	r.recvuntil("= ")

	mac = r.recvline().strip()

	return enc,mac


flagEnc , flagMac = getData(b"3")

zeroEnc = getData( b"1", flagEnc[-32:] )[0][:32]

zeroMac = getData( b"1", flagMac )[1]

r.sendlineafter("> ",b"2")
r.sendlineafter("> ",flagEnc + zeroEnc )
r.sendlineafter("> ",zeroMac )

r.interactive()
