import math
import random
import time

'''MONTE CARLO METHOD
DRAWING COORDINATES
THEN CHECK THAT THE LENGTH FROM POINT (X, Y) <= RADIUS
'''


def generator_pi(a, it):
    r = 0.5 * a
    shots = 0
    o_x = r
    o_y = r

    # drawing coordinates x,y
    # starting point in  (0,0)

    for i in range(it):
        x = random.uniform(0,a)
        y = random.uniform(0,a)
        length = math.sqrt((o_x - x) ** 2 + (o_y - y) ** 2)
        if length <= r:
            shots += 1

    return 4*(shots / (it))

start = time.time()

print(generator_pi(1, 10000))

stop = time.time()
print('Executed in {} seconds'.format(stop-start))

