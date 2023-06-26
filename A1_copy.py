

class MinHeap():
    def __init__(self, vertices_count):
        """
        Constructor for MinHeap (Fixed Heap)
        """
        #fixed heap: array size is fixed, no need to insert
        #save index 0 as None since 1//2 = 0
        #inf for dijakstra, 
        #leave index 0 as None, since 1//2 = 0
        #MinHeap: key - id of vertices, value - weight of edge to this vertex (key, value) = (id, weight)
        self.array = [(None,None)]   #simplify calculation, otherwise, 1//2 = 0, 2//2 = 1, (not the same parent)
        self.length = 0    #start from 1, 2//2 = 1, 3//2 = 1, (same parent)
        self.index_array = [None] * vertices_count   #index_array： index - id of vertices, value - position of vertices in min heap
        self.maxsize = vertices_count + 1 #index 0 is None,
       
    
   
    def insert(self, v_id, value):
        """
        Add an element to MinHeap's array
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        print("insert: " + str(v_id))

        vv = (v_id, value)
        self.array.append(vv) #append to the end of array
        self.length += 1 
        self.index_array[v_id] = self.length #update index_array

        if self.length > 1: #if there is more than one element in the array
            self.rise(self.length) 
    
        
    def serve(self):
        """
        Removes and returns the smallest number in the MinHeap's array
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        vertex_id = self.array[1][0] #get the id of the vertex
        print("serve: " + str(vertex_id))

        self.length -= 1           #lose from root would need a lot of comparison
        print(self.length)

        if self.length > 0: 
            self.swap(1, self.length+1) #since self.length was -=1, need +=1 to make is last element
            #swap the minimum to the end, easy to loss, less change needed to the MinHeap
            self.sink(1)   #since it was at the end (one of biggest element), need to sink back to correct position
            #only sink when there is more than one element in the array

        self.index_array[vertex_id] = None #set to None, since it is not in the heap anymore
        return self.array.pop() #pop out the minimum #


    def swap(self, x, y):
        #just swap the position between two vertices
        """
        Swap two number's position in the minheap array
        Time Complexity: O(1)
        """
        v_id = self.array[x][0]
        print("before swap: element: " + str(v_id) + "pos: " + str(self.index_array[v_id]))
        v2_id = self.array[y][0]

        self.array[x], self.array[y] = self.array[y], self.array[x]

        #for tracking in index_array
        
        self.index_array[v_id] = y
        
        print("after swap: element: " + str(v_id)  + "pos: " + str(self.index_array[v_id]))
        self.index_array[v2_id] = x


    def update(self, vertex_id, value):
        heap_pos = self.index_array[vertex_id] #replace old tuple with new tuple
        print(heap_pos)
        self.array[heap_pos] = (vertex_id, value) #update on the heap
        self.rise(heap_pos) #rise to correct position 
        #only update when the new value is smaller than the old one

    
    def rise(self, element): #rise new node to the correct position by comparing with its parent and another node
        """
        Adjusts the position of the element accordingly
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        parent = element // 2    #parent's position is //2 left child's position
        
        
        print("rise: heap pos: " + str(element))
        while parent >= 1: #make sure parent is not, must start from index 1

            if self.array[parent][1] > self.array[element][1]: #comparign weight of edge to themselves
                print("rise: element: " + str(self.array[element][0]))
                print("rise: parent: " + str(self.array[parent][0]))
                self.swap(element,parent)
                element = parent 
                print("rise: new pos:" + str(element))
                
            else:
                break


    
    def sink(self, element): 
        """ 
        Adjusts the position of the element accordingly
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        child = 2*element 
        #improved version:
                
        while child <= self.length: #since start from 1
                #avoid swapping the one that should be popped out(minimum)
            if child < self.length and self.array[child+1][1]< self.array[child][1]: 
                #checks if the right child exists  #compare left and right child which is smaller
                child += 1 #if right child is smaller, then switch to right child, 
                #smaller child be the parent
            if self.array[element][1] > self.array[child][1]: #then parent < left child
                self.swap(element, child)
                element = child  #switch pointer to correct position
                child = 2*element 
            else:
                break
    




#What else is needed for dijkstra?
"""
1) Modify the MinHeap implementation to accoutn for vertices
2) Write the update function. What happens when the vertex's length is updated?
3) Account for vertex's index

Assignment1
1. directed graph
1. store <a,b,c,d) attributes in edge
2. store lists of edge in vertex, adjacent list I guess
3. need to build own graph
reverse graph is possible, by fliping (a,b,c,d) to (b,a,c,d
get multipleverses (in node a, if go link1 to b, what if I go link2 to c) of route-choosing for graph
only reverse the one route in each verse at a time
layered graph = multipleverse graph

inputs, multiple start to end (intermediate stops (nodes    ))
"""

