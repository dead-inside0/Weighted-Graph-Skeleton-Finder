#Optional: count time
#import time					
#tic = time.perf_counter()
import json

graph = []#List of all vortexes in the graph & their connections to other vortexes
names = {}#Naming of vortexes
path = []#Lines forming the skeleton
structure = []#Skeleton


#Get shortest path from vortex
def get_shortest_path(list):
  shortest_path = 9999999
  for length in list:
    if length < shortest_path and length != 0:
      shortest_path = length
  return shortest_path

#Load data from json file
json_file = open('graph.json')

dictionary = json.load(json_file)
counter = 0
for key,value in dictionary.items():
  graph.append(value)
  names[str(counter)] = str(key)

json_file.close()

#Add first vortex to structure
structure.append(graph[0])
  
#Repeat len(graph)-1 times 
for i in range(1, len(graph)):
  
  shortest_path = 9999999
  
  actual_vortex: list
  #Get shortest path from structure
  for vortex in structure:
    
    length = get_shortest_path(vortex)
    
    if length < shortest_path and length != 0:
      
      actual_vortex = structure[structure.index(vortex)]
      
      shortest_path = length
  #Add vortex to structure
  structure.append(graph[actual_vortex.index(shortest_path)])
  #Add line leading to vortex to path
  path.append((str(graph.index(actual_vortex)), str(actual_vortex.index(shortest_path))))
  #Set the line to 0 in graph so it doesn't repeat
  graph[actual_vortex.index(shortest_path)][graph.index(actual_vortex)] = 0
  graph[graph.index(actual_vortex)][actual_vortex.index(shortest_path)] = 0
#Output lines
for tuple in path:
  print(tuple[0] + ',' + tuple[1])

#Optional: count & print time
#toc = time.perf_counter()
#print(f"Operation completed in {toc - tic} seconds")
