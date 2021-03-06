from timeit import default_timer as timer
import heapq

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


    def minDistance(self, node, visited): 
  
        # Initilaize minimum distance for next node 
        min = float('inf')
  
        # Search not nearest vertex not in the  
        # shortest path tree
        min_index = 0
        for v in range(self.V): 
            if visited[v] == False and self.graph[node][v] < min:
                min = self.graph[node][v]
                min_index = v
        
        return min_index

    #dis boi fast pe grafe mari
    def tsp(self, src):
        """
        Cel mai scurt traseu care pleaca din locatia src si viziteaza toate locatiile si revine in src
        Input: src - int, <= self.V
        Output:
            first line: number of cities (n)
            second line: the optimal traversing path that visits all the cities (indexes of cities, starting by 1)
            third line: the value of the optimal path through all the cities (real value)
        
        Complexitate: O(V^2)
        """
        dist = [float('inf')] * self.V
        path = []
        src -= 1
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            visited[src] = True
            u = self.minDistance(src, visited)
            # path[i] = src+1
            path.append(src+1)
            #print(">>> ", src, u, path)
            dist[u] = dist[src] + self.graph[src][u]
            src = u
        
        with open("tsp-solution.txt", "w") as f:
            f.write(str(len(path)) + "\n")
            f.write(str(path).strip("[]") + "\n")
            f.write(str(dist[src]) + "\n")
        # print(len(path))
        # print(str(path).strip("[]"))
        # print(dist[0])

    #dis boi fast pe grafe mici
    def dijkstra(self, src, dest):
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
        

        Complexitate: O(ElogV)
        """
        dist = [float('inf')] * self.V
        heap = []
        heapq.heappush(heap, (0, src-1))
        path = dict()
        dist[src-1] = 0
        path[src-1] = -1
        visited = [False] * self.V

        cycle = False
        if src == dest:
            cycle = True
        
        while heap != []:
            u = heapq.heappop(heap)
            if cycle:
                heap = []
            vecin = u[1]
            cost = u[0]
            visited[vecin] = True
            for v in range(self.V):
                if cycle:
                    if visited[v] == False and self.graph[vecin][v] > 0:
                        dist[v] = cost + self.graph[vecin][v]
                        heapq.heappush(heap, (dist[v], v))
                        path[v] = vecin
                else:
                    if visited[v] == False and self.graph[vecin][v] > 0 and dist[v] > cost + self.graph[vecin][v]:
                        dist[v] = cost + self.graph[vecin][v]
                        heapq.heappush(heap, (dist[v], v))
                        path[v] = vecin

        # print(dist)
        # print(path)
        if cycle:
            dist[dest-1] = u[0] + self.graph[u[1]][dest-1]
            path[dest-1] = u[1]
            
        # print(dist)
        # print(path)
        node = path[dest-1]
        path[src-1] = -1
        if not cycle:
            drum = [dest]
        else:
            drum = []
        while node != -1:
            drum.append(node+1)
            node = path[node]
        drum.reverse()
        with open("tsp-solution.txt", "a+") as f:
            f.write(str(len(drum)) + "\n")
            f.write(str(drum).strip("[]") + "\n")
            f.write(str(dist[dest-1]) + "\n")
        # print(len(drum))
        # print(str(drum).strip("[]"))
        # print(dist[dest-1])

def run():
    #Start timer
    start = timer()
    filename = "graph4.txt"
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
    #End timer
    end = timer()
    print("Exec time pentru read: ", end-start)

    with open("tsp-solution.txt", "w") as f:
        f.write("")

    start = timer()
    g.tsp(1)
    end = timer()
    print("Exec time pentru a vizita toate orasele (v1): ", end-start)

    start = timer()
    g.dijkstra(1, 1)
    end = timer()
    print("Exec time pentru a vizita toate orasele (djk): ", end-start)

    start = timer()
    g.dijkstra(src, dest)
    end = timer()
    print("Exec time pentru src-dest (djk): ", end-start)


    # g.dijkstra(1, 1)
    # g.dijkstra(src, dest)

run()
