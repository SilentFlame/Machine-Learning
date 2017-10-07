import LDA

# We define a very small set of data for which to perform the tests
# the matrix represents a data set with dimensionality N
# to reduce this dimensionality with minimal error
# it is better that you dont reduce to much the data
# from the resulting data you can use an algorithm like the KNN
# to check the error in the clasification
# KNN is a linear clasificator with the N neighbors more close

def small_data_test():
    test_1 = LDA.lda_function([[1,0,1,2,3],[2,1,1,2,3],[2,2,3,4,5]],[[0],[1],[1]],3)  
    result = [[-0.559, -0.281, -0.78], [-0.3336, -0.7849, 0.5219], [-0.759, 0.552, 0.345]]
    if test_1:
        return("All OK")
    else:
        return("something went wrong")

print(small_data_test())