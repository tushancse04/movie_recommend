import pandas
import math
import os 
from movies import movies
from tags import tags
from ratings import ratings
import pickle
from kmeans import Point, Cluster, KMeans
import random

class UserMatrix:
	def __init__(self):
		fname = 'user_matrix.p'
		if os.path.isfile(fname):
			self.matrix = pickle.load(open( fname, "rb" ) )
			return
		matrix = {}
		rats = ratings('ds\\ratings.csv')
		tgs = tags('ds\\tags.csv')
		for id in rats.user_rat_mat:
			rm = rats.user_rat_mat[id]
			avg = sum(rm)/len(rm)
			tm = [0]*len(list(rats.user_rat_mat.values())[0])
			if id in rats.user_rat_mat:
				tm = [x*avg for x in rats.user_rat_mat[id]]

			tgm = [0]*len(list(tgs.tag_user_mat.values())[0])
			if id in tgs.tag_user_mat:
				tgm = [x*avg for x in tgs.tag_user_mat[id]]


			matrix[id] = rm + tm + tgm 

		pickle.dump(matrix, open(fname, "wb"))
		self.matrix = matrix

	def similarity(self,id1,id2):
		matrix = self.matrix
		if id1 not in matrix:
			print('id1 not found!')
			return

		if id2 not in matrix:
			print('id2 not found!')
			return

		mat1 = matrix[id1]
		mat2 = matrix[id2]
		d = 0
		mat1_sqr,mat2_sqr = 0,0
		for i in range(len(mat1)):
			d += mat1[i]*mat2[i]
			mat1_sqr += mat1[i]**2
			mat2_sqr += mat2[i]**2
		sim = d/(math.sqrt(mat1_sqr)*math.sqrt(mat2_sqr) )
		return sim

	def cluster(self,k):
		matrix = self.matrix
		points = []
		for u in matrix:
			points.append(Point(matrix[u]))
		random.shuffle(points)
		model = KMeans(points, k, 0.01)
		model.cluster()



