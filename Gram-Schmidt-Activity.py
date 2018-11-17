#extracredit_GS_ws4.py
#Author: Sebrianne Ferguson
#purpose: to do dot products, find orthogonal sets, find orthonormal sets
#         and solve the worksheet Professor Lapuz gave to us.

import math

def dotProduct(m1, m2):
    '''find the dot product of 2 matrices'''
    #only find if the 2 are of equal length
    if (len(m1) == len(m2)):
        dp = 0
        for i in range(len(m1)):
            dp += m1[i] * m2[i]
        return dp

def product(scalar, v):
    '''multiplies every entry of v by the scalar'''
    for i in range(len(v)):
        v[i] *= scalar;
    return v

def subtract(x, y):
    '''subtracts the corresponding element of y from x'''
    if len(x) == len(y):
        for i in range(len(x)):
            x[i] -= y[i]
    return x

def gs(x):
    '''performs gram-schmidt process on a set of vertexes x and returns automatic transpose'''
    orthoVs = [] #stores all the vectors
    for i in range(len(x)):
        vi = x[i] #because each of the formulas start out with xp
        if i != 0: #if its not the first vector
            for j in range(i):
                #find the dot product of xp and vj and divide by dot product of vj and vj
                scalar = dotProduct(x[i], x[j])/dotProduct(x[j], x[j])
                vi = subtract(vi, product(scalar,x[j])) #subtract from the current difference
        orthoVs.append(vi[:]) #add to the list of vectors

    #note: due to how python structures lists, the setup is already the transpose.
    print("orthogonal vectors (transpose):")
    for row in orthoVs:
        print(row)

    #now normalize the vectors
    for i in range(len(orthoVs)):
        orthoVs[i] = normalize(orthoVs[i])

    print("normalized vectors (transpose):")
    for row in orthoVs:
        print(row)
            
    return orthoVs

def normalize(vector):
    '''normalizes the vector if needed by finding the magnitude and creating a unit vector'''
    # ||vi|| = the square root of the dot product of vi
    mag = math.sqrt(dotProduct(vector, vector))
    if (mag == 1): #already a unit vector
       return vector
    else: #normalize it
       return product(1/mag, vector)

def transpose(u):
    '''not needed apparently'''
    transpose = [] #empty matrix
    for i in range(len(u[0])): #make a row the size of the original matrix's columns
        row = [] #make an empty row
        for j in range(len(u)): #set the size equal to the height of the original matrix
            row.append(0)
        transpose.append(row) #add the row to the transpose
    #print(transpose)

    #fill in the transpose
    for i in range(len(u[0])):
        for j in range(len(u)):
            transpose[i][j] = u[j][i] #new[row][column] = old[column][row]

    print("transpose:")
    for row in transpose:
        print(row)

    return transpose

def mProduct(m1, m2):
    '''finds the product of 2 matrices'''
    product = []
    for i in range(len(m2)):
        product.append(0)

    for i in range(len(m1)): #for the number of rows
        z =0
        for j in range(len(m1[0])): #for every entry of the row
            z += (m1[i][j] * m2[j]) #multiply and add to the product of that row
        #print(z)
        product[i] = z
        
    return product
            
def shipGame(position, end, x):
    u = gs(x) #normalize the vectors and return the transpose 
    target = subtract(end,position) #then find the target vertex
    print("target:", target)
    #ut = transpose(u) #get the transpose -- NOT NEEDED

    c = mProduct(u, target)
    for i in range(len(c)):
        print("c", end = "")
        print(i, "=", c[i])

    
#example from the professor's video
print("Professor Lapuz's Example:")
x = [[-1,2,-2],[-1,0,-1],[-2,1,-1]]
shipGame([1,1,1], [-2,4,3], x)

print("Sebrianne's Homework:")
ship2 = [[1,2,-2],[1,-1,-1],[2,1,-1]]
shipGame([-2,4,3], [-3,-4,2], ship2)



        
        
        
    
    
    
        
