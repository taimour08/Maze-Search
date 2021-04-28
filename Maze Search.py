maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 26, 25, 24, 23, 22, 21, 20, 19, 18, 0, 0, 15, 14, 13, 12, 11, 10, 9],
        [0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 14, 0, 0, 0, 10, 0, 0],
        [0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 16, 15, 14, 13, 0, 0, 0, 9, 8, 7],
        [0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 12, 0, 0, 0, 8, 0, 6],
        [0, 0, 22, 21, 20, 19, 0, 0, 0, 0, 14, 0, 0, 11, 10, 9, 8, 7, 0, 5],
        [0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 6, 0, 4],
        [0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 18, 0, 16, 15, 14, 13, 12, 11, 0, 0, 0, 0, 0, 5, 4, 3, 2],
        [0, 0, 18, 17, 0, 15, 0, 0, 12, 0, 10, 0, 0, 0, 6, 0, 4, 0, 0, ],
        [0, 0, 17, 0, 15, 14, 0, 0, 11, 0, 9, 8, 7, 6, 5, 0, 3, 2, 1, 0],
        [0, 0, 18, 0, 16, 15, 14, 0, 12, 0, 0, 0, 0, 0, 6, 0, 4, 0, 0, 0],
        [21, 20, 19, 18, 0, 0, 15, 0, 13, 0, 0, 0, 0, 0, 7, 0, 0, 0, 3, 2],
        [0, 0, 20, 0, 0, 0, 16, 0, 14, 0, 0, 0, 0, 0, 8, 7, 6, 5, 4, 0],
        [0, 0, 21, 20, 19, 18, 17, 0, 15, 0, 0, 0, 0, 0, 9, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

openNodes = []
closedNodes = []
steps = 0


class state:
    def __init__(self, i, j, heuristic):
        self.i = i
        self.j = j
        self.heuristic = heuristic

def noRepeat(i, j):

    f = 1

    for node in closedNodes:
        if node.i == i and node.j == j:
            f = 0
    return f

def checkNodes(i, j):

    if i > 0:  # Up
        if maze[i - 1][j] > 0 and noRepeat(i - 1, j):
            openNodes.append(state(i - 1, j, maze[i - 1][j]))
            print("Up:", i - 1, j, "h:", maze[i - 1][j])

    if j > 0:  # Left
        if maze[i][j - 1] > 0  and noRepeat(i, j - 1):
            openNodes.append(state(i, j - 1, maze[i][j - 1]))
            print("Left:", i, j - 1, "h:", maze[i][j])

    if j < 19:  # Right
        if maze[i][j + 1] > 0 and noRepeat(i, j + 1):
            openNodes.append(state(i, j + 1, maze[i][j + 1]))
            print("Right:", i, j + 1, "h:", maze[i][j + 1])

    if i < 19:  # Down
        if maze[i + 1][j] > 0 and noRepeat(i + 1, j):
            openNodes.append(state(i + 1, j, maze[i + 1][j]))
            print("Down:", i + 1, j, "h:", maze[i + 1][j])


def aStarSearch(maze):

    global steps
    startNode = state(14, 0, 21)  # Make start and end node
    endNode = state(12, 19, 0)

    currentNode = startNode

    openNodes.append(startNode)  # Put in openNode list

    # While until openList empty


    #print("H():", openNodes[1].heuristic)

    # Sort open list
    while (openNodes):
    #for r in range (0,7):
        checkNodes(currentNode.i, currentNode.j)

        low = steps + openNodes[0].heuristic

        # This loop finds the the path with lowest (steps + heuristic) value
        c = 0
        lowNode = 0
        for i in openNodes:
      #      print("Open H:", i.heuristic)
            if steps + i.heuristic < low:
                low = steps + i.heuristic
                lowNode = c  # The index of lowest node, so can be removed from openNodes
            c += 1

       # print("Least: ", lowNode)

# Update values in open/close list and currentNode
        closedNodes.append(openNodes[lowNode])

        currentNode = openNodes[lowNode]
        print("CURRENT: ", currentNode.i, currentNode.j)

        openNodes.pop(lowNode)  # Remove lowest value from open

        steps += 1
        if (currentNode.i == 12 and currentNode.j == 14):
            break

def bestFirstSearch(maze):

    global steps
    startNode = state(14, 0, 21)  # Make start and end node
    endNode = state(12, 19, 0)

    currentNode = startNode

    openNodes.append(startNode)  # Put in openNode list

    # While until openList empty


    #print("H():", openNodes[1].heuristic)

    # Sort open list
    while (openNodes):
    #for r in range (0,7):
        checkNodes(currentNode.i, currentNode.j)

        low = openNodes[0].heuristic

        # This loop finds the the path with lowest (steps + heuristic) value
        c = 0
        lowNode = 0
        for i in openNodes:
      #      print("Open H:", i.heuristic)
            if i.heuristic < low:
                low = i.heuristic
                lowNode = c  # The index of lowest node, so can be removed from openNodes
            c += 1
            if c % 5 == 0:
                steps+=1

       # print("Least: ", lowNode)

# Update values in open/close list and currentNode
        closedNodes.append(openNodes[lowNode])

        currentNode = openNodes[lowNode]
        print("CURRENT: ", currentNode.i, currentNode.j)

        openNodes.pop(lowNode)  # Remove lowest value from open

        steps += 1
        if (currentNode.i == 12 and currentNode.j == 14):
            break


aStarSearch(maze)
print("\nSteps:", steps)