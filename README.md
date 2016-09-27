## Machine learning algorithms ##
The aove repo contains some of the ML based algorithms.

### Algorithms Implemented ###
- Single-sample perceptron
- Single-sample perceptron with margin
- Relaxation algorithm with margin
- Widrow-Hoff or Least Mean Squared (LMS) Rule


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
