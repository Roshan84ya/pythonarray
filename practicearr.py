'''   matrix=matrix
      row=no. of row
      col=no.od coloumn
      SumM=sum of the matrix
      Relement=ROws element '''

matrix=[]
row,col=map(int,input().split())
SumM=0
for i in range(row):            #here we have adeed so many list i.e the no of rows that we want in our array
    matrix.append([])
for i in range(row):
    for j in range(col):
        matrix[i].append([])     #here we have added the c list again and we made the coloumn
      
for i in range(row):
    Relement=[int(t) for t in input().split()]
    for j in range(col):
        
        matrix[i][j]=Relement[j]               #here we took input in that array

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end="")
        print(" ",end="")
    print()
for i in matrix:
    SumM+=sum(i)
print(SumM)
