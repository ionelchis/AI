from random import randint

def generate(vertices, filename, maxweight):
    graph = [[0 for column in range(vertices)] for row in range(vertices)]
    f = open(filename, "w")
    for i in range(vertices):
        j = i
        while j < vertices:
            if i == j:
                graph[i][j] = 0
            elif i < j:
                graph[i][j] = graph[j][i] = randint(1, maxweight)
            j += 1
    
    f.write(str(vertices) + "\n")
    for rows in graph:
        for col in range(vertices):
            if col < vertices-1:
                f.write(str(rows[col]) + ",")
            else:
                f.write(str(rows[col]))
        f.write("\n")
    
    f.close()


#generate(100, "graph2.txt")
#generate(50, "graph3.txt")
#generate(150, "graph4.txt")
#generate(500, "graph5.txt")
filename = "graph8.txt"
vertices = 5
generate(vertices, filename, 10)
with open(filename, "a+") as f:
    x1 = randint(1, vertices+1)
    x2 = randint(1, vertices+1)
    f.write(str(x1) + "\n" + str(x2))
