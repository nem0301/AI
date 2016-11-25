#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'green', 'red', 'green', 'red']
measurements = ['red', 'red']
motions = [1,1]
pHit = 0.9
pMiss = 0.1
pExact = 1.0
pOvershoot = 0.0
pUndershoot = 0.0

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))

    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        m = i - U
        if m > len(p) - 1:
            m = len(p) - 1
        if m < 0:
            m = 0

        q.append(p[m])
    return q



p1 = sense(p, measurements[0])

p2 = []
p2.append(p1[0] * 0.1)
p2.append(p1[1] * 0.9)
p2.append(p1[2] * 0.1)
p2.append(p1[3] * 0.9)
p2.append(p1[4] * 0.9)

print sum(p2)
