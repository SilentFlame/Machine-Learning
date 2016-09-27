import matplotlib.pyplot as plt
from math import sqrt

d1=[(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5)]
d2=[(-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]

dataset = [(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5), (-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]

def mid_eval(a,b):
	rslt = 0
	for i in xrange(3):
		rslt += a[i]*b[i]

	return rslt


# def mod(x):
# 	if x < 0:
# 		return x*(-1)
# 	else:
# 		return x

# nk = 0
# def widrow_hoff():
# 	weight = [1,1,1]
# 	eta = 0.9
# 	global nk 
# 	theta = 0.5
# 	iterations = 0
# 	while(1):
# 		iterations += 1
# 		classi = 0
# 		print weight
# 		for i in xrange(len(dataset)):
# 			semi = mid_eval(weight, dataset[i])
# 			correct = 0
# 			for j in xrange(3):
# 				if (mod(eta*(semi-1)*dataset[i][j])) < theta:
# 					correct+=1

# 			if correct == 3:
# 				classi += 1


# 		if classi != len(dataset):          # if not all the points are correctly classified.
# 			for i in xrange(len(dataset)):
# 				nk += 1
# 				eta = eta/nk           #using anneling for learning rate. n(k)=n(1)/k
# 				semi = mid_eval(weight, dataset[i])
# 				correct = 0
# 				for j in xrange(3):
# 					if mod((eta*(semi-1)*dataset[i][j])) < theta:
# 						correct+=1
# 				if correct == 3:       #whatif the classification becomes true only due to change in the eta value.
# 					break

# 				for j in xrange(3):
# 					weight[j] = weight[j] + float(eta*(1-semi)*dataset[i][j])

# 		if classi == len(dataset):
# 			print "weights: ",
# 			print weight
# 			print "no. of Iterations: ",
# 			print iterations
# 			break

# 		if correct == 3:
# 			print "weights: ",
# 			print weight
# 			print "no. of Iterations: ",
# 			print iterations
# 			break

# 	print "value of K: ",
# 	print nk
# 	return weight


def comp_funcn(a):
	result = 0
	for i in xrange(3):
		result += pow(a[i], 2)

	return sqrt(result)
		

def widrow_hoff():
	iterations = 0
	eta = 0.2
	theta = 0.9
	weight = [1,1,1]
	nk = 0
	while(1):
		iterations += 1
		nk += 1
		eta = eta/nk
		for i in xrange(len(dataset)):
			ans = [0,0,0]
			semi = mid_eval(weight, dataset[i])
			for j in xrange(3):
				ans[j] = float(eta*(1-semi)*dataset[i][j])
			for k in xrange(3):
				weight[k] += ans[k]
			
			comp = comp_funcn(ans)
			print "Updated weights: ",
			print ans

			print "comaparision value: ",
			print comp

			if ( comp >= theta):
				break

		if ( comp >= theta):
				break
	print "No. of Iterations: ",
	print iterations
	print "weights: ",
	print weight
			
	return weight


def main():
	a=widrow_hoff()
	print a
	x1 = []
	x2 = []
	y1 = []
	y2 = []
	for j in xrange(len(d1)):
		x1.append(d1[j][1])
		y1.append(d1[j][2])
	for j in xrange(len(d2)):
		x2.append((-1)*d2[j][1])
		y2.append((-1)*d2[j][2])

	plt.plot(x1,y1,'ro')
	plt.plot(x2,y2,'bo')
	
	m1 = a[2]/a[1]
	m2 = (-1)/(m1)
	c = (-1)*a[0]/a[2]
	ya = m2*100+c
	yb = m2*(-100)+c
	plt.plot([100,-100],[ya,yb],'r')
	plt.axis([-10,10,-10,10])
	plt.show()


if __name__ == '__main__':
	main()