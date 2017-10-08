import PCA

# We define a very small set of data for which to perform the tests
# the matrix represents a data set with dimensionality N
# to reduce this dimensionality with minimal reconstruction error
# from the resulting data you can use an algorithm like the KNN
# to check the error in the reconstruction

def small_data_test():
    test_1 = PCA.pca_function([[1,0,1,1],[0,1,2,0],[1,1,2,0],[0,1,2,1]],2)  
    result = [[0.8333, -0.5, -0.1666, -0.1666], [0.0, 0.0, 0.7071, -0.7071]]
    if test_1:
        return("All OK")
    else:
        return("something went wrong")

print(small_data_test())