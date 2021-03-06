Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 @mrinalini-iyer Sign out
1
0 0 mrinalini-iyer/cs-review
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
cs-review/DataStructure/StacksQueues/MultiStack.py
dd24c20  33 seconds ago
@mrinalini-iyer mrinalini-iyer Create MultiStack.py
     
62 lines (45 sloc)  1.48 KB
'''
Using single array implement three stacks
stack 0: [0,n/3)
stack 1: [n/3, 2n/3)
stack 2: [2n/3, n)
'''
class FixedMultiStack():
    
    def __init__(self, num_stack, capacity):
        self.number_of_stacks = num_stack
        self.stack_capacity = capacity
        self.values = [0] * self.stack_capacity * self.number_of_stacks
        self.size = [0] * self.number_of_stacks
    
    def isFull(self, stack_number):
        if self.size[stack_number] > self.stack_capacity:
            return True
        return False
    
    def isEmpty(self, stack_number):
        return self.size[stack_number] == 0

    
    def indexOfTop(self,stack_number):
        offset = stack_number * self.stack_capacity
        return offset + self.size[stack_number]
    
    def push(self, stack_number, value):
        if self.isFull(stack_number):
            print("stack is full")
            return
        self.values[self.indexOfTop(stack_number)] = value
        self.size[stack_number] += 1
    
    def pop(self, stack_number):
        if self.isEmpty(stack_number):
            print("stack empty")
            return 
        top_index = self.indexOfTop(stack_number)
        print("Top index:", top_index)
        value =  self.values[top_index - 1]
        self.values[top_index - 1] = 0
        self.size[stack_number] -= 1
        return value
    
# Test Case

MS = FixedMultiStack(4, 3)
MS.push(0, 1)
MS.push(0, 2)
MS.push(0, 3)
MS.push(0, 4)
MS.push(0, 2)
print(MS.pop(0))

        
        
        
    
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
Press h to open a hovercard with more details.
