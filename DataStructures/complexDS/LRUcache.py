import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = {}
        self.list = []
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.list:
            self.list.remove(key)
            self.list.append(key)
            return self.data[key]
        else:
            return -1
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #If capacity is reached, pop from the list and 
        if key in self.data:
            self.data[key] = value
            self.list.remove(key)
            self.list.append(key)
            
        else:
            if self.capacity <= 0:
                del self.data[self.list[0]]
                del self.list[0]
            self.data.update({key: value})
            self.list.append(key)
            self.capacity = self.capacity - 1
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