class Vertex:

    def __init__(self,id): #constructor
        self.id = id
        #list
        self.edges = []

        self.passenger = False
        self.accompany = False
        #self.speciaEdge
        self.speciaEdges = []
        #for traversal
        self.discovered = False
        self.visited = False
        #distance for un weighted and weighted
        self.distance = 0
        #backtracking/where i was from
        self.next = None
        #colourability
        #self.colour = Null

    def __str__(self):
        return_string = str(self.id) #print self.id
        #return_string = return_string + "\n with edges: " + str(self.edges)#this print the edges address
        for i in range(len(self.speciaEdges)):
            return_string = return_string + "\n with edges: " + str(self.edges[i]) + "\n with special edges: " + str(self.speciaEdges[i])  #print edge one by one + 
            # return_special = return_string + "\n with special edges: " + str(self.speciaEdge)
        return return_string

    def added_to_queue(self):
        self.discovered = True
    
    def visited(self):
        self.visited = True
    
    def add_edge(self, edge):
        self.edges.append(edge)

    def add_special_edge(self, edge):
        self.speciaEdges.append(edge)

    # def get_distance(self):
    #     return self.distance
    
    # def set_distance(self, distance):
    #     self.distance = distance
    #backtracking, where i was from
    #self.previous = None

#not counted in aux space
def optimalRoute(start, end, passengers, roads):
    max_vertices = -1

    for road in roads:
         s,e,nt,st = road
         
         if e > max_vertices:
            max_vertices = e
              
    graph = Graph(max_vertices)
    graph.add_Road(roads)

    graph.add_Passenger(passengers)
    dj = graph.dijkstra(start,end)
    return graph
    
    


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w #weight

    def __str__(self):
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string

class Graph:
    def __init__(self, argv_vertices_count): #list of vertices
        self.max_vertices = argv_vertices_count + 1

        #array
        self.vertices = [None] * self.max_vertices #list of vertices
        for i in range(self.max_vertices):
            self.vertices[i] = Vertex(i)

    def __str__(self):  
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex" + str(vertex) + "\n"
        return return_string     #Vertex0,\nVertex1, Vertex2, Vertex3, Vertex4, Vertex5, Vertex6, Vertex7, Vertex8, Vertex9
    
    def add_Road(self, roads, argv_directed=True): #list of edges for the graph, a
        for road in roads:
            u,v,nt,st = road
            current_edge = Edge(u,v,nt) #create edge for vertex u to vertex v with weight w
            current_speical_edge = Edge(u,v,st)
            current_vertex = self.vertices[u]

            current_vertex.add_edge(current_edge)  #add correspoding edge to each u(starting vertex of edge)
            current_vertex.add_special_edge(current_speical_edge)

    def add_Passenger(self, passenger):
        for p in passenger:
            self.vertices[p].passenger = True

    def reset(self):
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False

    def dijkstra(self, source, destination): #find the path that has smallest total weight of all edges 
        """
        starting from source, visit all vertices in the graph
        """
        #Backtracking list
        bl = []

        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        source.distance = 0; #source from source, distance = 0
        
        # discovered =MinHeap()
        discovered = MinHeap(self.max_vertices)
        discovered.insert(source.id, source.distance) #(key, data), smaller key closer to front of heap
        
        while discovered.length > 0:
             u_v, weight = discovered.serve() #serve()

             u = self.vertices[u_v] #retrieve vertex from the list
             u.visited = True 
             
             bl.append(u.distance)
             
             if u.id == destination:
                 return bl #return earlier
        
    
            #discovered stage
             for edge in u.edges:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]

                 if v.discovered == False: #just to be safe
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
                     v.distance = u.distance + edge.w
                     #update heap after update v.previous
                     discovered.insert(v.id, v.distance)
                     #first time update from inf to exact distance value
            
            #visiting stage
                 else: # if v is discovered
                    #if i find a shorter one, change it
                    if v.visited == False:
                        if v.distance > u.distance + edge.w:
                            #update distance
                            v.distance = u.distance + edge.w
                            v.previous = u
                            
                            #update heap
                            discovered.update(v.id,v.distance)
                            #not visited -> distance not finalised

        return bl


if __name__ == "__main__":
    a = [(0,3,5,3), (3,4,35,15),(3,2,2,2),(4,0,15,10),
         (2,4,30,25),(2,0,2,2),(0,1,10,10),(1,4,30,20)]

    p = [2,1]

    oR = optimalRoute(0,4,p,a)
    print(oR)
    
    


    