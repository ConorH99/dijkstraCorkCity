from apq import  *

def dijkstra(graph, s):
    open = APQ()
    locs = {}
    closed = {}
    preds = {s: None}

    svertex = graph.getVertexByLabel(s)
    elt = open.add(0, s)
    locs[s] = elt
    while open.length() != 0:
        vElt = open.remove_min()
        v = vElt.value
        vvertex = graph.getVertexByLabel(v)
        vcost = vElt.key
        locs.pop(v)
        predecessor = preds.pop(v)
        closed[v] = (vcost, predecessor)
        edges = graph.getEdges(graph.getVertexByLabel(v))
        for edge in edges:
            w = edge.opposite(vvertex)
            if w.element() not in closed:
                ecost = edge.element()
                newcost = vcost + ecost
                if w.element() not in locs:
                    preds[w.element()] = v
                    elt = open.add(newcost, w.element())
                    locs[w.element()] = elt
                elif newcost < locs[w.element()].key:
                    preds[w.element()] = v
                    locs[w.element()].key = newcost
    return closed