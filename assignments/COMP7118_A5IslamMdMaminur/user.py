class user:
	def __init__(self,glen):
		self.features = [[] for i in range(glen)]
		self.rated_movies = []

	def rate(self,mid,mg_map,rating):
		self.rated_movies.append(mid)
		for gid in mg_map[mid]:
			self.features[gid].append(rating)

	def matrix(self):
		mat = [sum(x)/len(x) if len(x) > 0 else 0 for i,x in enumerate(self.features)]
		return mat
