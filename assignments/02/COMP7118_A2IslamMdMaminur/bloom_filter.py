import numpy as np
import math
import random
from bitarray import bitarray

class BloomFilter:
	def __init__(self,dnalist,prob):
		self.bitarray_dna_map = {}
		n = len(dnalist)
		m = int(-n*np.log(prob)/((np.log(2))**2))
		self.n = n
		self.m = self.next_prime(m)
		k = int(m*np.log(2)/n)
		self.k = k
		self.gen_random_hash_functions()
		self.dna_bitmaps = []
		for dna in dnalist:
			self.insert_dna(dna)

	def insert_dna(self,dna):
		bitmap = self.gen_bitmap(dna)
		self.bitarray_dna_map[str(bitmap)] = dna
		self.dna_bitmaps.append(bitmap)

	def gen_bitmap(self,dna):
		a = bitarray('0'*self.m)
		for i in range(self.k):
			a[self.hash_fs[i](dna)] = 1
		return a

	def is_viral(self,dna):
		bitmap = self.gen_bitmap(dna)
		for bm in self.dna_bitmaps:
			if bm == bitmap:
				return True
		return False
	def test_bloom_filter(self,test_dna_list):
		c = 0
		for i,dna in enumerate(test_dna_list):
			if self.is_viral(dna):
				bitmap = self.gen_bitmap(dna)
				if self.bitarray_dna_map[str(bitmap)] == dna:
					c += 1
		print('False positive prob : ',c/len(test_dna_list))




	


	def random_dna(self,L):
		dna = ''
		for i in range(L):
			dna += random.choice('ACGT')
		return dna

	def next_prime(self,m):
		n = m
		while True:
			rt = int(math.sqrt(m))
			isprime = True
			for i in range(2,rt+1):
				if (n%i) == 0:
					isprime = False
					break
			if isprime:
				return n
			n += 1

	def gen_random_hash_functions(self):
		fs = []
		m,k = self.m, self.k
		for i in range(k):
			hf = self.random_hash_function(m)
			fs.append(hf)
		self.hash_fs = fs


	def random_hash_function(self,m):
		p = self.next_prime(m)
		a = random.randint(1, m)
		b = random.randint(1, m)
		d = {'A':0,'C':1,'G':2,'T':3}
		def f(dna):
			v = 0
			for c in dna:
				v = (v*4*a + d[c]*b)%p
			return v%m
		return f







