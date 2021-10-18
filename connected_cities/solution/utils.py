
from itertools import groupby
from collections import defaultdict
import os

class Connecting_Cities:

    def __init__(self, source, dest, textFile):
        self.source = source
        self.dest = dest
        self.textFile = textFile

    """
    Paired cities fetched line wise from textfile and converted to adjacency matrix/graph.
    Pair reverse also appended to the graph.
    """
    def process_file(self):
        kv = []
        with open(self.textFile) as f:
            for s in f.readlines():
                if s.strip() != '':
                    try:
                        kv.append(((s.split(','))[0].strip() ,(s.split(','))[1].strip()))
                        kv.append(((s.split(','))[1].strip() ,(s.split(','))[0].strip())) # Reverse pair
                    except:
                        print('Error Handler: Invalid input line found! Line skipped.')
        graph = defaultdict(list)
        for k,v in groupby(kv, lambda x:x[0]):
            graph[k].append([i[1] for i in list(v)][0])
        #print(graph)
        f.close()
        return graph

    """
    Traverse graph using Depth-first search starting from source city ending on destination city
    Return False if no destination found.
    """
    def connectivity(self, graph):
        flag = 0
        visited = set()
        def dfs(visited, graph, source, dest):
            if source == dest:
                return True
            if source in visited:
                return False
            else:
                visited.add(source)
                for next_city in graph[source]:
                    if dfs(visited, graph, next_city, dest): 
                        return True
        return (dfs(visited,graph,self.source,self.dest))

    def process_result(self, result):
        if result:
            return ('There is a connection between '+ self.source+ ' and ' + self.dest + '!')
        else:
            return ('No connection between '+ self.source+ ' and ' + self.dest + '!')
