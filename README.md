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

### PCA: *Principal component analysis*
Algorithm:
* Calculate average of the data:
$$x_{c}$$
* Substract the avarage to the data:
$$x_{i}=x_{c}-x_{i}$$
* Calc the covariant matrix:
$$\sum_{c}$$
* Find the eigenvectos.
* Sort it in a descendent way.
* Define W with the K first eigenvectos.