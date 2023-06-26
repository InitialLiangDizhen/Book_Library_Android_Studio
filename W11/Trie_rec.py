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

    def insert_recur(self, key, data=None):
        current = self.root
        self.insert_recur_aux(current, key, data)

    def insert_recur_aux(self, current, key, data=None):

        #base case
        if len(key) == 0:
            # reach the end of the key
            pass

        else:
            # find the index of the char with the ASCII value
            #since the link store them in order
            index = ord(key[0]) - 97 + 1

            #if path exit
            if current.link[index] is not None:
                current = current.link[index]

            #if path does not exist
            else:
                current.link[index] = Node()
                current = current.link[index]
                # recur with updated input
                self.insert_recur_aux(current, key[1:], data)

        char = key[0]
        index = ord(char) - 97 + 1

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