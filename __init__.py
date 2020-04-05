from roadmap import *

def graphreader(file):
    graph = Graph()
    infile = open(file, "r")
    line = infile.readline()
    num = 0
    while line == "Node\n":
        num += 1
        line = infile.readline().strip().split(" ")
        id = int(line[1])
        line = infile.readline().strip().split(" ")
        lat = float(line[1])
        long = float(line[2])
        v = graph.addVertex(id, lat, long)
        line = infile.readline()
    num = 0
    while line == "Edge\n":
        num += 1
        line = infile.readline().strip().split(" ")
        src = int(line[1])
        srcv = graph.getVertexByLabel(src)
        line = infile.readline().strip().split(" ")
        tgt = int(line[1])
        tgtv = graph.getVertexByLabel(tgt)
        infile.readline()
        line = infile.readline().strip().split(" ")
        time = float(line[1])
        graph.addEdge(srcv, tgtv, time)
        infile.readline()
        line = infile.readline()
    return graph


routemap = graphreader("corkCityData.txt")
print(routemap.numVertices(), routemap.numEdges())
ids = {}
ids['wgb'] = 1669466540
ids['turnerscross'] = 348809726
ids['neptune'] = 1147697924
ids['cuh'] = 860206013
ids['oldoak'] = 358357
ids['gaol'] = 3777201945
ids['mahonpoint'] = 330068634
sourcestr = "wgb"
deststr= "neptune"
source = ids[sourcestr]
dest = ids[deststr]
tree = routemap.shortestPath(source,dest)
routemap.printShortestPathList(tree)