import csv

# with open("movies.csv") as f:
#     data = list(csv.reader(f))
#     print(f"The headers are \n{data[0]}")
#     print(f"The records(data) are\n{data[1:]}")
    
#     with open("jpt.txt","w") as f:
#         f.write(str(data))
#         print("All Done!\n")

from numpy import random

def Maths(data):
    total,c =0,0
    for num in data:
        c+=1
        total+=num
    average = total/c

    max= data[0]
    for num in data:
        if(num>max):
            max = num
    
    min = data[0]
    for num in data:
        if(num<min):
            min = num
    
    for i in range(len(data)):
        for j in range(i,len(data)):
            if(data[i]>data[j]):
                t=data[i]
                data[i]= data[j]
                data[j]=t
    
    return min,max,round(average,4),data # this data np_array has been sorted now


data = random.randint(1,100,11)
print(data)
print("The calculated min, max and avg of data and sorted data from the function are")
print(Maths(data)) # printing the returned values(min, max and avg, sorted_array)
print(f"The min, max and mean of a data by numpy are : {data.min(), data.max(), round(data.mean(),3)}")