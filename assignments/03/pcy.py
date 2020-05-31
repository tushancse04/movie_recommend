# PCY Algorithm for finding frequent item sets
import count_filter
class PCY:

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
		cf = count_filter.CountPair(50000)
		for basket in baskets:
			for i in range(len(basket)):
				item = basket[i]
				if item not in freq:
					freq[item] = 0
				freq[item] += 1
				if freq[item] > threshold:
					frequent_items[item] = freq[item]

				# PCY heuristic
				for j in range(i+1, len(basket)):
					a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
					cf.add((a,b))

		return freq, frequent_items, cf

	#-------------------------------------------------------------
	def fis2(self,baskets, f1, cf, threshold):
		freq = {}
		frequent_items = {}
		cf3 = count_filter.CountTriple(50000)
		for basket in baskets:
			for i in range(len(basket)):
				for j in range(i+1, len(basket)):
					a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
					if (basket[i] in f1) and (basket[j] in f1) and cf.is_candidate((a,b),threshold):
						if (a,b) not in freq:
							freq[(a,b)] = 0
						freq[(a,b)] += 1
						if freq[(a,b)] > threshold:
							frequent_items[(a,b)] = freq[(a,b)]

						# PCY heuristic
						for k in range(j+1, len(basket)):
							l = [basket[i],basket[j],basket[k]]
							l.sort()
							a, b, c = l[0],l[1],l[2]
							cf3.add((a,b,c))

		return freq, frequent_items,cf3
	#-------------------------------------------------------------


	#-------------------------------------------------------------
	def fis3(self,baskets, f2, cf3, threshold):
		freq = {}
		frequent_items = {}
		for basket in baskets:
			for i in range(len(basket)):
				for j in range(i+1, len(basket)):
					for k in range(j+1, len(basket)):
						l = [basket[i],basket[j],basket[k]]
						l.sort()
						a, b, c = l[0],l[1],l[2]
						if ((a,b) in f2) and (b,c in f2) and (a,c in f2) and cf3.is_candidate((a,b,c),threshold):
							if (a,b,c) not in freq:
								freq[(a,b,c)] = 0
							freq[(a,b,c)] += 1
							if freq[(a,b,c)] > threshold:
								frequent_items[(a,b,c)] = freq[(a,b,c)]


		return freq, frequent_items,cf3
	#-------------------------------------------------------------

	def a_priori(self,filename,t):
		#-------------------------------------------------------------
		# PHASE 1
		#-------------------------------------------------------------
		Baskets = self.get_baskets(filename)
		t = 0.05 * len(Baskets)

		Freq_1, FIS_1, cf = self.fis1(Baskets, t)
		print('There are', len(FIS_1), ' in fis1 sets for A-Priori')

		#-------------------------------------------------------------
		# PHASE 2
		#-------------------------------------------------------------

		Freq_2, FIS_2,cf3 = self.fis2(Baskets, FIS_1, cf, t)
		print('There are', len(FIS_2), ' in fis2 sets for A-Priori ')


		Freq_3, FIS_3,cf3 = self.fis3(Baskets, FIS_2, cf3, t)
		print('There are', len(FIS_3), ' in fis3 sets for A-Priori')
		print('We only look at fewer than', len([x for x in cf3.Table if x > t]), "items for PCY.")




