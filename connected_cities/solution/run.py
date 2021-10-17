
from itertools import groupby
from collections import defaultdict
import os


class Connecting_Cities:

    def __init__(self, source, dest, textFile):
        self.source = source
        self.dest = dest
        self.textFile = textFile

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


    def process_file(self):
        kv = []
        with open(self.textFile) as f:
            for s in f.readlines():
                kv.append(((s.split(','))[0].strip() ,(s.split(','))[1].strip()))
        graph = defaultdict(list)
        for k,v in groupby(kv, lambda x:x[0]):
            graph[k].append([i[1] for i in list(v)][0])
        #print(graph)
        f.close()
        return graph


    def process_result(self, result):
        if result:
            return ('There is a connection between '+ self.source+ ' and ' + self.dest + '!')
        else:
            return ('No connection between '+ self.source+ ' and ' + self.dest + '!')



if __name__ == '__main__':
    CC = Connecting_Cities('Boston', 'Portland', 'solution/data.txt')
    graph = CC.process_file()
    res = CC.connectivity(graph)
    print(CC.process_result(res))
    

    
        
    
    