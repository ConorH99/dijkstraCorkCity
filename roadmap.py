from graph import *

class Vertex(Vertex):
    
    def __init__(self, label):
        super().__init__(label)

class Edge(Edge):

    def __init__(self, v, w, label):
        super().__init__(v, w, label)

class Graph(Graph):

    def __init__(self):
            super().__init__()
            self.coordinates = {}
            self.labelToVertex = {}

    def __str__(self):
        if self.numEdges() <= 100 and self.numVertices() <= 100:
            outstr = "{ "
            for vertex in self.structure:
                outstr += str(vertex) + ": { "
                for opposite in self.structure[vertex]:
                    outstr += str(opposite) + ": "
                    outstr += str(self.structure[vertex][opposite]) + " "
                outstr += "} "
            outstr += "}"
            return outstr
        return None

    def getVertexByLabel(self, label):
        if label in self.labelToVertex:
            return self.labelToVertex[label]
        return None

    def addVertex(self, label, lat, long):
            v = Vertex(label)
            self.coordinates[v] = (lat, long)
            self.structure[v] = {}
            self.labelToVertex[label] = v
            return v

    def addVertexIfNew(self, label, lat, long):
        for v in self.structure:
            if v.label == label:
                return None
        return self.addVertex(label, lat, long)

def graphreader(file):
    graph = Graph()
    infile = open(file, "r")
    line = infile.readline()
    while line == "Node\n":
        line = infile.readline().strip().split(" ")
        id = line[1]
        line = infile.readline().strip().split(" ")
        lat = line[1]
        long = line[2]
        v = graph.addVertexIfNew(id, lat, long)
        line = infile.readline()
    while line == "Edge\n":
        line = infile.readline().strip().split(" ")
        src = line[1]
        srcv = graph.getVertexByLabel(src)
        line = infile.readline().strip().split(" ")
        tgt = line[1]
        tgtv = graph.getVertexByLabel(tgt)
        infile.readline()
        line = infile.readline().strip().split(" ")
        time = line[1]
        graph.addEdge(srcv, tgtv, time)
        infile.readline()
        line = infile.readline()
    return graph


graph = graphreader("Dijkstra-Cork-City\simpleroute.txt")
print(graph)




