

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
        self.array = [(None,None)]    #simplify calculation, otherwise, 1//2 = 0, 2//2 = 1, (not the same parent)
        self.length = 0    #start from 1, 2//2 = 1, 3//2 = 1, (same parent)
        self.index_array = [None] * vertices_count   #index_array： index - id of vertices, value - position of vertices in min heap
        self.maxsize = vertices_count + 1 #index 0 is None,
       
    def insert(self, v_id, value):
        """
        Add an element to MinHeap's array
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        vv = (v_id, value)
        self.length += 1
        self.array += [vv]
         #append to the end of array
        self.index_array[v_id] = self.length #update index_array
        print("insert: " + str(v_id) + ", weight:  " + str(value) + ", pos: " + str(self.length))

        if self.length > 1: #if there is more than one element in the array
            self.rise(self.length) 
    
        
    def serve(self):
        """
        Removes and returns the smallest number in the MinHeap's array
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        print("serving")
        vertex_id = self.array[1][0] #get the id of the vertex
        
       
        self.swap(1, self.length) #since self.length was -=1, need +=1 to make is last element
        self.length -= 1 #avoid swapping with the one should be popped out in the sink
        #swap the minimum to the end, easy to loss, less change needed to the MinHeap
        self.sink(1)   #since it was at the end (one of biggest element), need to sink back to correct position
        #only sink when there is more than one element in the array
        
        #lose from root would need a lot of comparison
        print("serve: " + str(vertex_id) + ", length: " + str(self.length))
        self.index_array[vertex_id] = None #set to None, since it is not in the heap anymore
        return self.array.pop() #pop out the minimum #
    

    def swap(self, x, y):
        #just swap the position between two vertices
        """
        Swap two number's position in the minheap array
        Time Complexity: O(1)
        """
        self.index_array[self.array[x][0]] = y #update index_array
        self.index_array[self.array[y][0]] = x #update index_array
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def update(self, vertex_id, value):
        heap_pos = self.index_array[vertex_id] #replace old tuple with new tuple
        print(f"update: vertex: {vertex_id}, weight: {value}, heap pos: {heap_pos}")
        self.array[heap_pos] = (vertex_id, value) #update on the heap
        self.rise(heap_pos) #rise to correct position 
        #only update when the new value is smaller than the old one

    
    def rise(self, element): #rise new node to the correct position by comparing with its parent and another node
        """
        Adjusts the position of the element accordingly
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """

        tv = self.array[element][0]
        parent = element // 2    #parent's position is //2 left child's position
        print("parent: " + str(parent))
        v_id = self.array[element][0]
        print("self.length: " + str(self.length) )

        while parent>=1: #make sure parent is not, must start from index 1

            if  self.array[element][1] < self.array[parent][1]: #comparign weight of edge to themselves
                print("rise: vertex: " + str(v_id) + " pos: " + str(element))

                self.swap(element,parent)

                element = parent 
                parent = element // 2
                print("rise: element new pos:" + str(self.index_array[tv]))
                
            else:
                break


    
    def sink(self, element): 
        """ 
        Adjusts the position of the element accordingly
        Time Complexity: O(log V), where V is the number of elements in the MinHeap
        """
        child = 2*element 
        #improved version:
                
        while child < self.length: #since start from 1
                #avoid swapping the one that should be popped out(minimum)
            if self.array[child+1][1]< self.array[child][1]: 
                #checks if the right child exists  #compare left and right child which is smaller
                child += 1 #if right child is smaller, then switch to right child, 
                #smaller child be the parent
            if self.array[element][1] > self.array[child][1]: #then parent < left child
                self.swap(element, child)
                element = child  #switch pointer to correct position
                child = 2*element 
            else:
                break
    

    def test_serve(self):
        min_heap = MinHeap(10)
        min_heap.insert(1, 5)
        min_heap.insert(2, 3)
        min_heap.insert(3, 17)
        min_heap.insert(4, 10)
        min_heap.insert(5, 84)
        min_heap.insert(6, 19)
        min_heap.insert(7, 6)
        min_heap.insert(8, 22)
        min_heap.insert(9, 9)

        self.assertEqual(min_heap.serve(), (2, 3))
        self.assertEqual(min_heap.serve(), (1, 5))
        self.assertEqual(min_heap.serve(), (7, 6))






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
        #for traversal
        self.discovered = False
        self.visited = False
        #distance for un weighted and weighted
        self.distance = 0
        #backtracking/where i was from
        self.previous = None
        #colourability
        #self.colour = Null

    def __str__(self):
        return_string = str(self.id) #print self.id
        #return_string = return_string + "\n with edges: " + str(self.edges)#this print the edges address
        for i in range(len(self.edges)):
            return_string = return_string + "\n with edges: " + str(self.edges[i])
            # return_special = return_string + "\n with special edges: " + str(self.speciaEdge)
        return return_string

    def added_to_queue(self):
        self.discovered = True
    
    def visited(self):
        self.visited = True
    
    def add_edge(self, edge):
        self.edges.append(edge)


    # def get_distance(self):
    #     return self.distance
    
    # def set_distance(self, distance):
    #     self.distance = distance
    #backtracking, where i was from
    #self.previous = None




