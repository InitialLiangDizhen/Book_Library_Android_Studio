from multiprocessing.heap import Heap
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


class Vertex:

    def __init__(self,id): #constructor
        self.id = id
        #list
        self.edges = []
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
        for edge in self.edges:
            return_string = return_string + "\n with edges: " + str(edge) #print edge one by one
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

class Graph:
    
    def __init__(self, argv_vertices_count): #list of vertices
        #array
        self.vertices = [None] * argv_vertices_count #list of vertices
        for i in range(argv_vertices_count):
            self.vertices[i] = Vertex(i)


    def __str__(self):  
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex" + str(vertex) + "\n"
        return return_string     #Vertex0,\nVertex1, Vertex2, Vertex3, Vertex4, Vertex5, Vertex6, Vertex7, Vertex8, Vertex9
    
    def add_edge(self, argv_edges, argv_directed=True): #list of edges for the graph, a
        for edge in argv_edges:
            u = edge[0] #u is the vertex id
            v = edge[1]
            w = edge[2]
            current_edge = Edge(u,v,w) #create edge for vertex u to vertex v with weight w
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)  #add correspoding edge to each u(starting vertex of edge)

            #undirected graph add v to u
            if not argv_directed: #if not directed
                current_edge = Edge(v,u,w) #create edge for vertex u to vertex v with weight w
                current_vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)  #add correspoding edge to each u(starting vertex of edge)


    #BFS is an algorithm for traversing or searching tree 
    #or graph data structures. It starts at the tree root 
    #(or some arbitrary node of a graph) and explores all of the neighbor 
    # nodes at the present depth level before moving on to the nodes at the 
    # next depth level. BFS uses a queue data structure to keep track of the 
    # nodes to be visited. When BFS reaches a dead end (i.e., a node with no unvisited 
    # neighbors), it simply moves on to the next node in the queue and continues the 
    # search from there. The algorithm continues in this manner until all nodes have been 
    # visited or a solution has been found. Is there anything else you would like to know?
    def bfs(self, source):
        """
        starting from source, visit all vertices in the graph
        """
        self.reset() #reset all vertices to undiscovered and unvisited
        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        return_bfs = []
        discovered=[]
        discovered.append(source)
        
        while len(discovered) > 0:
             u = discovered.pop(0) #serve()\
             u.visited = True
             return_bfs.append(u)
             for edge in u.edges:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]
                 if v.discovered == False and v.visited == False: #just to be safe
                     discovered.append(v)
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
        return return_bfs
    
    def bfs_colour(self, source):
        """
        starting from source, visit all vertices in the graph
        """
        self.reset() #reset all vertices to undiscovered and unvisited
        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        #colourability Tut5_Q5
        #source.colour = "Black"
        return_bfs = []
        discovered=[]
        discovered.append(source)
        
        while len(discovered) > 0:
             u = discovered.pop(0) #serve()\
             u.visited = True
             return_bfs.append(u)
             for edge in u.edges:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]
                 if v.discovered == False and v.visited == False: #just to be safe
                     #colourability Tut5_Q5
                     #if u.colour = "Black"
                        #v.clour = "Blue"
                     discovered.append(v)
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
        return return_bfs

    #undirected cycle finding
    def bfs_cycle(self, source):
        """
        starting from source, visit all vertices in the graph
        """
        self.reset() #reset all vertices to undiscovered and unvisited
        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        return_bfs = []
        discovered=[]
        discovered.append(source)
        
        while len(discovered) > 0:
             u = discovered.pop(0) #serve()\
             u.visited = True
             return_bfs.append(u)
             for edge in u.edges:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]
                 
                #undirected cycle finding
                 if v.discovered == True:
                     print("Cycling graph")
                     
                 elif v.discovered == False and v.visited == False: #just to be safe
                     discovered.append(v)
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
        return return_bfs
    
    #bfs shortest cycle
    def bfs_sc(self, source):
        """
        starting from source, visit all vertices in the graph
        """
        self.reset() #reset all vertices to undiscovered and unvisited
        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        source.distance = 0
        return_bfs = []
        discovered=[]
        discovered.append(source)
        
        while len(discovered) > 0:
             u = discovered.pop(0) #serve()\
             u.visited = True
             return_bfs.append(u)
             for edge in u.edges:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]
                                #undirected cycle finding

                 if source == v:
                     print("Cycling graph")
                     return source.distance
                 
                 elif v.discovered == False and v.visited == False: #just to be safe
                     discovered.append(v)
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
                     v.distance = u.distance + 1
                     
        return return_bfs
    
    # def bfs_distance(self, source): bfs not work on weighted edge
    def bfs_distance(self, source): #bfs just find the path that has smallest number of edges
        """
        starting from source, visit all vertices in the graph
        """
        self.reset() #reset all vertices to undiscovered and unvisited
        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        #source.distance = 0, not needed if default value is 0
        return_bfs = []
        discovered=[]
        discovered.append(source)
        
        while len(discovered) > 0:
             u = discovered.pop(0) #serve()\
             u.visited = True
             return_bfs.append(u)
             for edge in u.edges:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]
                 if v.discovered == False and v.visited == False: #just to be safe
                     discovered.append(v)
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
                     v.distance = u.distance + 1
                     #for backtracking
                     v.previous = u
        return return_bfs

    

    def reset(self):
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False

    
    def dfs(self, source):
        """
        dfs_not recursion
        """
        self.reset()
        source = self.vertices[source]
        
        return_dfs = []
        discovered=[]
        discovered.append(source) #append = push

        while len(discovered) > 0:
             u = discovered.pop() #pop() last item
             u.visited = True
             return_dfs.append(u)

             for edge in u.edges:
                 v = edge.v #v is the number of vertex id
                 v = self.vertices[v]

                 if v.discovered == False and v.visited == False:
                     discovered.append(v)
                     v.discovered = True
        return return_dfs
    
    #iteration
    def dfs(self, source):
        """
        dfs_not recursion
        """
        self.reset()
        source = self.vertices[source]
        
        return_dfs = []
        discovered=[]
        discovered.append(source) #append = push
        while len(discovered) > 0:
             u = discovered.pop() #pop() last item
             u.visited = True
             return_dfs.append(u)
             for edge in u.edges:
                 v = edge.v #v is the number of vertex id
                 v = self.vertices[v]
                #undirected cycle finding, only for undirectly, since reaching the same vertex meaning the go and come from the vertex, so form a complete cycle
                 #if v.discovered = True:
                    #print("undirected cycling graph")
                 if v.discovered == False and v.visited == False:
                     discovered.append(v)
                     v.discovered = True
        return return_dfs
    
    
    #recursion
    def dfs_self(self, source):  #loop it self

        #make vertex from number
        u = self.vertices[source]
        
        current_dfs = []
        next_dfs = []
        u.visited = True
        current_dfs.append(u)
        
        #check available edges and the correponding v
        for edge in u.edges:
            v = edge.v
            v = self.vertices[v]

            #for directed cycle_detection
            #u.active = True, u to v, set u.status active v -> d, set v.status active
            #if there is a edge between u to v, set u.active = True
            
            #if v.visied == True v.active == True 
            #print("directed cycling graph")

            #check whether it is visited or not
            #elif v.visited == False:
            #   next_dfs =self.dfs_self(v.id)
            if v.visited == False: #to avoid cycling back to the vertex that is visted already
                next_dfs = self.dfs_self(v.id)

        #for directed cycle_detection
        #u.active = False
            current_dfs += next_dfs
        return current_dfs
    

    

    #tail_recursion
    def dfs_aux(self, source):
        self.reset()    

        #make vertex from number
        u = self.vertices[source]
        current_dfs = []
        u.visited = True
        current_dfs.append(u)
        
        #check available edges and the correponding v
        for edge in u.edges:
            v = edge.v
            v = self.vertices[v]
            
            #check whether it is visited or not
            if v.visited == False: #to avoid cycling back to the vertex that is visted already
                self.dfs_recursion(v.id, current_dfs)

        return current_dfs
    
    
    #tail_recursion
    def dfs_recursion(self, current_vertex, current_dfs): #stack in recursion as as discovered stack

        #make vertex from number
        u = self.vertices[current_vertex]
        u.visited = True
        current_dfs.append(u)

        for edge in u.edges:
            v = edge.v
            v = self.vertices[v]

            if v.visited == False: #to avoid cycling back to the vertex that is visted already
                self.dfs_recursion(v.id, current_dfs) #must use self. to be self-aware

        return current_dfs
    






