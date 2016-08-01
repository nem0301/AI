"""
p = [[1./9, 1./9, 1./9],
     [1./9, 1./9, 1./9],
     [1./9, 1./9, 1./9]]
"""

p = [[1./9, 1./9, 1./9],
     [1./9, 1./9, 1./9],
     [1./9, 1./9, 1./9]]



color = [['green', 'green', 'green'],
         ['green', 'red', 'red'],
         ['green', 'green', 'green']]

measurements = ['red', 'red']

motions=[[0, 0], [0, 1]]

sensor_right = 0.8
p_move = 1.0


for k in range(2):
    q = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range (3):
        for j in range(3):
            hit = (measurements[k] == color[i][j])
            q[i][j] = (p[i][j] * (hit * sensor_right + (1 - hit) * (1.0 - sensor_right)))
   
    s = 0
    for i in range (3):
        s += sum(q[i])

    for i in range(3):
        for j in range(3):
            p[i][j] = q[i][j]/s
    
    q = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range (3):
        for j in range(3):
            r = motions[k][0]
            c = motions[k][1]
            
            s2 = p_move * p[(i - r) % 3][(j - c) % 3]
            s2 += (1.0 - p_move) * p[i][j]
            q[i][j] = s2


    p = q[:]
    


for i in range(3):
    for j in range(3):
        print ('[%.5f] ' % p[i][j], end="")

    print()

