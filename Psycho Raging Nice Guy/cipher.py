class PRNG:

	def __init__(self,key):

		self.key = key

		self.N = 16

		self.lfsr = [0]*self.N

		self.index = [ 2, 3, 5, 7, 11, 13, 15 ]

		for i in range(self.N):

			for j in range(self.N):

				self.lfsr[ (i+j)%self.N ] ^= ( key >> (i*self.N) + j ) & 1


		for i in range(0x100):

			xor = 0

			for j in self.index:

				xor ^= self.lfsr[j]

			self.lfsr = [xor] + self.lfsr[:-1]





	def generateBit(self):

		xor = 0

		for j in self.index:

			xor ^= self.lfsr[j]

		self.lfsr = [xor] + self.lfsr[:-1]

		return xor

