# sort a stack using another stack - smallest element on top

def sort(input_list):
    
    output_list = []
    
    
    while(input_list):
        tmp = input_list.pop()
        
        while(output_list and output_list[-1] > tmp):
            input_list.append(output_list.pop())
        
        output_list.append(tmp)
        
    while(output_list):
        input_list.append(output_list.pop())
    
    return input_list

#test case

input_list = [6, 8, 3, 9, 1]
print(sort(input_list))
