import random
from bloom_filter import BloomFilter
class DNA:
	def __init__(self):
		pass

	def gen_dna(self,L):
		dna = ''
		for i in range(L):
			dna += random.choice('ACGT')
		return dna

	def dnalist(self,L,N):
		l = []
		for i in range(N):
			l.append(self.gen_dna(L))
		return l

	def evaluate_bloom_filter(self):
		L = 100
		train_n = 10000
		prob = .001
		dna = DNA()
		train_dnalist = dna.dnalist(L,train_n)
		bf = BloomFilter(train_dnalist,prob)

		test_n = 2000
		test_dnalist = dna.dnalist(L,test_n)
		bf.test_bloom_filter(test_dnalist)




