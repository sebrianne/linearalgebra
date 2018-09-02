#matrix program.py
#Sebrianne Ferguson
#Last edited September 1st, 2018
#Written in IDLE
#Purpose: to perform scale, swap, and add operations on matrices
#         in addition to checking if it is in row echelon and/or
#         reduced row echelon form. Also an operation to display a
#         matrix in matrix form.


import numpy as np #found this on w3resources.com, needed for make_id()

def row_scale(matrix, rowNum, scalar):
    '''multiplies each of the elements of the row with the scalar'''
    for i in range (len(matrix[rowNum-1])): #rowNum-1 so we don't have to start at 0
        matrix[rowNum-1][i] *= scalar
    return matrix

def row_swap(matrix, row1, row2):
    '''if the lengths of the rows are the same then swaps the elements in each
       corresponding column in 2 different rows'''
    if (len(matrix[row1-1]) != len(matrix[row2-1])):
        print("these 2 rows cannot be swapped")
    else:
        for i in range(len(matrix[row1-1])): #swap algorithm
            temp = matrix[row1-1][i]
            matrix[row1-1][i] = matrix[row2-1][i]
            matrix[row2-1][i] = temp
    return matrix

def row_add(matrix, row1, row2, scalar):
    '''if the lengths of the rows are the same multiplies the first row
       by the scalar and adds the product to the value in 2nd row corresponding
       column'''
    if (len(matrix[row1-1]) != len(matrix[row2-1])):
        print("this operation cannot be done")
    else:
        for i in range(len(matrix[row1-1])):
            product = matrix[row1-1][i] * scalar
            matrix[row2-1][i] += product
    return matrix

def display(matrix):
    '''will display the matrix in matrix form'''
    print() #blank line for formatting purposes
    for i in range (len(matrix)):
        print(matrix[i])

def make_id(n): #not complete, need to install NumPy for this to work
    '''creates an “n” by “n” matrix with 1’s in the diagonal and 0’s elsewhere'''
    #referred to w3resource.com for the numpy information
    matrix = np.zeros((n,n), dtype=int)
    matrix = matrix.tolist() #found this command on stackoverflow
    for i in range(n):
        for j in range (n):
            if (i == j): #this will create the diagonal pivots 
                matrix[i][j] = 1
    return matrix
                
def is_row_echelon(matrix):
    '''checks to see if the matrix is in row echelon form and
      returns true if m is already in row echelon form; false if it is not.'''

    #row echelon form:
    #1. All nonzero rows are above any rows of all zeros.
    #   (dont need to explicitly check for this i don't think)
    #2. Each leading entry of a row is in a column to the right of the leading entry of
    #the row above it.
    #3. All entries in a column below a leading entry are zeros

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if (row == column): #checking to make sure there is a pivot
                if (matrix[row][column] == 0):
                    return False
            if (column < row): 
                if (matrix[row][column] != 0):
                    return False
    return True #if it passes through the for loop sucessfully 


def is_rref(matrix): 
    ''' checks to see if the matrix is in reduced row echelon form
      returns true if m is already in reduced row echelon form; false if it is not.'''

    #reduced row echelon form (in addition to the row echelon reqs)
    #1. The leading entry in each nonzero row is 1.
    #2. Each leading 1 is the only nonzero entry in its column.

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if (row == column): #checking to make sure there is a pivot
                if (matrix[row][column] != 1):
                    return False
            elif (matrix[row][column] != 0):
                return False
    return True #if it passes through the entire list and doesn't find anything
    

#main method
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[0,1,1],[2,1,2],[3,1,2]]
z = [[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
print("scale row 3 of x by 2")
display(row_scale(x, 3, 2))
print("make_id(7)")
display(make_id(7))
print("is y row echelon:", is_row_echelon(y))
print("is make_id(3) row echelon:",is_row_echelon(make_id(3)))
print("is make_id(4) rref:", is_rref(make_id(4)))
print("is z rref:", is_rref(z))
print("is z row echelon:", is_row_echelon(z))
print("x swap row 1 and 2 ")
display(row_swap(x, 1, 2))
print("add row2 * -4 scalar to row 1:")
display(row_add(x, 2, 1, -4))
