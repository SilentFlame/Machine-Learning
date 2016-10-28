import matplotlib.pyplot as plt

d1=[(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5)]
d2=[(-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]

dataset = [(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5), (-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]

#defining the function
def single_sample_perceptron():
	weight=[1,1,1]
	iterations=0
	eta = 0.2
	while(1):
		iterations=iterations+1
		ans=0
		count=0
		# print weight
		for j in xrange(len(dataset)):
			ans=0
			for i in xrange(3):
				ans=ans+float(weight[i]*dataset[j][i])
			if(ans<1):                                          #different values of "b" for this comparison so differs the value of total Iterations, so as differs the time of computing.
				for i in xrange(3):
					weight[i]=weight[i]+eta*dataset[j][i]
				break
			count+=1
		if count==len(dataset):
			break
	print
	print "Final weights: ",
	print weight
	print "No. of Iterations: ",
	print iterations
	return weight


def main():
	a=single_sample_perceptron()
	x1 = []
	x2 = []
	y1 = []
	y2 = []
	for j in range(len(d1)):
		x1.append(d1[j][1])
		y1.append(d1[j][2])
	for j in range(len(d2)):
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

if __name__ == "__main__":
	main()

