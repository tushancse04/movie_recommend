from movies import movies
from tags import tags
from ratings import ratings
import pickle
import os.path
import math
from UserMatrix import UserMatrix
from kmeans import Point, Cluster, KMeans
import random

class MovieMatrix(UserMatrix):
	def __init__(self):
		fname = 'movie_matrix.p'
		if os.path.isfile(fname):
			self.matrix = pickle.load(open( fname, "rb" ) )
			return
		matrix = {}
		mvs = movies('ds\\movies.csv')
		rats = ratings('ds\\ratings.csv')
		tgs = tags('ds\\tags.csv')
		for id in mvs.gen_mat:
			gm = mvs.gen_mat[id]
			ym = [0]*len(list(mvs.year_mat.values())[0])
			if id in mvs.year_mat:
				ym = mvs.year_mat[id]

			tm = [0]*len(list(tgs.tag_mov_mat.values())[0])
			if id in tgs.tag_mov_mat:
				tm = tgs.tag_mov_mat[id]

			rm = [0]*len(list(rats.mov_rat_mat.values())[0])
			if id in rats.mov_rat_mat:
				rm = rats.mov_rat_mat[id]
			matrix[id] = gm + ym + tm + rm

		pickle.dump(matrix, open(fname, "wb"))
		self.matrix = matrix




