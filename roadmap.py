from graph import *
from dijkstra import *

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
        if label not in self.labelToVertex:
            return self.addVertex(label, lat,long)
        return None

    def shortestPath(self, v, w):
        sp = dijkstra(self, v)
        shortestPathList = []
        self.shortestPathListBuilder(v, w, shortestPathList, sp)
        shortestPathList.reverse()
        return shortestPathList

    def shortestPathListBuilder(self, v, w, spList, sp):
        ''' Takes the shortest path to all reachable vertices from the dijksta output, and restricts it
            from the start vertex "v" to a vertex of choice "w". Builds a list with each index formed by
            ("v", "Cost to that vertex from start vertex). Then reverses the list  '''
        spList.append((w, sp[w][0]))
        if w == v:
            return spList
        else:
            return self.shortestPathListBuilder(v, sp[w][1], spList, sp)

    def printShortestPathList(self, list):
        ''' Prints out the name of each vertex and the latitude and the longitude associated with each vertex. 
            This output can be entered into the textbox for https://www.gpsvisualizer.com/map_input?form=google
            to visualise it on a map '''
            
        outstr = "Name,Latitude,Longitude\n"
        for vertex in list:
            v = self.getVertexByLabel(vertex[0])
            latitude = self.coordinates[v][0]
            longitude = self.coordinates[v][1]
            outstr += "%s,%s,%s\n" %(v.element(), latitude, longitude)
        print(outstr)
