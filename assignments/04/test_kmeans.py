from kmeans import Point, Cluster, KMeans
import random

#-----------------------------------------------------------
def silhouette(points, clusters):
	s = [0] * len(points)
	for i, p in enumerate(points):
		b_min = None
		for c in clusters:
			if p in c.points:
				a, a_count = 0, 0
				for q in c.points:
					a += p.RMS(q)
					a_count += 1
				a = a/a_count
			else:
				b, b_count = 0, 0
				for q in c.points:
					b += p.RMS(q)
					b_count += 1
				b = b/b_count
				if b_min is None or b_min > b:
					b_min = b

		# print(a, b_min)
		s[i] = (b_min-a)/max(b_min,a)
	return sum(s)/len(s)

#-----------------------------------------------------------
def get_iris_data():
	file_name = 'iris.csv'
	with open(file_name) as f:
		header = f.readline()
		points = []
		for line in f:
			items = line.strip().split(',')
			r = [
				float(items[0]),
				float(items[1]),
				float(items[2]),
				float(items[3]),
				items[4]
			]
			points.append( Point(r) )
	random.shuffle(points)
	return points

#-----------------------------------------------------------

points = get_iris_data()
for k in range(2, 10):
	model = KMeans(points, k, 0.01)
	model.cluster()
	# model.show()
	print('k = ', k, 'silhouette = ', silhouette(model.points, model.clusters))

