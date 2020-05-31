import pandas


def get_baskets(data_file):
	baskets = []
	ifile = open(data_file)
	for l in ifile:
		l = l.strip().split(' ')
		l = [int(i) for i in l]
		baskets.append(l)
	return baskets
	ifile.close()


def fis1(baskets,t):
	freq = {}
	candidates = {}
	for basket in baskets:
		for item in basket:
			if item not in freq:
				freq[item] = 0
			freq[item] += 1
			if freq[item] > t:
				candidates[item] = freq[item]
	return freq,candidates

data_file = 'datasets/retail_small.txt'
t = .005 * 1000
baskets = get_baskets(data_file)
freq,FIS_1 = fis1(baskets,t)
for k,v in FIS_1.items():
	print(k,v)
print(len(FIS_1))

