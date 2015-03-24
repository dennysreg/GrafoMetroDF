"""
Lee la lista de adyacencias en formato tsv:
nombre, id, linea, posx, posy, [id_ady1], [id_ady2], ... , [id_adyn]

y genera la lista de distancias mas cortas entre cada par de nodos y la lista de predecesores
que se utiliza para generar la ruta 
algoritmo de floy-warshall 
{
	 "dist": {"0" : {"1": 3, "2":5, ...}}
	,"pred": {"0" : {"3", 3, ....}}	
}
, donde cada nodo posee un diccionario con las distancias hacia todos los demas nodos
, asi como un diccionario con los predecesores, es decir como llegar del nodo actual a un nodo determinado
"""
import json

def floydwarshall(graph):
 
    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = 1000
            pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u
 
    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v] # route new path through t
 
    return dist, pred

if __name__ == '__main__':
	f = open("lista_ady.tsv","r")
	
	#name, id, links
	graph = {}
	for line in f.readlines():
		line = line.split('\t')[:-1]
		source = int(line[1])								
		targets = line[5:]
		vecinos = {}
		for target in targets:
			if target:				
				vecinos[int(target)] = 1
		graph[source] = vecinos

	f.close()
	#print graph	
	
	dist, pred = floydwarshall(graph)
	out = json.dumps({"dist": dist, "pred": pred})
	print out

	#print "Predecesors in shortest path:"
	#for v in pred: print "%s: %s" % (v, pred[v])
	#print "Shortest distance from each vertex:"
	#for v in dist: print "%s: %s" % (v, dist[v])
