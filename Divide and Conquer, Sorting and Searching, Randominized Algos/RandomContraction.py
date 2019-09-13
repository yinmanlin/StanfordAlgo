import random


def Contraction(vertices):
    # read in data as list of list
    # first randomly pick a row
    # then fetch the length of the row
    # then randomly pick a column from the row
    # then count how many common numbers they have in the row
    # self loop is duplicates in the row

    while (len(vertices)) > 2:
        # keep vertex, remove edge
        vertexToKeepLocation = random.randint(0, len(vertices) - 1)
        vertexToRemoveLocation = random.randint(1, len(vertices[vertexToKeepLocation]) - 1) 
        vertexToKeep = vertices[vertexToKeepLocation][0]
        vertexToRemove = vertices[vertexToKeepLocation][vertexToRemoveLocation]

        # find the vertex to remove vector
        for i in range(len(vertices)):
            if vertexToRemove == vertices[i][0]:
                removeLocation = i
                break
        
        del vertices[removeLocation][0]
        vertices[removeLocation] = list(filter((vertexToKeep).__ne__, vertices[removeLocation]))
        vertices[vertexToKeepLocation] = list(filter((vertexToRemove).__ne__, vertices[vertexToKeepLocation]))

        vertices[vertexToKeepLocation] = vertices[vertexToKeepLocation] + vertices[removeLocation]

        del vertices[removeLocation]

        # clean other involved vertices
        # might create dups as well
        for i in range(len(vertices)):
            if vertexToRemove in vertices[i]:
                vertices[i] = [vertexToKeep if x == vertexToRemove else x for x in vertices[i]]
    
    # after only two vertices left
    return len(vertices[0]) - 1

with open('kargerMinCut.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
content = [x.split('\t') for x in content] 
content = [[int(j) for j in i] for i in content]
#print(content)

minCutCount=[]
for i in range(10000):
    minCutCount.append(Contraction(content))

print(min(minCutCount))