
import numpy

def covariances(data):
    return numpy.cov(data)

def eigenvectors(cov):
    eigen_vv = []
    eigenvectors = numpy.linalg.eig(cov)[1]
    eigenvectors = format_matrix(eigenvectors)
    eigenvectors = eigenvectors.transpose()
    #eigen_vv.append(eigenvectors)
    eigenvalues = numpy.linalg.eig(cov)[0]
    eigenvalues = format_vector(eigenvalues)
    #eigen_vv.append(list(eigenvalues))
    for i in range(0,len(eigenvalues)):
        eigen_vv.append((eigenvalues[i],list(eigenvectors[i])))
    return eigen_vv

def format_matrix(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            matrix[i][j] = (truncate(matrix[i][j], 4))
    return matrix

def format_vector(vec):
    for i in range(0,len(vec)):
        vec[i]= truncate(vec[i], 4)
    return vec

def truncate(f, n):
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return float('.'.join([i, (d+'0'*n)[:n]]))

def pca_function(data,k):
    number_cols = len(data[0])  
    number_rows = len(data)   
    mean_of_matrix = []
    for index_cols in range(0,number_cols):    
        sumi = 0
        for index_rows in range(0,number_rows):
            sumi = sumi + data[index_rows][index_cols]
        mean_of_matrix.append(sumi/number_rows)     

    for index_cols in range(0,number_cols):
        for index_rows in range(0,number_rows):
            data[index_rows][index_cols] = data[index_rows][index_cols] - mean_of_matrix[index_cols]

    cov = covariances(data);    
    eigen = eigenvectors(cov);
    eigen = sorted(eigen, key=lambda x: x[0])
    eigen = eigen[::-1]
    for i in range(0,len(eigen)):
        eigen[i] = eigen[i][1]
    eigen = format_matrix(eigen)
    return eigen[:k]


