import pandas
import operator

class tags:
	def __init__(self,fname):
		self.total_tags = 100
		df = pandas.read_csv(fname)
		self.set_user_mov_tag_matrix(df)


	def set_user_mov_tag_matrix(self,df):
		tags = self.get_frequent_tags(df)
		tag_mov_mat = {}
		tag_user_mat = {}
		for i, tag in df.iterrows():
			id = tag['movieId']
			user_id = tag['userId']
			if id not in tag_mov_mat:
				tag_mov_mat[id] = [0]*self.total_tags

			if user_id not in tag_user_mat:
				tag_user_mat[user_id] = [0]*self.total_tags

			mov_tags = tag['tag'].strip().split(' ')
			for t in mov_tags:
				if t not in tags:
					continue
				i = tags.index(t)
				tag_mov_mat[id][i] = 1
				tag_user_mat[user_id][i] = 1
		self.tag_user_mat = tag_user_mat
		self.tag_mov_mat = tag_mov_mat



	def get_frequent_tags(self,df):
		tags = {}
		for i, row in df.iterrows():
			cats = row['tag'].strip().split(' ')
			for c in cats:
				if c not in tags:
					tags[c] = 0
				tags[c] += 1

		tags = sorted(tags.items(), key=operator.itemgetter(1),reverse=True)
		i = 0
		l = []
		for(x,y) in tags:
			if i >= self.total_tags:
				break
			i += 1
			l.append(x)
		return l
		

