class APriori:

	def __init__(self,DATA_FILE,t):
		Baskets = self.get_baskets(DATA_FILE)
		t = 0.05 * len(Baskets)
		Freq_1, FIS_1 = self.fis1(Baskets, t)
		print('There are', len(FIS_1), ' in fis1 sets.')

		Freq_2, FIS_2 = self.fis2(Baskets, FIS_1, t)
		print('There are', len(FIS_2), ' in fis2 sets.')

		Freq_3, FIS_3 = self.fis3(Baskets, FIS_2, t)
		print('There are', len(FIS_3), ' in fis3 sets.')
		for k, v in FIS_3.items():
			print(k, v)


	#-------------------------------------------------------------
	def get_baskets(self,filename):
		baskets = []
		with open(filename) as f:
			for line in f:
				items = line.strip().split(' ')
				baskets.append([ int(i) for i in items ])
		return baskets

	#-------------------------------------------------------------
	def fis1(self,baskets, threshold):
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



	# PHASE 2
	#-------------------------------------------------------------
	def fis2(self,baskets, f1, threshold):
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



	#-------------------------------------------------------------
	# PHASE 3
	#-------------------------------------------------------------



	def fis3(self,baskets, f2, threshold):
		freq = {}
		frequent_items = {}
		for basket in baskets:
			for i in range(len(basket)):
				for j in range(i+1, len(basket)):
					for k in range(j+1):
						l = [basket[i],basket[j],basket[k]]
						l.sort()
						a,b,c = l[0],l[1],l[2]
						if (a,b) in f2 and (a,c) in f2 and (b,c) in f2:
							if (a,b,c) not in freq:
								freq[(a,b,c)] = 0
							freq[(a,b,c)] += 1
							if freq[(a,b,c)] > threshold:
								frequent_items[(a,b,c)] = freq[(a,b,c)]
		return freq, frequent_items
	#-------------------------------------------------------------



