matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

# Number of rows
print(len(matrix))

# Number of columns
print(len(matrix[0]))

# Accessing an element in a 2d list
print(matrix[1][2])

# Looping through values in the 2d list
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end=" ")
    print("\n")

rows=int(input("Enter the number of rows - "))
columns=int(input("Enter the number of columns - "))
matrix=[]
for i in range(rows):
    temp=[]
    for j in range(columns):
        x=int(input("Enter your element - "))
        temp.append(x)
    matrix.append(temp)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print("\n")

matrixA=[[1,2],[3,4]]
matrixB=[[5,6],[7,8]]

aditionResult=[[0,0],[0,0]]
subtractionResult=[[0,0],[0,0]]

for i in range(0,2):
    for j in range(0,2):
        aditionResult[i][j]=matrixA[i][j]+matrixB[i][j]
        subtractionResult[i][j]=matrixA[i][j]-matrixB[i][j]

#Addition Result
for i in range(2):
    for j in range(2):
        print(aditionResult[i][j],end=" ")
    print("\n")

#Subtraction Result
for i in range(2):
    for j in range(2):
        print(subtractionResult[i][j],end=" ")
    print("\n")