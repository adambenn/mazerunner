from maze import *
from generator import *
import random

if __name__ == "__main__":
    #random.seed(12345)
    maze = Maze(5)
    print("Testing DFS generation")

    # maze.generate(DFSGenerator(debug = True))
    maze.generate(DFSGenerator())
    print(maze.graphicalRepresentation())