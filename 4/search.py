# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    temp = []
    for g in grid:
        temp.append(g[:])
    temp[init[0]][init[1]] = 1
    if init == goal:
        return [cost, init[0], init[1]]

    isStuck = 1
    result = []
    for d in delta:
        if (init[0] + d[0] >= 0 and init[0] + d[0] < len(grid) and
            init[1] + d[1] >= 0 and init[1] + d[1] < len(grid[0])):
            coord = [init[0] + d[0], init[1] + d[1]]
            if (grid[coord[0]][coord[1]] == 0):
                isStuck = 0
                result.append(search(temp, coord, goal, cost + 1))

    if isStuck:
        return 'fail'
    minval = None
    path = 'fail'
    for r in result:
        if r != 'fail' and (minval == None or r[0] < minval):
            minval = r[0]
            path = r
        
    return path


print (search(grid, init, goal, 0))
