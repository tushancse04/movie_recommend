import pandas 



class movies:
	def __init__(self,fname):
		df = pandas.read_csv(fname)
		gen_mat = self.get_gen_matrix(df)
		year_mat = self.get_year_matrix(df)
		self.gen_mat = gen_mat
		self.year_mat = year_mat
	



	# several times iterations over the data frame done to make the code more readable
	def get_year_matrix(self,df):
		year_mat = {}
		m_x,m_n = 2018,1902
		years = [0,1,2,3,4,5]
		for i, mov in df.iterrows():
			id = mov['movieId']
			mat = [0]*6
			title = mov['title'].strip().split('(')
			if len(title) > 1:
				year = int(title[-1].split(')')[0].split('–')[0])
				year = round((m_x - year)/24.0)
				mat[years.index(year)] = 1
			year_mat[id] = mat
		return year_mat		

	def get_gen_matrix(self,df):
		gnrs = self.get_all_genres(df)
		gen_mat = {}
		for i, mov in df.iterrows():
			gnrs_mat = [0]*len(gnrs)
			mov_gnrs = mov['genres'].strip().split('|')
			for g in mov_gnrs:
				i = gnrs.index(g)
				gnrs_mat[i] = 1
			id = mov['movieId']
			gen_mat[id] = gnrs_mat
		return gen_mat



	def get_all_genres(self,df):
		gnrs = set([])
		for i, row in df.iterrows():
			cats = row['genres'].strip().split('|')
			gnrs = gnrs.union(set(cats))
		return list(gnrs)



