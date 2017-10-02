import numpy

def covariances(data):
    return numpy.cov(data)    

def traspuest_1(matrix):
    return_matrix = []
    for elements in matrix:
        return_matrix.append(elements[0])
    return return_matrix

def matrix_plus_K(matrix,K):
    for i in range(0,len(matrix)):        
        for j in range(0,len(matrix[i])):
            matrix[i][j] = matrix[i][j] + K            
    return matrix
def vector_plus_K(vec,K):
    vec_r = []
    for i in range(0,len(vec)):
        vec_r.append(vec[i] * K) 
    return vec_r



def matrix_inicialicer(rows, columns):
    matrix = []
    for i in range(0,rows):
        aux_m = []
        for j in range(0,columns):
            aux_m.append(0)
        matrix.append(aux_m)    
    return matrix

def means_substract(mean_of_class,mean_of_matrix):
    for i in range(0,len(mean_of_class)):
        mean_of_class[i] = mean_of_class[i] - mean_of_matrix[i]
    return mean_of_class

def vector_plus_vector(vec_1,vec_2):
    vec = []
    for i in range(0,len(vec_1)):
        vec_row = []
        for j in range(0,len(vec_1)):
            vec_row.append(vec_1[i]*vec_2[j]) 
        vec.append(vec_row)           
    return vec
    
def matrix_plus_matrix(m1,m2):
    for i in range(0,len(m1)):
        for j in range(0,len(m1[i])):
            m1[i][j] = m1[i][j] +m2[i][j]
    return m1
def eigenvectors(cov):
    eigen_vv = []
    eigenvectors = numpy.linalg.eig(cov)[1]
    eigenvalues = numpy.linalg.eig(cov)[0]
    for num_eigenvalues in range(0,len(eigenvalues)):
        eigen_vv.append((eigenvalues[num_eigenvalues],list(eigenvectors[num_eigenvalues])))
    return eigen_vv

def pca_function(data,data_C,k):
    number_cols = len(data[0])   
    number_rows = len(data) 
    mean_of_matrix = []
    for index_rows in range(0,number_rows):
        mean_of_matrix.append(sum(data[index_rows])/number_cols)
    #print(mean_of_matrix)
    data_no_repeted = []
    for index_rows in range(0,number_rows):
        for index_cols in range(0,1):
            if data_C[index_rows][index_cols] not in data_no_repeted:
                data_no_repeted.append(data_C[index_rows][index_cols])
    Nc = len(data_no_repeted)
    sb = matrix_inicialicer(number_rows, number_rows)
    sw = matrix_inicialicer(number_rows, number_rows)
    for data_nr in data_no_repeted:
        class_index = []
        for index_rows in range(0,number_rows):
            aux_cl_index = []
            for index_cols in range(0,1):
                aux_cl_index.append(data_C[index_rows][index_cols] == data_nr)
            class_index.append(aux_cl_index)       
        Xc = []   
        for index_rows in range(0,number_rows):
            aux_Xc = []
            selected_index = 0
            for index_cols in range(0,number_cols):
                if class_index[selected_index][0]:
                    aux_Xc.append(data[index_rows][index_cols])                    
                selected_index = selected_index +1    
            Xc.append(aux_Xc)    
        
        mean_of_class = []
        for index_rows in range(0,number_rows):
             mean_of_class.append(sum(Xc[index_rows])/len(Xc[index_rows]))
        
        Xc = traspuest_1(Xc)        
        covclase = covariances(Xc)        
        sw = matrix_plus_K(sw,covclase)        
        mea_sub = means_substract(mean_of_class,mean_of_matrix)        
        fir_m = vector_plus_K(mea_sub,Nc)
        fir_m = vector_plus_vector(fir_m,mea_sub)
        sb = matrix_plus_matrix(sb,fir_m)        

    eigen = eigenvectors(sb);    
    eigen = sorted(eigen, key=lambda x: x[0])  
    for index_ei in range(0,len(eigen)):
        eigen[index_ei] = eigen[index_ei][1]
    return eigen[:k]    


print(pca_function([[1,2,3],[4,5,6],[7,8,9]],[[1],[2],[3]],3))