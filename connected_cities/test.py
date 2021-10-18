import  os
import unittest
from solution.config import Config
from solution.utils import *

class TestConnectivityApp(unittest.TestCase):
    
    def test_File(self):
        # Check if the data.txt file is not empty
        self.assertTrue(os.path.getsize(Config.MY_FILE_PATH) != 0)


    def test_Adjacency_Graph(self):
        """
        Use the data.txt file to get a list of all unique cities.
        Compare the number of unique cities to number of keys in adjacency matrix before dfs search.
        """
        cityList = []
        with open(Config.MY_FILE_PATH) as f:
            for s in f.readlines():
                if s.strip() != '':
                    try:
                        cityList.append((s.split(','))[0].strip())
                        cityList.append((s.split(','))[1].strip())
                    except:
                        continue
        f.close()
        uniquecityList = set(cityList)
        CC = Connecting_Cities('Testa','Testb',Config.MY_FILE_PATH)
        graph = CC.process_file()
        self.assertEqual(len(uniquecityList), len(list(graph.keys())))


    def test_DFS(self):
        """
        Use a test graph to check DFS search algorithm is working as expected.
        """
        testGraph = {"A":["D","C","B"],
                        "B":["E"],
                        "C":["G","F"],
                        "D":["H"],
                        "E":["I"],
                        "F":["J"]}
        CC = Connecting_Cities('A','H','')
        self.assertTrue(CC.connectivity(testGraph))

if __name__ == '__main__':
    unittest.main()

