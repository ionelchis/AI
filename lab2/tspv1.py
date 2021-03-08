from timeit import default_timer as timer
import heapq

inf = float('inf')

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


    def minDistance(self, node, visited): 
        # min = float('inf')
        min = inf
        # Cauta cel mai apropiat vecin
        min_index = 0
        for v in range(self.V): 
            if visited[v] == False and self.graph[node][v] < min:
                min = self.graph[node][v]
                min_index = v
        
        return min_index

    def tsp2(self, src, dest):
        """
        Daca src == dest
            Cel mai scurt traseu care pleaca din locatia src si viziteaza toate locatiile si revine in src
        Daca src != dest
            Cel mai scurt traseu care pleaca din locatia src si ajunge in locatia dest
        Input: src - int, <= self.V; dest - int, <= self.V
        Output:
        Daca src == dest:
            first line: number of cities (n)
            second line: the optimal traversing path that visits all the cities (indexes of cities, starting by 1)
            third line: the value of the optimal path through all the cities (real value)
        Altfel:
            first line: the length (in number of cities) of the optimal path from the source city to the destination city
            second line: the optimal traversing path from the source city to the destination city (indexes of cities, starting by source city and ending by destination city)
            third line: the value of the optimal path from the source city to the destination city
        
        Complexitate: O(V^2)
        """
        # dist = [float('inf')] * self.V
        dist = [inf] * self.V
        path = []
        src -= 1
        dest -= 1
        dist[src] = 0

        visited = [False] * self.V
        
        for count in range(self.V):
            visited[src] = True
            u = self.minDistance(src, visited)
            # path[count] = src+1
            path.append(src+1)
            # print(">>> ", src, u, path)
            dist[u] = dist[src] + self.graph[src][u]
            if src == dest and count != 0:
                break
            src = u
  
        self.__print_solution("tsp-solution.txt", path, dist, src)
    
    def __print_solution(self, filename, path, dist, src):
        with open(filename, "a+") as f:
            f.write(str(len(path)) + "\n")
            f.write(str(path).strip("[]") + "\n")
            f.write(str(dist[src]) + "\n")


def read_graph(filename):
    with open(filename, "r") as f:
        src = dest = 0
        g = Graph(int(f.readline()))
        graph = []
        for _ in range(g.V):
            line = f.readline()
            graph.append([int(x) for x in line.split(",")])
        src = int(f.readline())
        dest = int(f.readline())
        g.graph = graph
    return g, src, dest

def run():
    #Start timer
    start = timer()
    # filename = "easy_01_tsp.txt"
    # filename = "medium_01_tsp.txt"
    filename = "hard_01_tsp.txt"
    # filename = "graph10.txt"

    g, src, dest = read_graph(filename)
    
    #End timer
    end = timer()
    print("Exec time pentru read: ", end-start)

    with open("tsp-solution.txt", "w") as f:
        f.write("")

    start = timer()
    g.tsp2(1, 1)
    end = timer()
    print("Exec time pentru a vizita toate orasele: ", end-start)

    start = timer()
    g.tsp2(src, dest)
    end = timer()
    print("Exec time pentru a vizita toate orasele " + str(src) + "-" + str(dest) + ": ", end-start)


run()
