class Graph:
    #this class is to be used as a discrete graph to model the map of the world
    #each node has it's key (name), and a list of the adjacent nodes as the value

    #nodes should be a dictionary type
    def __init__(self,nodes):
        self.nodes = nodes

    #adds new node(key/value pair) to the dictionary
    def add_node(self,key,value):
        self.nodes[key] = value

    #deletes the node corresponding to the key
    def delete_node(self,key):
        self.nodes.pop(key)

    def print_graph(self):
        print(self.nodes)
