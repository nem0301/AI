# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))] 
    
    x = goal[0]
    y = goal[1]
    value[x][y] = 0

    open = [[0, x, y]]

    while len(open) != 0:
        next = open.pop()
        x = next[1]
        y = next[2]
        value[x][y] = next[0]
        
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                if value[x2][y2] > value[x][y] + 1 and grid[x2][y2] != 1:
                    value[x2][y2] = value[x][y] + 1
                    open.append([value[x2][y2], x2, y2])

    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 


for p in compute_value(grid, goal, cost):
    print (p)
