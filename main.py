#import time					
#tic = time.perf_counter()
import json

graph = []
names = {}
path = []
structure = []



def get_shortest_path(list):
  shortest_path = 9999999
  for length in list:
    if length < shortest_path and length != 0:
      shortest_path = length
  return shortest_path

json_file = open('graph.json')

dictionary = json.load(json_file)
counter = 0
for key,value in dictionary.items():
  graph.append(value)
  names[str(counter)] = str(key)

json_file.close()

structure.append(graph[0])
  
for i in range(1, len(graph)):
  
  shortest_path = 9999999
  
  actual_vortex: list
  
  for vortex in structure:
    
    length = get_shortest_path(vortex)
    
    if length < shortest_path and length != 0:
      
      actual_vortex = structure[structure.index(vortex)]
      
      shortest_path = length
      
  structure.append(graph[actual_vortex.index(shortest_path)])
  
  path.append((str(graph.index(actual_vortex)), str(actual_vortex.index(shortest_path))))
  
  graph[actual_vortex.index(shortest_path)][graph.index(actual_vortex)] = 0
  
  graph[graph.index(actual_vortex)][actual_vortex.index(shortest_path)] = 0

for tuple in path:
  print(tuple[0] + ',' + tuple[1])

#toc = time.perf_counter()
#print(f"Operation completed in {toc - tic} seconds")
