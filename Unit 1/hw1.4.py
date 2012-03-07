colors = [['red', 'green', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8


def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []
row = len(colors)
col = len(colors[0])
pro = 1. / (row * col)
for i in range(row):
    t = []
    for j in range(len(colors[i])):
        t.append(pro)
    p.append(t)


def sense(p, Z):
    q = []
    s = 0
    for i in range(len(p)):
        t = []
        for j in range(len(p[i])):
            hit = (Z == colors[i][j])
            t.append(p[i][j] * (hit * sensor_right + (1 - hit) * (1 - sensor_right)))
        q.append(t)
        s = s + sum(t)
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = q[i][j] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        t = []
        for j in range(len(p[i])):
            s = p_move * p[(i - U[0]) % len(p)][(j - U[1]) % len(p[i])]
            s = s + (1 - p_move) * p[i % len(p)][j % len(p[i])]
            t.append(s)
        q.append(t)
    return q

for i in range(len(motions)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])
#Your probability array must be printed
#with the following code.

show(p)
