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
    for i in range(0,len(vec)):
        vec[i] = vec[i] * K
    return vec

def vector_plus_vector(vec_1,vec_2):
    for i in range(0,len(vec_1)):
        vec_1[i] = vec_1[i]*vec_2[i]
    return vec_1[i]

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
        print(mea_sub)
        fir_m = vector_plus_K(mea_sub,Nc)
        #fir_m = vector_plus_vector(fir_m,mea_sub)
        print(fir_m)






    #print(data_no_repeted)
# function[W]=lda(X,Xl,k)
    
#     m = mean(X,2); % Calcular la media
#     Sw = zeros(F,F); % Completar con ceros
#     Sb = zeros(F,F); % Completar con ceros
#     Nc = length(unique(Xl)); % Obtener clases 
#     for c=unique(Xl) % Por cada clase
#         indices = Xl==c; % Vector para comprobar clases
#         Xc=X(:,indices); % Comprobarlas
#         MediaClase=mean(Xc,2); % Sacar la media
#         CovClase = cov(Xc'); % Matriz de covarianza
#         Sw=Sw+CovClase; % Cálculo de matriz intraclases
#         Sb=Sb+(Nc*(MediaClase-m)*(MediaClase-m)'); % Cálculo de matriz entre
#     end
#     [Vec,Lam] = eig(Sb,Sw); % Obtener eigenvectore y egenvalores
#     [V,I] = sort(diag(Lam),'descend'); % Ordenarlos
#     Eigen = Vec(:,I); % Obtener los deseados
#     W = Eigen(:,1:k); % Retornarlos
# end

pca_function([[1,2,3],[4,5,6],[7,8,9]],[[1],[2],[3]],3)