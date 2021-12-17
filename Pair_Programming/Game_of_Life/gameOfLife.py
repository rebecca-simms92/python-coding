from random import randint
import copy
import time

def start(n):
    matrix = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(randint(0,1))
        matrix.append(l)
    for j in matrix:
        print(j)
    print("\n")
    return matrix

def changePopulation(matrix,n):
    matrix_copy = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                counter = 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if k<n and k>-1 and l < n and l>-1:
                            if matrix_copy[k][l] == 1:
                                counter +=1
                if matrix_copy[i][j] == 1:
                    counter -=1
                if counter > 3 or counter <2:
                    matrix[i][j] = 0
            elif matrix[i][j] == 0:
                counter = 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if k<n and k>-1 and l < n and l>-1:
                            if matrix_copy[k][l] == 1:
                                counter +=1
                if matrix_copy[i][j] == 1:
                    counter -=1
                if counter == 3:
                    matrix[i][j] = 1
    for j in matrix:
        print(j)


matrix = start(3)
for i in range(10):
    changePopulation(matrix,3)
    print("\n")
    time.sleep(2)
