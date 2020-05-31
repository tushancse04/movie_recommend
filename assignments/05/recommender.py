from movie_data import movie_data
import os
import pickle
from matrix import Matrix
import numpy
from numpy import array
from user import user
import random

class recommender:
	def __init__(self):
		self.pickle_file = 'mat.p'
		if os.path.exists(self.pickle_file):
			self.md = pickle.load(open(self.pickle_file, "rb" ) )
		else:
			self.md = movie_data()
			pickle.dump(self.md,open(self.pickle_file,"wb"))


	def get_random_movie(self):
		m = self.md.movies.sample(n=1).values[0]
		id = m[0]
		if id not in self.md.mg_map:
			return get_random_movie()
		return m

	def finally_reco_movie(self,u):
		uf = array(u.matrix())
		mf = array(self.md.uf)
		um = uf.dot(mf.transpose())
		max_i = 0
		for i in range(len(um)):
			if um[i] > um[max_i]:
				max_i = i

		uf = array(self.md.uf[max_i])
		mf = array(self.md.mf)
		um = uf.dot(mf.transpose())
		max_i = 0
		for i in range(len(um)):
			if um[i] > um[max_i] and self.md.idx_mid_map[i]  not in u.rated_movies:
				max_i = i
				
		mid = self.md.idx_mid_map[max_i]
		m = self.md.movies[self.md.movies.movie_id == mid].values[0]
		return m

	def recommended_movie(self,u):
		uf = array(u.matrix())
		mf = array(self.md.mf)
		um = uf.dot(mf.transpose())
		max_i = 0
		for i in range(len(um)):
			if um[i] > um[max_i] and (self.md.idx_mid_map[i] not in u.rated_movies):
				max_i = i

		mid = self.md.idx_mid_map[max_i]
		u.rated_movies.append(mid)
		m = self.md.movies[self.md.movies.movie_id == mid].values[0]
		return m





