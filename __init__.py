from graph import *
from dijkstra import *

def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.addVertex(nodeid)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.getVertexByLabel(source)
        target = int(file.readline().split()[1])
        tv = graph.getVertexByLabel(target)
        length = float(file.readline().split()[1])
        edge = graph.addEdge(sv, tv, length)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    return graph

def println(dic):
    print("----------")
    for vertex in dic:
        print("%s: (%i, %s)" % (vertex, closed[vertex][0], closed[vertex][1]))
    print("----------")

graph = graphreader("simplegraph1.txt")
closed = dijkstra(graph, 1)
println(closed)

graph = graphreader("simplegraph2.txt")
closed = dijkstra(graph, 14)
println(closed)
