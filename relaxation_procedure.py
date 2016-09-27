import matplotlib.pyplot as plt

d1=[(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5)]
d2=[(-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]
dataset = [(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5), (-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]


# evaluating the a^Ty term.
def evaluate(w,x):
	ret = 0
	for i in xrange(3):
		ret +=  w[i]*x[i]
	return ret
# to determine the denominator of the expression of "J"
def square_values(x):
	square_sum = 0
	for i in xrange(3):
		square_sum += x[i]*x[i]
	return square_sum

# the main relaxation procedure with margins
def relaxation_procedure():
	noOfIterations = 0
	weight = [1,1,1]
	eta = 0.3

	#for i in xrange(len(dataset)):
	#	mod_value.append(square_values(dataset[i])
	while(1):
		noOfIterations += 1
		sumEval = 0
		#print weight
		missClass = []
		for i in xrange(len(dataset)):
			sumEval = 0
			for j in xrange(3):         # evaluating each of the points for correctly or incorrectly classified determination
				sumEval += dataset[i][j]*weight[j]

			if sumEval < 0.1:                 # 0.9 is the value of the 'b' used in the equation above, for further values of 'b' like 1/2/.. the Iterations dont stop and here also it stops at close to 50k iterations.
# with 'b=0.2' no. of iterations reduces to 5200 and it further reduces to 3.5k on 'b=0.1'.
				missClass.append(dataset[i])
		semiAns = [0,0,0]
		for i in xrange(len(missClass)):
			numer = float((1-evaluate(weight, missClass[i]))/square_values(missClass[i]))
			for j in xrange(3):
				semiAns[j] += float(numer*missClass[i][j])

		for i in xrange(3):
			weight[i] = weight[i] + eta*semiAns[i]
		#print "Misscalssified_length: ",		
		#print len(missClass)
		if(len(missClass)==0):
			break
	print "Total Iterations: ",
    	print noOfIterations
    	print "Final Weights: ",
    	print weight
    	return weight


def main():
	a=relaxation_procedure()
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


if __name__=="__main__":
	main()

