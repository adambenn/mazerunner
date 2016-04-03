import math

def heur_uniform_cost(maze, n):
    return 0

def heur_straight_line(maze, n):
    m = maze.exit.coordinate
    n = n.coordinate
    return math.sqrt((m[0] - n[0])**2 +  (m[1] - n[1])**2)