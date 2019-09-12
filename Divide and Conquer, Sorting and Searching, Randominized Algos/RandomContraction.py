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
        vertex = random.randint(1, len(vertices) + 1)
        edge = random.randint(1, len(vertices[vertex]) + 1)
        vertexToKeep = vertices[vertex][0]
        vertexToRemove = vertices[edge][0]


        # note here remove will only remove the first occurence, but we want to remove all occurences
        vertices[edge] = list(filter((vertexToKeep).__ne__, vertices[edge]))
        # merge two lists, might create duplicates but that's fine
        vertices[vertex] = vertices[vertex] + vertices[edge]
        vertices[vertex] = list(filter((vertexToRemove).__ne__, vertices[vertex]))

        del vertices[edge]

        # clean other involved vertices
        # might create dups as well
        for i in range(len(vertices)):
            if vertexToRemove in vertices[i]:
                vertices[i] = [vertexToKeep if x == vertexToRemove else x for x in vertices[i]]
    
    # after only two vertices left
        

