"""
Lee la lista de adyacencias en formato tsv:
nombre, id, linea, terminal, posx, posy, [id_ady1], [id_ady2], ... , [id_adyn]

y lo convierte a formato JSON
{
	"nodes": [{"y": 452.186, "x": 66.31, "terminal": 1, name": "Observatorio", "linea": 1}, ..., ]
	,"links": [{"source": 162, "target": 161, "linea": 12}, ..., ]
}
"""
import json

f = open("lista_ady.tsv","r")
nodos = []
links = []
#name, id, links
nums = []
for line in f.readlines():
	line = line.split('\t')[:-1]
	source = int(line[1])
	nums.append(source)
	name = line[0]
	linea = int(line[2])
	terminal = int(line[3])
	x = float(line[4])
	y = float(line[5])
	targets = line[6:]
	nodos.append({"name": name, "linea": linea, "terminal": terminal, "x":x, "y": y})
	for target in targets:
		if target:
			links.append({"source": source, "target":int(target), "linea": linea })
			nums.append(int(target))

#print max(nums), min(nums)
print json.dumps({"links": links,"nodes": nodos})
