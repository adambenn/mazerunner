import math

def heur_uniform_cost(maze, n):
    return 0

def heur_straight_line(maze, n):
    m = maze.exit.coordinate
    c = n.coordinate
    return math.sqrt((m[0] - c[0])**2 +  (m[1] - c[1])**2)

def heur_manhattan(maze, n):
    m = maze.exit.coordinate
    c = n.coordinate
    return abs(m[0] - c[0]) + abs(m[1] + c[1])