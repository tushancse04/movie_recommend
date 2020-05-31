import random
import math

#-----------------------------------------------------------
class Point:
	def __init__(self, row):
		self.row = row


	def RMS(self, y):
		s = 0
		for i in range(len(self.row)):
			s += (self.row[i] - y.row[i])**2
		return math.sqrt(s)


	def __str__(self):
		return str(self.row)

#-----------------------------------------------------------
class Cluster:
	def __init__(self, point=None):
		self.points = []
		self.centroid = None
		self.old_centroid = None
		self.delta = None
		if point is not None:
			self.add(point)


	def add(self, point):
		self.points.append(point)
		if len(self.points) == 1:
			self.centroid = Point([x for x in point.row])
		else:
			n = len(self.points) - 1
			for i in range(len(self.centroid.row)):
				self.centroid.row[i] = (self.centroid.row[i]*n + point.row[i]) / (n+1)


	def update(self):
		if self.old_centroid is None:
			self.old_centroid = Point( [0]* len(self.centroid.row) )

		self.delta = self.centroid.RMS(self.old_centroid)
		# print('delta: {}'.format(self.delta))
		self.old_centroid = Point( [ i for i in self.centroid.row ] )


	def show(self):
		print('\nCluster centroid', self.centroid)
		print('Delta', self.delta)
		for p in self.points:
			print('\t', p)


#-----------------------------------------------------------
class KMeans:
	def __init__(self, points, k, threshold=0.1):
		self.points = points
		self.k = k
		self.clusters = []
		self.threshold = threshold


	def cluster(self):
		i = 0
		while not self.converged():
			i += 1
			for c in self.clusters:
				c.points = []

			for point in self.points:
				if len(self.clusters) < self.k:
					self.clusters.append( Cluster(point) )
				else:
					# Find the closest cluster
					min_d, closest_cluster = None, None
					for c in self.clusters:
						d = point.RMS(c.centroid)
						if closest_cluster is None or d < min_d:
							min_d = d
							closest_cluster = c

					# Add point to closest cluster
					closest_cluster.add(point)

			for c in self.clusters:
				c.update()
		i = 0
		for c in self.clusters:
			d = 0
			for p in c.points:
				d += p.RMS(c.centroid)
			print("average distance among points and : ",i,"th cluster's centroid : ",d/len(c.points))
			i += 1
		print('----------------------------------------------------------------------------')
		avg = 0
		c = 0
		for i in range(len(self.clusters)):
			for j in range(i+1,len(self.clusters),1):
				p1 = self.clusters[i].centroid
				p2 = self.clusters[j].centroid
				d = p1.RMS(p2)
				print('Distance between ',i,'th and ',j,'th centroid : ',d)
				avg += d
				c += 1
		print('---------------------------------------------------------------------------')
		print('Average distance between centroids : ', avg/c)



	def converged(self):
		if len(self.clusters) < self.k:
			return False
		return all([c.delta < self.threshold for c in self.clusters])


	def show(self):
		for c in self.clusters:
			c.show()

#-----------------------------------------------------------



