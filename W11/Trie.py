class Node:
    def __init__(self, data =None, level=None, size = 27):
        #terminal $ at index 0 +  lp + up
        self.link = [None] * size #link stores $ + 27 characters in order
        #data want to store
        self.data = data
        #level of node
        self.level = level

class Trie:
    def __init__(self):
        self.root = Node(level=0)

    def insert(self, key, data=None):
        count_level = 0
        # start ffrom the root
        current = self.root

        #go through the key 1 by 1
        for char in key:
            # calculate index
            # $ = 0, a = 1, b = 2, c = 3
            index = ord(char) - 97 + 1 #shift by 1


            #if path exit
            if current.link[index] is not None:
                current = current.link[index]

            #if path does not exist
            else:
                #create a new node
                current.link[index] = Node(level=count_level)
                current = current.link[index]
                #Trie level
            count_level +=1


        #after finish the given string (list of chars)
        #check if there is a $
        #go through the terminal $
        index = 0
        if current.link[index] is not None:
            current = current.link[index]

        # if path does not exist
        else:
            # create a new node
            current.link[index] = Node(level=count_level)
            current = current.link[index]

        #add in the payload, frequency in assignment
        current.data = data

    def search(self, key):
        # start ffrom the root
        current = self.root

        #go through the key 1 by 1
        for char in key:
            print(current.level)
            # calculate index
            # $ = 0, a = 1, b = 2, c = 3
            index = ord(char) - 97 + 1 #shift by 1

            #if path exit
            if current.link[index] is not None:
                current = current.link[index]

            #if path does not exist
            else:
                raise Exception(str(key) + " doesn't exist")

        #after finish the given string (list of chars)
        #check if there is a $
        #go through the terminal $, index = 0

        print(current.level)

        # terminal $ index
        index = 0
        if current.link[index] is not None:
            #traverse to terminal node (leaf node0
            current = current.link[index]
        else:
            #to diffentiate None item from None from not such key
            raise Exception(str(key) + " doesn't exist")

        # now we are at the leaf node(terminal)
        return current.data

if __name__ == '__main__':
    bla = Trie()
    bla.insert("lo", "123")
    bla.insert("loa", "456")
    bla.insert("lol", "789")
    bla.insert("uwusdwfg", None)

    try:
        print(bla.search("lol"))
    except Exception as e:
        print(e)

    try:
        print(bla.search("loa"))
    except Exception as e:
        print(e)

    try:
        print(bla.search("uwusdwfg"))
    except Exception as e:
        print(e)

    try:
        print(bla.search("los"))
    except Exception as e:
        print(e)