class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w #weight

    def __str__(self):
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string

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

class Graph:

    def __init__(self, argv_vertices_count): #list of vertices
        self.max_vertices = (argv_vertices_count + 1)*2
        self.mirror_vertice = argv_vertices_count + 1
        self.actualSize = self.max_vertices//2

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
            
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)  #add correspoding edge to each u(starting vertex of edge)

            #mirror vertices
            current_vertex = self.vertices[u + self.mirror_vertice]
            current_speical_edge = Edge(u+self.mirror_vertice,v+self.mirror_vertice,st)
            current_vertex.add_edge(current_speical_edge)

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

        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        source.distance = 0; #source from source, distance = 0
        
        # discovered =MinHeap(), begin by put source into it
        discovered = MinHeap(self.max_vertices)
        discovered.insert(source.id, source.distance) #(key, data), smaller key closer to front of heap
        
        while discovered.length > 0: #.length for heap
             u_v, weight = discovered.serve() #serve()

             u = self.vertices[u_v] #retrieve vertex from the list
             u.discovered = True
             u.visited = True 

             print("\n dijastr actual serve vertex: " + str(u.id) + "\n")
             
            #carPoolLink
             if u.passenger == True:
                u.accompany = True
                #add Link between actual vertices and mirrored vertices
                u.add_edge(Edge(u.id, u.id + self.mirror_vertice, 0))
             
             if u.accompany == True:
                v.accopany = True
            
             useEdge = u.edges

            # Add a print statement here to see which edges are being used
             print(f"Vertex: {u.id}, Edges: {[str(edge) for edge in useEdge]}")

            #discovered stage
             for edge in useEdge:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]
                 
                 if u.accompany == True:
                     v.accompany = True
                     

                 if v.discovered == False: #just to be safe
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
                     v.distance = u.distance + edge.w
                     #update continous time taken each vertex in self.verteices

                     #update heap after update v.previous
                     discovered.insert(v.id, v.distance)
                     #insert vertex with continuous time taken
                     #first time update from inf to exact distance value

                     
                     #Backtracking

                    #  print(self.actualSize)
                    #  u_acId = 0
                    #  v_acId = 0
                    
                    #  if u.id >= self.actualSize and v.id >= self.actualSize:
                    #     u_acId = u.id - self.actualSize
                    #     v_acId = v.id- self.actualSize
                    #     self.vertices[v_acId].previous = self.vertices[u_acId]
                    #     print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")
                        
                    #  elif u.id >= self.actualSize:
                    #     u_acId = u.id - self.actualSize
                    #     v_acId = v.id
                    #     self.vertices[v_acId].previous = self.vertices[u_acId]
                    #     print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")

                    #  elif v.id >= self.actualSize:
                    #     u_acId = u.id
                    #     v_acId = v.id-self.actualSize
                    #     self.vertices[v_acId].previous = self.vertices[u_acId]
                    #     print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")
                    #  else:
                    #     v.previous = u
                    #     print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")

                     
            
            #visiting stage
                 else: # if v is discovered #if i find a shorter one, change it
                     if v.visited == False:
                        if v.distance > u.distance + edge.w:
                            #update distance
                            v.distance = u.distance + edge.w
                        
                        print(self.actualSize)
                        
                        if u.id >= self.actualSize and v.id >= self.actualSize:
                            u_acId = u.id - self.actualSize
                            v_acId = v.id- self.actualSize
                            self.vertices[v_acId].previous = self.vertices[u_acId]
                            print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")
                        
                        elif u.id >= self.actualSize:
                            u_acId = u.id - self.actualSize
                            v_acId = v.id
                            self.vertices[v_acId].previous = self.vertices[u_acId]
                            print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")

                        elif v.id >= self.actualSize:
                            u_acId = u.id
                            v_acId = v.id-self.actualSize
                            self.vertices[v_acId].previous = self.vertices[u_acId]
                            print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")
                        else:
                            v.previous = u
                            u_acId = u.id
                            v_acId = v.id-self.actualSize
                            print("\nprevious vertex: "+ str(u_acId) + "\n"  + ", origin vertex: " + str(v_acId) + "\n")
                    
                            #update heap
                        discovered.update(v.id,v.distance)
                            #not visited -> distance not finalised
        
        return self.backtracking(destination)           
                        #carPoolLink is not openned somehow

    
    def backtracking(self,destination, path = []):
        current = self.vertices[destination]

        if current is not None:
            path.append(current.id)
            
        if current.previous is not None:
            pre = self.backtracking(current.previous.id, path)
     
        return path
    
if __name__ == "__main__":
    a = [(0,3,5,3), (3,4,35,15),(3,2,2,2),(4,0,15,10),
         (2,4,30,25),(2,0,2,2),(0,1,10,10),(1,4,30,20)]

    p = [2,1]

    oR = optimalRoute(0,4,p,a)
    print(oR)
    
   
    
    


    