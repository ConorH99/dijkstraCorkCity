class Vertex:

    def __init__(self, label):
        self.label = label

    def __str__(self):
        outstr = str(self.label)
        return outstr

    def element(self):
        return self.label

class Edge:

    def __init__(self, label, x, y):
        self.label = label
        self.vertices = (x, y)

    def __str__(self):
        outstr = str(self.label)
        return outstr

    def vertices(self):
        return self.vertices

    def opposite(self, vertex):
        if vertex == self.vertices[0]:
            return self.vertices[1]
        elif vertex == self.vertices[1]:
            return self.vertices[0]
        return None

    def element(self):
        return self.label

class Graph:

    def __init__(self):
        self.structure = {}

    # Printing the dict form of the graph
    def __str__(self):
        outstr = "{ "
        for vertex in self.structure:
            outstr += str(vertex) + ": { "
            for opposite in self.structure[vertex]:
                outstr += str(opposite) + ": "
                outstr += str(self.structure[vertex][opposite]) + " "
            outstr += "} "
        outstr += "}"
        return outstr
        
    # Used to get a vertex node by passing in the label of that vertex
    def getVertexByLabel(self, label):
        for vertex in self.structure:
            if vertex.label == label:
                return vertex
        return None

    def vertices(self):
        vertexList = []
        for vertex in self.structure:
            vertexList.append(vertex)
        return vertexList

    def edges(self):
        edgeList = []
        for vertex in self.structure:
            for opposite in self.structure[vertex]:
                edgeList.append(self.structure[vertex][opposite])
        return edgeList

    def numVertices(self):
        vertexList = self.vertices()
        return len(vertexList)

    def numEdges(self):
        edgeList = self.edges()
        return len(edgeList)

    def getEdge(self, v, w):
        return self.structure[v][w]

    def degree(self, v):
        count = 0
        for w in self.structure[v]:
            count += 1
        return count

    def getEdges(self, v):
        edgeList = []
        for w in self.structure[v]:
            edgeList.append(self.structure[v][w])
        return edgeList

    def addVertex(self, label):
        v = Vertex(label)
        self.structure[v] = {}
        return v

    def addEdge(self, v, w, label):
        e = Edge(label, v, w)
        self.structure[v][w] = e
        self.structure[w][v] = e
        return e
class Vertex:

    def __init__(self, label):
        self.label = label

    def __str__(self):
        outstr = str(self.label)
        return outstr

    def element(self):
        return self.label

class Edge:

    def __init__(self, label, x, y):
        self.label = label
        self.vertices = (x, y)

    def __str__(self):
        outstr = str(self.label)
        return outstr

    def vertices(self):
        return self.vertices

    def opposite(self, vertex):
        if vertex == self.vertices[0]:
            return self.vertices[1]
        elif vertex == self.vertices[1]:
            return self.vertices[0]
        return None

    def element(self):
        return self.label

class Graph:

    def __init__(self):
        self.structure = {}

    # Printing the dict form of the graph
    def __str__(self):
        outstr = "{ "
        for vertex in self.structure:
            outstr += str(vertex) + ": { "
            for opposite in self.structure[vertex]:
                outstr += str(opposite) + ": "
                outstr += str(self.structure[vertex][opposite]) + " "
            outstr += "} "
        outstr += "}"
        return outstr
        
    # Used to get a vertex node by passing in the label of that vertex
    def getVertexByLabel(self, label):
        for vertex in self.structure:
            if vertex.label == label:
                return vertex
        return None

    def vertices(self):
        vertexList = []
        for vertex in self.structure:
            vertexList.append(vertex)
        return vertexList

    def edges(self):
        edgeList = []
        for vertex in self.structure:
            for opposite in self.structure[vertex]:
                edgeList.append(self.structure[vertex][opposite])
        return edgeList

    def numVertices(self):
        vertexList = self.vertices()
        return len(vertexList)

    def numEdges(self):
        edgeList = self.edges()
        return len(edgeList)

    def getEdge(self, v, w):
        return self.structure[v][w]

    def degree(self, v):
        count = 0
        for w in self.structure[v]:
            count += 1
        return count

    def getEdges(self, v):
        edgeList = []
        for w in self.structure[v]:
            edgeList.append(self.structure[v][w])
        return edgeList

    def addVertex(self, label):
        v = Vertex(label)
        self.structure[v] = {}
        return v

    def addEdge(self, v, w, label):
        e = Edge(label, v, w)
        self.structure[v][w] = e
        self.structure[w][v] = e
        return e