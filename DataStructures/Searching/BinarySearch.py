''' 
Searching through a list

1. Binary search
2. Hash maps
3. Binary trees


Binary search can be used since data is sorted.

'''
import math 

def binarySearch(input_list, data, left, right):
     
    mid = math.floor((left + right) / 2)
    
    if data < input_list[mid]:
        return binarySearch(input_list, data, left, mid -1)
    elif data > input_list[mid]:
        return binarySearch(input_list, data, mid + 1, right)
    else:
        return mid
    

input_list = [1, 2, 5, 7, 8]    
print(binarySearch(input_list, 8, 0, 5))