# class Graph_matrix:
#     def __init__(self, V):
#         self.matrix = [None] * len(V)
#         for i in range(len(V)):
#             self.matrix[i] = [None] * len(V)





    
if __name__ == "__main__":
    total_vertices = 10
    my_graph = Graph(total_vertices)
    print(my_graph)
    
    #edges
    edges = []   #from 3 to 1, can not 1 to 3 for this, bfs must be unique, either 1 to 3 or 3 to 1
    # edges.append((1,2,1)) #u, v, w = from vertex 3 to vertex 1 with weight 5
    # edges.append((2,3,1))
    # edges.append((3,4,1)) #vertex 3 has 2 reference address so two objects
    # edges.append((4,5,1))
    # edges.append((5,6,1))
    # edges.append((6,7,1)) 
    # edges.append((1,8,1))
    # edges.append((8,9,1))
    # edges.append((9,4,1))

    edges.append((1,8,1))
    edges.append((8,9,1))
    edges.append((9,4,1))
    edges.append((1,2,1)) #if this edge exist, 1,2,3,4,5,6,7,8,9 is one of the correct answer
    edges.append((2,3,1))
    edges.append((3,4,1))
    edges.append((4,5,1))
    edges.append((5,6,1))
    edges.append((6,7,1))

    #create proper edges

    my_graph.add_edge(edges)
    print(my_graph)

    #run BFS 
    # for vertex in range(total_vertices):
    #     print(str(vertex) + " infected " + str(len(my_graph.bfs(vertex)))) #start different vertex in undirected graph would result different f=bfs_list
    #as some vertex can not reach other vertex 3 -> len 5, 1 -> len 3
    # bla = my_graph.bfs(3) #return_bfs list
    # for vertex in bla:
    #     print(vertex)

    #run DFS
    dfs_list = my_graph.dfs_aux(1)
    for v in dfs_list:
        print(v.id)

    