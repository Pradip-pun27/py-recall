# Multiples return in a function
import statistics as stat
list1=[i for i in range(100,120)]
def Mean_Median_Mode(lists):
    return stat.mean(lists), stat.median(lists), stat.mode(lists)
x,y,z=Mean_Median_Mode(list1) # Tuple of 3 values will returned as o/p

print(f"Mean :{x}\nMedian:{y}\nMode:{z}")
