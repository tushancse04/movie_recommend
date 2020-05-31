import pandas as pd
import pickle
import os
import time

class movie_data:
	def __init__(self,reload=False):
		self.dir = 'movielens/'
		self.ratings_file = self.dir + 'ratings.csv'
		movies = pd.read_csv(self.dir + 'movies.csv')
		ratings = pd.read_csv(self.ratings_file)
		users = pd.read_csv(self.dir + 'users.csv')
		self.movies = movies
		self.users = users
		self.ratings = ratings
		self.set_user_movie_rating_matrix(users,movies,ratings)

	def add_rating(self,uid,mid,rating):
		t = int(time.time())
		self.ratings.loc[len(self.ratings)] = [uid, mid,rating,t]
		self.ratings.to_csv(self.dir + 'ratings.csv')
		pickle.dump(self,open('mat.p',"wb"))


	def set_user_movie_rating_matrix(self,users,movies,ratings):
		uids = users.user_id.unique()
		uid_idx_map = {}
		idx_uid_map = {}
		for i,uid in enumerate(uids):
			uid_idx_map[uid] = i 
			idx_uid_map[i] = uid

		mid_idx_map = {}
		idx_mid_map = {}
		mids = movies.movie_id.unique()
		for i,mid in enumerate(mids):
			mid_idx_map[mid] = i
			idx_mid_map[i] = mid

		genres = movies.genres.unique()
		glist = []
		for g in genres:
			g = g.strip()
			g = g.split('|')
			glist += g

		glist = list(set(glist))
		gname_idx_map = {}
		for i,g in enumerate(glist):
			gname_idx_map[g] = i

		mg_map = {}
		for i,r in movies.iterrows():
			mg_map[r['movie_id']] = [gname_idx_map[g] for g in r['genres'].strip().split('|')]


		uf = [[[] for g in gname_idx_map] for uid in uid_idx_map]
		mf = [[[] for g in gname_idx_map] for mid in mid_idx_map]
		for i,r in ratings.iterrows():
			uidx = uid_idx_map[r['user_id']]
			midx = mid_idx_map[r['movie_id']]
			score = r['rating']
			if midx not in mg_map:
				continue
			for gid in mg_map[midx]:
				uf[uidx][gid].append(score)
				mf[midx][gid].append(score)
		for i in range(len(uf)):
			for j in range(len(uf[i])):
				r = uf[i][j]
				uf[i][j] = 0 if len(r) == 0 else sum(r)/len(r)
		
		for i in range(len(mf)):
			for j in range(len(mf[i])):
				r = mf[i][j]
				mf[i][j] = 0 if len(r) == 0 else sum(r)/len(r)


		self.uid_idx_map = uid_idx_map
		self.idx_uid_map = idx_uid_map
		self.mid_idx_map = mid_idx_map
		self.idx_mid_map = idx_mid_map
		self.gname_idx_map = gname_idx_map
		self.mg_map = mg_map
		self.uf = uf
		self.mf = mf

