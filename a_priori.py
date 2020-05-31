# A Priori Algorithm for finding frequent item sets

DATA_FILE = 'datasets/retail.txt'

#-------------------------------------------------------------
def get_baskets(filename):
	baskets = []
	with open(filename) as f:
		for line in f:
			items = line.strip().split(' ')
			baskets.append([ int(i) for i in items ])
	return baskets

#-------------------------------------------------------------
def fis1(baskets, threshold):
	freq = {}
	frequent_items = {}
	for basket in baskets:
		for item in basket:
			if item not in freq:
				freq[item] = 0
			freq[item] += 1
			if freq[item] > threshold:
				frequent_items[item] = freq[item]
	return freq, frequent_items

#-------------------------------------------------------------
def fis2(baskets, f1, threshold):
	freq = {}
	frequent_items = {}
	for basket in baskets:
		for i in range(len(basket)):
			for j in range(i+1, len(basket)):
				if basket[i] in f1 and basket[j] in f1:
					a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
					if (a,b) not in freq:
						freq[(a,b)] = 0
					freq[(a,b)] += 1
					if freq[(a,b)] > threshold:
						frequent_items[(a,b)] = freq[(a,b)]
	return freq, frequent_items
#-------------------------------------------------------------

def a_priori(filename):
	#-------------------------------------------------------------
	# PHASE 1
	#-------------------------------------------------------------
	Baskets = get_baskets(filename)
	t = 0.001 * len(Baskets)

	print('Phase 1 begins')
	Freq_1, FIS_1 = fis1(Baskets, t)
	for k,v in FIS_1.items():
		print(k,v)
	print('There are', len(FIS_1), 'sets.')

	#-------------------------------------------------------------
	# PHASE 2
	#-------------------------------------------------------------
	print('Phase 2 begins')
	Freq_2, FIS_2 = fis2(Baskets, FIS_1, t)
	for k, v in FIS_2.items():
		print(k, v)
	print('There are', len(FIS_2), 'sets.')
#-------------------------------------------------------------


a_priori(DATA_FILE)



#-------------------------------------------------------------
# print('Confidence({48} -> 334', FIS_2[(48,334)] / FIS_1[48] )
# print('Confidence({334} -> 48', FIS_2[(48,334)] / FIS_1[334] )