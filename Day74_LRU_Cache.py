#Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:

#PUT x y: sets the value of the key x with value y
#GET x: gets the value of key x if present else returns -1.
#The LRUCache class has two methods get() and put() which are defined as follows.

#get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
#put(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should remove the least recently used item before inserting the new item.
#In the constructor of the class the capacity of the cache should be initialized.

# design the class in the most optimal way

class LRUCache:
      
    def __init__(self, cap):
        #code here
        self.cap = cap
        self.s = []
        self.res = []
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        for i in range(len(self.s)):
            if self.s[i][0] == key:
                self.s.append(self.s.pop(i))
                self.res.append(self.s[-1][1])
                return self.s[-1][1]
        self.res.append(-1)
        return -1
        
        
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        #for checking if key already exist
        for i in range(len(self.s)):
            if self.s[i][0] == key:
                self.s[i][1] = value
                self.s.append(self.s.pop(i))
                return
        #checking for new key
        if len(self.s) < (self.cap):
            self.s.append([key, value])
        else:
            self.s.pop(0)
            self.s.append([key, value])
