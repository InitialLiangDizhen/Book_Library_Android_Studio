class MinHeap():
    def __init__(self):
        """
        Constructor for MinHeap
        """
        self.array = [None]
        self.length = 0 
    
    def insert(self, element):
        """
        Add an element to MinHeap's array
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        self.array.append(element) #append to the end of array
        self.length += 1 
        self.rise(self.length) 
    
    def serve(self):
        """
        Removes and returns the smallest number in the MinHeap's array
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        self.swap(1, self.length)  #swap the minimum to the end, easy to loss, less change needed to the MinHeap
        self.length -= 1           #lose from root would need a lot of comparison
        self.sink(1)   #since it was at the end (one of biggest element), need to sink back to correct position
        return self.array.pop() #pop out the minimum #


    def swap(self, x, y):
        #just swap the position between two vertices
        """
        Swap two number's position in the minheap array
        Time Complexity: O(1)
        """
        self.array[x], self.array[y] = self.array[y], self.array[x]
    
    def rise(self, element): #rise new node to the correct position by comparing with its parent and another node
        """
        Adjusts the position of the element accordingly
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        parent = element // 2    #parent's position is //2 left child's position
        while parent >= 1:
            if self.array[parent] > self.array[element]:
                self.swap(parent, element)
                element = parent 
                parent = element // 2
            else:
                break
    
    def sink(self, element): 
        """ 
        Adjusts the position of the element accordingly
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        child = 2*element 
        #improved version:
            
        # while child < self.length: 
        #   if self.array[child+1] < self.array[child]: #make sure left child < right child, 

        while child <= self.length: 
                #avoid swapping the one that should be popped out(minimum)
            if child < self.length and self.array[child+1] < self.array[child]: #make sure left child < right child, 
                child += 1 
            if self.array[element] > self.array[child]: #then parent < left child
                self.swap(element, child)
                element = child  #switch pointer to correct position
                child = 2*element 
            else:
                break
    
    # def update(self):



#What else is needed for dijkstra?
"""
1) Modify the MinHeap implementation to accoutn for vertices
2) Write the update function. What happens when the vertex's length is updated?
3) Account for vertex's index
"""

