## Machine learning algorithms ##
The aove repo contains some of the ML based algorithms.

### Algorithms Implemented ###
- Single-sample perceptron
- Single-sample perceptron with margin
- Relaxation algorithm with margin
- Widrow-Hoff or Least Mean Squared (LMS) Rule
- K-mean Clustering algorithm on one feature.


`more to be added later....`

### Formulas used in respective algorithms ###
- Single-sample perceptron
```
if(ans<0):
				for i in xrange(3):
					weight[i]=weight[i]+eta*dataset[j][i]
```

- Single-sample perceptron with margin
```
if(ans<1):                                          
				for i in xrange(3):
					weight[i]=weight[i]+eta*dataset[j][i]
```

- Relaxation algorithm with margin

![relaxation](https://cloud.githubusercontent.com/assets/9693795/18884894/0a500e14-8507-11e6-83ad-3fd5753ca39a.png)


- Widrow-Hoff or Least Mean Squared (LMS) Rule
![widrow-hoff](https://cloud.githubusercontent.com/assets/9693795/18884895/0a57378e-8507-11e6-92ce-d45b9797c94b.png)


### KPCA: *Kernel Principal Component Analysis*

Algorithm:
- Calculate the [Sqaured-Euclidean](https://en.wikipedia.org/wiki/Euclidean_distance) Distance of the data
- convert the resulting data into a sqaure matrix
- Apply the [Radius Basis Function](https://en.wikipedia.org/wiki/Radial_basis_function_kernel) kernel method on the resulting Square matrix.
- Center the resulting kernel matrix (say K) following the below method :
	* Calculate the mean of kernel matrix (say K_mean)
	* K_center_data = K - K_mean
	(Here an inbuilt data centerer algorithm is used for this purpose)
- Find the Eigen Values and corresponding Eigen vectors of the centered data
- Sort the Eigen vectors in descending order of eigen values
- Calculate the final result as dot product of K_center_data and first *N* Eigen vectors (here *N* is the feature_size)

Implementaion:
- We have a 2D non-linear data containing 2 classes marked with red and blue.
- Kernel Principal Component Analysis Algorithm was applied on the data to separate both classes of data.
- The resulting data can be visualised in 3D and 2D plot.
