
"""
k-means is  one of  the simplest unsupervised  learning  algorithms  that  solve  the well  known clustering problem.

The procedure follows a simple and  easy  way  to classify a given data set  through a certain number of  clusters.

- Let  X = {x1,x2,x3,……..,xn} be the set of data points and V = {v1,v2,…….,vc} be the set of centers.
- Randomly select ‘c’ cluster centers.
- Calculate the distance between each data point and cluster centers.
- Assign the data point to the cluster center whose distance from the cluster center is minimum of all the cluster centers.
- Recalculate the new cluster center using: `v[i] = (1/c[i])Summation(x[i])` for no. of data points in ith cluster.
- Recalculate the distance between each data point and new obtained cluster centers.
- If no data point was reassigned then stop, otherwise repeat from step 3.


Implementatios of K-mean clustering algorithm is below.
"""

import random

def k_means(data, k):
	# 1. k initial "means" are randomly selected from the data set.
	means = random.sample(data, k)
	def kmeans1(data, means):
		# 2. k clusters are created by associating every observation with the nearest mean.
		clusters = [ [] for _ in means ]
		for d in data:
			distances = [ (abs(d-m), i) for i,m in enumerate(means) ]
			_,closest = min(distances)
			clusters[closest].append(d)
		return sorted(clusters)
	prev = []
	curr = kmeans1(data, means)
	while curr != prev:
		prev = curr
		# 3. The centroid of each of the k clusters becomes the new means.
		means = [ sum(c) / max(1,len(c)) for c in curr ]
		curr = kmeans1(data, means)
	# 4. ...repeated until convergence has been reached.
	return zip(means, curr)

if __name__ == '__main__':
	Ages = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
	print k_means(Ages, 2)
  
  



"""
change the data of Ages as per the required data, and change the value of "2" to the no. of clusters you want to have.
"""
