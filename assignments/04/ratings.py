import pandas 
import math

class ratings:
	def __init__(self,fname):
		df = pandas.read_csv(fname)
		self.mov_rat_mat = self.get_avg_rating_matrix(df)
		self.set_user_rat_matrix(df)
	
	def set_user_rat_matrix(self,df):
		rat_mat = {}
		time_mat = {}
		rats = [0,1,2,3,4,5]
		mx = 1537799250
		for i, rat in df.iterrows():
			id = rat['userId']
			r = round(rat['rating'])
			t = rat['timestamp']

			if id not in rat_mat:
				rat_mat[id] = [0]*6
			if id not in time_mat:
				time_mat[id] = [0]*7

			r = rats.index(r)
			rat_mat[id][r] += 1

			t = int(round((mx - t)/118279105))
			time_mat[id][t] = 1
		self.time_mat = time_mat
		self.user_rat_mat = rat_mat


	def get_avg_rating_matrix(self,df):
		rat_matrix = {}
		m = df.groupby(['movieId'])['rating'].mean()
		rats = [0,1,2,3,4,5]
		for i, item in m.iteritems():
			mat = [0]*6
			r = rats.index(round(item))
			mat[r] = 1
			rat_matrix[i] = mat
		return rat_matrix