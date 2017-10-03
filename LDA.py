import numpy

def covariances(data):
    return numpy.cov(data)    

def matrix_inicialicer(rows, columns):
    matrix = []
    for i in range(0,rows):
        aux_m = []
        for j in range(0,columns):
            aux_m.append(0)
        matrix.append(aux_m)    
    return matrix

def vector_plus_vector(vec_1,vec_2):
    vec = []
    for i in range(0,len(vec_1)):
        vec_row = []
        for j in range(0,len(vec_1)):
            vec_row.append(vec_1[i]*vec_2[j]) 
        vec.append(vec_row)           
    return vec    

def eigenvectors(cov):
    eigen_vv = []
    eigenvectors = numpy.linalg.eig(cov)[1]
    eigenvalues = numpy.linalg.eig(cov)[0]
    for num_eigenvalues in range(0,len(eigenvalues)):
        eigen_vv.append((eigenvalues[num_eigenvalues],list(eigenvectors[num_eigenvalues])))
    return eigen_vv
def eigenvectors(cov):
    eigen_vv = []
    eigenvectors = numpy.linalg.eig(cov)[1]
    eigenvectors = format_matrix(eigenvectors)
    eigenvectors = eigenvectors.transpose()
    eigenvalues = numpy.linalg.eig(cov)[0]
    eigenvalues = format_vector(eigenvalues)
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

def lda_function(data,data_C,k):
    number_cols = len(data[0])
    number_rows = len(data) 
    mean_of_matrix = []
    for index_rows in range(0,number_rows):
        mean_of_matrix.append(sum(data[index_rows])/number_cols)
    data_no_repeted = []
    for index_rows in range(0,number_rows):
        for index_cols in range(0,1):
            if data_C[index_rows][index_cols] not in data_no_repeted:
                data_no_repeted.append(data_C[index_rows][index_cols])
    Nc = len(data_no_repeted)    
    sb = numpy.array(matrix_inicialicer(number_rows, number_rows))
    sw = numpy.array(matrix_inicialicer(number_rows, number_rows))    
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
                if (len(class_index) > selected_index) and (class_index[selected_index][0]):
                    aux_Xc.append(data[index_rows][index_cols])                    
                selected_index = selected_index +1    
            Xc.append(aux_Xc)   
        mean_of_class = []
        for index_rows in range(0,number_rows):
             mean_of_class.append(sum(Xc[index_rows])/len(Xc[index_rows]))            
        Xc = numpy.array(Xc)           
        covclase = covariances(Xc) 
        sw = sw + covclase         
        mea_sub = numpy.array(mean_of_class) - numpy.array(mean_of_matrix) 
        fir_m = vector_plus_vector(mea_sub,mea_sub)
        fir_m = Nc *  numpy.array(fir_m)
        sb = sb + fir_m   
    print(sb)
    eigen = eigenvectors(sb);
    eigen = sorted(eigen, key=lambda x: x[0])
    eigen = eigen[::-1]
    for i in range(0,len(eigen)):
        eigen[i] = eigen[i][1]
    eigen = format_matrix(eigen)
    return eigen[:k]  