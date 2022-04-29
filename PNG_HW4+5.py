# Paragon National Group Spring 2022
# Computer Science / Data Science Track
# HW 4+5

# Assigned: April 29, 2022
# Due: May 4, 2022 11:59pm

# This is the fourth programming assignment of the computer science track.
# For each function, a skeleton is provided, where your job is to fill the *TODO* out.
# The questions will cover the topics learned in the fourth and fifth lecture, which 
# entailed object-oriented programming, graphs, and trees.

# This class includes all the functions needed for a graph, including __init__,
# addVertex, getVertices, edges, AddEdge, and findedges. Fill these functions
# out and add more functions if needed.
class graph:
    def __init__(self,gdict=None):
        #TODO
        return
    
    def addVertex(self, vrtx):
        #TODO
        return

    def getVertices(self):
        #TODO
        return

    def edges(self):
        #TODO
        return

    def AddEdge(self, edge):
        #TODO
        return
    
    def findedges(self):
        #TODO
        return

# This function takes in n (the number of cities), flights (a list of an int list
# showing the edges of the graph in the format [src, dst, price]), src (the starting
# city), dst (the destination), and K (the number of max stops). It outputs the
# the cheapest price and outputs -1 if there is no such route.
# Ex) cheapestflight(3, [[0,1,50],[1,2,350], [0,2,550]], 0, 2, 1) -> 400
#     cheapestflight(4, [[0,1,100],[0,2,200],[1,2,150],[1,3,200],[2,3,50]], 0, 3, 2) -> 250
#     cheapestflight(4, [[0,1,50],[1,3,350],[0,2,100],[2,3,200]], 0, 3, 0) -> -1
def cheapestflight(n, flights, src, dst, K):
    #TODO
    return